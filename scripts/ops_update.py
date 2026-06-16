#!/usr/bin/env python3
"""
Mollie Ops Board Auto-Updater v3
Reads new Fathom transcripts + Slack messages + Gmail threads + Memory notes
from the last 25h, combines into unified context, sends to Claude Haiku for
structured JSON extraction, then does a smart merge into ops-data.json and
pushes to GitHub Pages.

Runs inside Inbox Monitor cron (7am + 5pm) — NOT standalone.
Author: Mollie / DigitsUp
Created: 2026-06-08
Updated: v3 — Multi-source: Fathom + Slack + Gmail + Memory
"""

import os
import json
import base64
import re
import sys
import subprocess
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
WORKSPACE          = Path("/Users/minigrill/.openclaw/workspace")
OPS_DATA_PATH      = WORKSPACE / "mollie-ops" / "ops-data.json"
CLIENTS_DIR        = WORKSPACE / "clients"
MEMORY_DIR         = WORKSPACE / "memory"
GH_TOKEN_PATH      = Path.home() / ".config" / "github" / "token"
ANTHROPIC_KEY_PATH = Path.home() / ".config" / "anthropic" / "api_key"
GH_REPO            = "DigitsUp/mollie-ops"
GH_FILE            = "ops-data.json"
OPS_URL            = "https://digitsup.github.io/mollie-ops/"
LOOKBACK_HOURS     = 25  # slightly over 24h to catch edge cases

# Dry run mode: set OPS_DRY_RUN=1 to skip GitHub push (for testing)
DRY_RUN = os.environ.get("OPS_DRY_RUN", "") == "1"

# Client ID → folder name mapping (ops board id → clients/ subfolder)
# NOTE: hiba → hiba-academy (Fathom routes to clients/hiba-academy/)
CLIENT_FOLDER_MAP = {
    "frnk":        "frnk-boutique",
    "rvca":        "rvca",
    "salehe":      "salehe-bembury",
    "hiba":        "hiba-academy",    # FIXED: was "hiba", Fathom routes to hiba-academy/
    "the-lab":     "the-lab",
    "epicure":     "epicure",
    "riversol":    "riversol",
    "outersignal": "outersignal",
    "sfr":         "sfr-distillery",
}

# Fallback dot color heuristics (used when LLM call fails)
RED_SIGNALS   = ["blocked", "broken", "urgent", "overdue", "past due", "critical", "failed", "error"]
AMBER_SIGNALS = ["in progress", "building", "pending", "waiting", "needs", "review needed", "draft"]
GREEN_SIGNALS = ["live", "launched", "complete", "done", "signed", "approved", "delivered", "✅"]

# Claude model preference
CLAUDE_MODELS = ["claude-haiku-4-5", "claude-haiku-4-0"]

# ── New: Slack Config ─────────────────────────────────────────────────────────
SLACK_CHANNEL_MAP = {
    "epicure":     ["C095H8FCQF7", "C09C5LE2USW"],   # epicure, epicure-external
    "rvca":        ["C0ANTES075L", "C0B2YGKQDGX"],    # rvca, rvca-external
    "salehe":      ["C0B505T49NX"],                    # salehe-bembury
    "frnk":        ["C0B4E5DQRRV"],                   # frnk-boutique
    "riversol":    ["C096D0MB4SD"],                    # riversol-skincare
    "sfr":         ["C0BAM4QM4QM"],                   # sfr-distillery
    "the-lab":     ["C0B6Z7ESJ0N"],                   # lab-life
    "outersignal": ["C0AQ4K1MK4H", "C0B690055A6"],   # outersignal, outersignal-digitsup
    "hiba":        ["C08GK09GG14"],                   # hiba
}

# Static channel ID → display name map (from brief comments)
SLACK_CHANNEL_NAMES = {
    "C095H8FCQF7": "epicure",
    "C09C5LE2USW": "epicure-external",
    "C0ANTES075L": "rvca",
    "C0B2YGKQDGX": "rvca-external",
    "C0B505T49NX": "salehe-bembury",
    "C0B4E5DQRRV": "frnk-boutique",
    "C096D0MB4SD": "riversol-skincare",
    "C0BAM4QM4QM": "sfr-distillery",
    "C0B6Z7ESJ0N": "lab-life",
    "C0AQ4K1MK4H": "outersignal",
    "C0B690055A6": "outersignal-digitsup",
    "C08GK09GG14": "hiba",
}

SLACK_TOKEN_PATH      = Path.home() / ".config" / "slack" / "bot_token"
SLACK_LOOKBACK_HOURS  = 25
SLACK_API_BASE        = "https://slack.com/api"

SIGNAL_WORDS = [
    "approved", "accepted", "rejected", "signed", "confirmed", "done", "live",
    "blocked", "delayed", "pushed", "waiting", "need", "urgent", "asap",
    "brief", "build", "launch", "send", "schedule", "deadline", "due",
    "feedback", "revision", "change", "update", "fix", "broken",
    "meeting", "call", "tomorrow", "monday", "tuesday", "wednesday", "thursday", "friday",
    "this week", "next week", "going live", "ready to", "can you", "please",
    "✅", "🔴", "⚠️", "❌", "🚀"
]

# ── New: Gmail Config ─────────────────────────────────────────────────────────
GOG_BIN            = "gog"
GMAIL_ACCOUNT      = "mollie@digitsup.com"
GMAIL_LOOKBACK_DAYS = 2

CLIENT_EMAIL_HINTS = {
    "epicure":     ["epicure.com", "geoff@", "amelia@epicure", "cindy@epicure"],
    "rvca":        ["rvca.com", "clay", "clayton"],
    "salehe":      ["fardad", "salehe"],
    "frnk":        ["frnk", "kieran"],
    "riversol":    ["riversol.com", "arnaud", "victoria@riversol"],
    "sfr":         ["sfrdistillery.com", "will.rogers@stratford"],
    "the-lab":     ["thelab", "lab life"],
    "outersignal": ["outersignal.com", "christy", "sam@"],
    "hiba":        ["hibaacademy", "veronica"],
}

# ── New: Memory Config ────────────────────────────────────────────────────────
# PRIMARY hints: client's own name/brand — MUST appear for a paragraph to match
# SECONDARY hints: people names — only used to confirm if primary already matched
# This prevents cross-client contamination (e.g. "Victoria" appearing in both RVCA + Riversol)
CLIENT_PRIMARY_HINTS = {
    "epicure":     ["Epicure"],
    "rvca":        ["RVCA"],
    "salehe":      ["Salehe", "SPUNGE", "Sponge"],
    "frnk":        ["FRNK"],
    "riversol":    ["Riversol"],
    "sfr":         ["SFR Distillery", "SFR", "Stratford"],
    "the-lab":     ["The Lab Life", "The Lab", "Lab Life"],
    "outersignal": ["OuterSignal"],
    "hiba":        ["Hiba"],
}
# Secondary hints only used to enrich context — never used alone to match a paragraph
CLIENT_NAME_HINTS = {
    "epicure":     ["Epicure", "Geoff", "Amelia", "Cindy"],
    "rvca":        ["RVCA", "Clay", "Clayton"],
    "salehe":      ["Salehe", "Fardad", "SPUNGE", "Sponge"],
    "frnk":        ["FRNK", "Kieran", "Megan"],
    "riversol":    ["Riversol", "Arnaud"],
    "sfr":         ["SFR", "Stratford", "Will Rogers", "Lawrence"],
    "the-lab":     ["The Lab", "Lab Life"],
    "outersignal": ["OuterSignal", "Christy", "Christy Dawn", "Dov"],
    "hiba":        ["Hiba", "Veronica"],
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_ops_data():
    if not OPS_DATA_PATH.exists():
        print(f"  ✗ ops-data.json not found at {OPS_DATA_PATH}")
        sys.exit(1)
    return json.loads(OPS_DATA_PATH.read_text())


def save_ops_data(data):
    OPS_DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def get_gh_token():
    return GH_TOKEN_PATH.read_text().strip()


def get_anthropic_key():
    return ANTHROPIC_KEY_PATH.read_text().strip()


def find_new_meeting_files(lookback_hours=LOOKBACK_HOURS):
    """Find all meeting markdown files modified in the last N hours."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    found = []
    for client_dir in CLIENTS_DIR.iterdir():
        meetings_dir = client_dir / "meetings"
        if not meetings_dir.exists():
            continue
        for f in meetings_dir.glob("*.md"):
            mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
            if mtime > cutoff:
                found.append((client_dir.name, f))
    return found


def extract_summary_sections(content):
    """
    Extract Key Takeaways and Next Steps raw text from a Fathom transcript.
    Returns (takeaways_text, next_steps_text) as raw strings for LLM consumption.
    Also returns (takeaways_list, next_steps_list) for fallback heuristics.
    """
    takeaways_text = ""
    next_steps_text = ""
    takeaways_list = []
    next_steps_list = []

    # Key Takeaways — capture the raw section
    kt_match = re.search(r'## Key Takeaways\s*(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if kt_match:
        takeaways_text = kt_match.group(1).strip()
        # Also parse structured bullets for fallback
        items = re.findall(r'\*\*([^*]+)\*\*[:\s]*([^\n]*)', takeaways_text)
        for bold, rest in items:
            line = (bold + " " + rest).strip()
            if line:
                takeaways_list.append(line)

    # Next Steps — capture the raw section
    ns_match = re.search(r'## Next Steps\s*(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if ns_match:
        next_steps_text = ns_match.group(1).strip()
        # Also parse for fallback
        items = re.findall(r'\[([^\]]+)\]', next_steps_text)
        for item in items[:5]:
            clean = item.strip()
            if len(clean) > 20:
                next_steps_list.append(clean)

    return takeaways_text, next_steps_text, takeaways_list, next_steps_list


def has_signal(text):
    """Return True if the message text contains any signal word (case-insensitive)."""
    text_lower = text.lower()
    for word in SIGNAL_WORDS:
        if word.lower() in text_lower:
            return True
    return False


# ── New Source: Slack ─────────────────────────────────────────────────────────

def _slack_api_get(path, params, token):
    """Make a GET request to the Slack API. Returns parsed JSON or raises."""
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{SLACK_API_BASE}/{path}?{query}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def collect_slack_messages():
    """
    Pull filtered Slack messages from the last 25h for all clients.
    Returns dict: {client_id: formatted_text_block}
    Also returns stats: {client_id: int (message count)}
    """
    result = {}
    stats = {}

    if not SLACK_TOKEN_PATH.exists():
        print(f"  ⚠ Slack: token not found at {SLACK_TOKEN_PATH} — skipping")
        return result, stats

    token = SLACK_TOKEN_PATH.read_text().strip()
    if not token:
        print(f"  ⚠ Slack: token file is empty — skipping")
        return result, stats

    oldest = str((datetime.now(timezone.utc) - timedelta(hours=SLACK_LOOKBACK_HOURS)).timestamp())

    for client_id, channel_ids in SLACK_CHANNEL_MAP.items():
        client_blocks = []
        client_msg_count = 0

        for channel_id in channel_ids:
            channel_name = SLACK_CHANNEL_NAMES.get(channel_id, channel_id)

            try:
                # Pull channel history
                data = _slack_api_get("conversations.history", {
                    "channel": channel_id,
                    "oldest": oldest,
                    "limit": "100"
                }, token)

                if not data.get("ok"):
                    err = data.get("error", "unknown")
                    print(f"  ⚠ Slack: {channel_name} — API error: {err}")
                    continue

                messages = data.get("messages", [])

                # Track which thread_ts we've already fetched
                fetched_threads = set()

                for msg in messages:
                    text = msg.get("text", "")
                    ts = msg.get("ts", "")
                    thread_ts = msg.get("thread_ts")
                    reply_count = msg.get("reply_count", 0)
                    user = msg.get("user", msg.get("username", "unknown"))

                    # Format timestamp
                    try:
                        dt = datetime.fromtimestamp(float(ts), tz=timezone.utc).astimezone()
                        dt_str = dt.strftime("%Y-%m-%d %H:%M")
                    except Exception:
                        dt_str = ts

                    # Build thread context if there are replies
                    thread_lines = []
                    if thread_ts and reply_count > 0 and thread_ts not in fetched_threads:
                        fetched_threads.add(thread_ts)
                        try:
                            thread_data = _slack_api_get("conversations.replies", {
                                "channel": channel_id,
                                "ts": thread_ts,
                                "oldest": oldest,
                                "limit": "20"
                            }, token)
                            if thread_data.get("ok"):
                                for reply in thread_data.get("messages", [])[1:]:  # skip parent
                                    r_text = reply.get("text", "")
                                    r_user = reply.get("user", reply.get("username", "unknown"))
                                    if r_text:
                                        thread_lines.append(f"  ↳ {r_user}: {r_text}")
                        except urllib.error.HTTPError as e:
                            if e.code == 429:
                                print(f"  ⚠ Slack: rate limited on thread fetch for {channel_name} — skipping thread")
                            # else skip silently

                    # Combine message + thread text for signal filtering
                    full_text = text + "\n" + "\n".join(thread_lines)
                    if not has_signal(full_text):
                        continue

                    # Format the block
                    header = f"[SLACK — #{channel_name} — {dt_str}]"
                    block = header + f"\n{user}: {text}"
                    if thread_lines:
                        block += "\n" + "\n".join(thread_lines)
                    client_blocks.append(block)
                    client_msg_count += 1

            except urllib.error.HTTPError as e:
                if e.code == 429:
                    print(f"  ⚠ Slack: rate limited on {channel_name} — skipping channel")
                else:
                    print(f"  ⚠ Slack: HTTP {e.code} on {channel_name} — skipping")
            except Exception as e:
                print(f"  ⚠ Slack: unexpected error on {channel_name}: {str(e)[:100]}")

        if client_blocks:
            result[client_id] = "\n\n".join(client_blocks)
        stats[client_id] = client_msg_count

    return result, stats


# ── New Source: Gmail ─────────────────────────────────────────────────────────

def collect_gmail_threads():
    """
    Pull relevant Gmail threads for each client via gog CLI.
    Returns dict: {client_id: formatted_text_block}
    Also returns stats: {client_id: int (thread count)}
    """
    result = {}
    stats = {}

    for client_id, hints in CLIENT_EMAIL_HINTS.items():
        client_blocks = []
        thread_count = 0

        # Build search query — simple keyword search, no to/cc restriction
        # (to/cc compound was too restrictive and returned 0 results)
        hint_str = " OR ".join(hints)
        query = f"newer_than:{GMAIL_LOOKBACK_DAYS}d ({hint_str})"

        try:
            # Search for messages
            search_result = subprocess.run(
                [GOG_BIN, "gmail", "messages", "search", query,
                 "--max", "10", "--account", GMAIL_ACCOUNT],
                capture_output=True, text=True, timeout=20
            )

            if search_result.returncode != 0:
                err = (search_result.stderr or "").strip()[:100]
                if err:
                    print(f"  ⚠ Gmail: search failed for {client_id}: {err}")
                stats[client_id] = 0
                continue

            output = search_result.stdout.strip()
            if not output:
                stats[client_id] = 0
                continue

            # Parse thread IDs from gog plain-text output
            # Format: ID<ws>THREAD<ws>DATE<ws>FROM<ws>SUBJECT<ws>LABELS
            thread_ids = []
            for line in output.splitlines():
                # Skip header/comment lines
                if line.startswith('#') or line.startswith('ID') or not line.strip():
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    thread_id = parts[1]  # THREAD column
                    if re.match(r'^[0-9a-f]{16,}$', thread_id):
                        thread_ids.append(thread_id)
            # Deduplicate while preserving order
            thread_ids = list(dict.fromkeys(thread_ids))

            for thread_id in thread_ids[:5]:  # cap at 5 threads
                try:
                    thread_result = subprocess.run(
                        [GOG_BIN, "gmail", "thread", "get", thread_id,
                         "--account", GMAIL_ACCOUNT],
                        capture_output=True, text=True, timeout=20
                    )

                    if thread_result.returncode != 0:
                        continue

                    thread_text = thread_result.stdout
                    if not thread_text.strip():
                        continue

                    # Parse messages from thread output
                    # Look for From: and Date: lines and body text
                    msgs_in_thread = re.split(r'\n(?=From:|Message \d+|---)', thread_text)
                    for msg_block in msgs_in_thread[:4]:  # cap at 4 messages per thread
                        from_match  = re.search(r'From:\s*(.+)', msg_block)
                        date_match  = re.search(r'Date:\s*(.+)', msg_block)

                        sender  = from_match.group(1).strip() if from_match else "unknown"
                        date_s  = date_match.group(1).strip() if date_match else ""

                        # Try to clean up date
                        try:
                            from email.utils import parsedate_to_datetime
                            dt = parsedate_to_datetime(date_s)
                            date_s = dt.strftime("%Y-%m-%d")
                        except Exception:
                            pass

                        # Extract body: everything after headers
                        body_match = re.search(r'\n\n(.+)', msg_block, re.DOTALL)
                        body = body_match.group(1).strip() if body_match else msg_block.strip()
                        # Remove quoted text (lines starting with >)
                        body_lines = [l for l in body.split("\n") if not l.startswith(">")]
                        body = "\n".join(body_lines).strip()
                        # Cap body at 500 chars
                        if len(body) > 500:
                            body = body[:497] + "..."

                        if body:
                            block = f"[EMAIL — From: {sender} — {date_s}]\n{body}"
                            client_blocks.append(block)

                    thread_count += 1

                except subprocess.TimeoutExpired:
                    print(f"  ⚠ Gmail: thread fetch timed out for {client_id}/{thread_id}")
                except Exception as e:
                    print(f"  ⚠ Gmail: thread parse error for {client_id}: {str(e)[:80]}")

        except subprocess.TimeoutExpired:
            print(f"  ⚠ Gmail: search timed out for {client_id} — skipping")
            stats[client_id] = 0
            continue
        except FileNotFoundError:
            print(f"  ⚠ Gmail: '{GOG_BIN}' not found in PATH — skipping Gmail source")
            # Don't keep printing this for every client
            for cid in CLIENT_EMAIL_HINTS:
                stats[cid] = 0
            return result, stats
        except Exception as e:
            print(f"  ⚠ Gmail: unexpected error for {client_id}: {str(e)[:100]}")
            stats[client_id] = 0
            continue

        if client_blocks:
            result[client_id] = "\n\n".join(client_blocks)
        stats[client_id] = thread_count

    return result, stats


# ── New Source: Memory ────────────────────────────────────────────────────────

def collect_memory_notes():
    """
    Read today's and yesterday's memory files. Find paragraphs mentioning each client.
    Returns dict: {client_id: formatted_text_block}
    Also returns stats: {client_id: int (paragraph count)}
    """
    result = {}
    stats = {}

    today     = datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    date_files = {}
    for date_str in [today, yesterday]:
        mem_file = MEMORY_DIR / f"{date_str}.md"
        if mem_file.exists():
            try:
                date_files[date_str] = mem_file.read_text()
            except Exception:
                pass

    if not date_files:
        return result, stats

    for client_id, hints in CLIENT_NAME_HINTS.items():
        client_blocks = []
        paragraph_count = 0

        for date_str, content in date_files.items():
            # Split into paragraphs (double newline separated)
            paragraphs = re.split(r'\n{2,}', content)

            for para in paragraphs:
                para = para.strip()
                if not para:
                    continue
                # MUST match a PRIMARY hint (client brand name) — people names alone are not enough
                para_lower = para.lower()
                primary_hints = CLIENT_PRIMARY_HINTS.get(client_id, hints[:1])
                matched = any(hint.lower() in para_lower for hint in primary_hints)
                if not matched:
                    continue
                # EXCLUDE if paragraph also mentions another client's primary name
                # Prevents cross-client contamination in mixed daily notes
                contaminated = any(
                    hint.lower() in para_lower
                    for other_id, other_primary in CLIENT_PRIMARY_HINTS.items()
                    if other_id != client_id
                    for hint in other_primary
                )
                if contaminated:
                    continue  # Too risky — skip mixed paragraphs entirely
                if True:
                    block = f"[MEMORY — {date_str}]\n{para}"
                    client_blocks.append(block)
                    paragraph_count += 1

        if client_blocks:
            result[client_id] = "\n\n".join(client_blocks)
        stats[client_id] = paragraph_count

    return result, stats


# ── New: Collect All Sources ──────────────────────────────────────────────────

def collect_all_sources():
    """
    Gather context from all sources for all clients.
    Returns:
        combined: dict {client_id: combined_context_string}
        stats:    dict {client_id: {"fathom": N, "slack": N, "gmail": N, "memory": N}}
    """
    print("  Collecting sources...")

    # 1. Fathom meeting files
    new_meetings = find_new_meeting_files()
    fathom_data = {}   # {client_id: (text_block, takeaways_list, next_steps_list)}
    for folder_name, filepath in new_meetings:
        client_id = None
        for ops_id, folder in CLIENT_FOLDER_MAP.items():
            if folder == folder_name:
                client_id = ops_id
                break
        if not client_id:
            continue
        content = filepath.read_text()
        ta_text, ns_text, ta_list, ns_list = extract_summary_sections(content)
        if ta_text or ns_text:
            block = ""
            if ta_text:
                block += f"[FATHOM MEETING — {filepath.stem}]\nKey Takeaways:\n{ta_text}"
            if ns_text:
                block += f"\n\nNext Steps:\n{ns_text}"
            fathom_data[client_id] = (block.strip(), ta_list, ns_list)

    print(f"    Fathom: {len(new_meetings)} meeting file(s) found")

    # 2. Slack
    print("    Collecting Slack messages...")
    slack_data, slack_stats = collect_slack_messages()
    total_slack = sum(slack_stats.values())
    print(f"    Slack: {total_slack} signal message(s) across all clients")

    # 3. Gmail
    print("    Collecting Gmail threads...")
    gmail_data, gmail_stats = collect_gmail_threads()
    total_gmail = sum(gmail_stats.values())
    print(f"    Gmail: {total_gmail} thread(s) across all clients")

    # 4. Memory
    print("    Collecting memory notes...")
    memory_data, memory_stats = collect_memory_notes()
    total_memory = sum(memory_stats.values())
    print(f"    Memory: {total_memory} paragraph(s) across all clients")

    # Combine all sources per client
    all_client_ids = set(
        list(fathom_data.keys()) +
        list(slack_data.keys()) +
        list(gmail_data.keys()) +
        list(memory_data.keys())
    )

    combined = {}
    stats = {}

    for client_id in all_client_ids:
        parts = []
        s = {"fathom": 0, "slack": 0, "gmail": 0, "memory": 0}

        if client_id in fathom_data:
            block, _, _ = fathom_data[client_id]
            parts.append(block)
            s["fathom"] = 1

        if client_id in slack_data:
            parts.append(slack_data[client_id])
            s["slack"] = slack_stats.get(client_id, 0)

        if client_id in gmail_data:
            parts.append(gmail_data[client_id])
            s["gmail"] = gmail_stats.get(client_id, 0)

        if client_id in memory_data:
            parts.append(memory_data[client_id])
            s["memory"] = memory_stats.get(client_id, 0)

        if parts:
            combined[client_id] = "\n\n".join(parts)
        stats[client_id] = s

    return combined, stats, fathom_data


# ── LLM Call (v1 — Fathom-only, preserved for fallback reference) ─────────────

SYSTEM_PROMPT = """You are extracting structured data from a meeting summary for a client ops board.
Return ONLY valid JSON — no markdown, no explanation, just the JSON object."""

USER_PROMPT_TEMPLATE = """Meeting summary for client: {client_name}
Date: {date}

Key Takeaways:
{takeaways_text}

Next Steps:
{next_steps_text}

Extract and return this JSON structure:
{{
  "tagline": "1-2 sentence summary of current status. Max 160 chars. Lead with the most important thing.",
  "dot": "green|amber|red|grey",
  "tasks": [
    {{"text": "specific actionable task", "owner": "Michael|DigitsUp|RV|Kieran|Victoria|Client", "complexity": "quick|medium|heavy", "urgent": true, "source": "auto"}}
  ],
  "waitingOn": [
    {{"party": "name", "item": "what we're waiting for", "source": "auto"}}
  ],
  "flags": ["short status bullet", "..."],
  "nextMilestone": "next key date or deliverable"
}}

Rules:
- tasks: only include items explicitly mentioned as next steps or action items. Max 6.
- waitingOn: only include items explicitly waiting on someone else. Max 5.
- flags: mix of ✅ completed items and ⚠️ blockers from the takeaways. Max 5.
- dot: green=on track, amber=needs attention/in progress, red=blocked/urgent problem, grey=waiting on client
- All tasks and waitingOn must have source: "auto"
- If a field has no data, return empty array []"""


def call_claude_haiku(client_name, date_str, takeaways_text, next_steps_text):
    """
    Call Claude Haiku via raw urllib (v1 — Fathom-only). Returns parsed JSON dict or raises on failure.
    Tries CLAUDE_MODELS in order, falls back to next if 404.
    """
    api_key = get_anthropic_key()
    endpoint = "https://api.anthropic.com/v1/messages"

    user_prompt = USER_PROMPT_TEMPLATE.format(
        client_name=client_name,
        date=date_str,
        takeaways_text=takeaways_text or "(none)",
        next_steps_text=next_steps_text or "(none)"
    )

    payload = {
        "system": SYSTEM_PROMPT,
        "messages": [{"role": "user", "content": user_prompt}],
        "max_tokens": 1000
    }

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    last_error = None
    for model in CLAUDE_MODELS:
        payload["model"] = model
        data_bytes = json.dumps(payload).encode("utf-8")

        req = urllib.request.Request(endpoint, data=data_bytes, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read())
                # Extract text content from response
                text = result["content"][0]["text"].strip()
                # Strip markdown code fences if present
                if text.startswith("```"):
                    text = re.sub(r'^```[a-z]*\n?', '', text)
                    text = re.sub(r'\n?```$', '', text)
                parsed = json.loads(text)
                return parsed
        except urllib.error.HTTPError as e:
            if e.code == 404:
                last_error = f"404 for model {model}"
                continue  # Try next model
            body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP {e.code}: {body[:300]}") from e
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Invalid JSON from Claude: {e}") from e

    raise RuntimeError(f"All Claude models failed. Last error: {last_error}")


# ── LLM Call v3 — Combined Context ───────────────────────────────────────────

SYSTEM_PROMPT_V3 = """You are extracting structured status data for a client ops board.
Return ONLY valid JSON — no markdown, no explanation, just the JSON object.
CRITICAL: Extract data ONLY for the specific client named in the prompt. Any information about other clients, brands, or companies mentioned in the source material must be completely ignored."""

USER_PROMPT_V3_TEMPLATE = """You are extracting structured status data for the client ops board.

⚠️ EXTRACTION SCOPE: You are ONLY extracting data for "{client_name}". 
Any mention of other clients, brands, or companies in the source material below must be COMPLETELY IGNORED.
If a task, issue, or update is about a different client, do not include it — even if it appears in a meeting transcript or message thread alongside {client_name} content.

Client: {client_name}
Date: {date}

Combined context from meetings, Slack, email, and session notes:
---
{combined_context}
---

Extract and return this JSON structure:
{{
  "tagline": "1-2 sentence summary of current status for {client_name} ONLY. Max 160 chars. Lead with the most important thing.",
  "dot": "green|amber|red|grey",
  "tasks": [
    {{"text": "specific actionable task for {client_name} only", "owner": "Michael|DigitsUp|Client", "complexity": "quick|medium|heavy", "urgent": true, "source": "auto"}}
  ],
  "waitingOn": [
    {{"party": "name", "item": "what we're waiting for (related to {client_name} only)", "source": "auto"}}
  ],
  "flags": ["short status bullet for {client_name} only", "..."],
  "nextMilestone": "next key date or deliverable for {client_name}"
}}

Rules:
- Only extract facts explicitly stated in the context above AND directly related to {client_name}
- Do not invent or infer tasks not mentioned
- Do not include any data about other clients even if mentioned in the same source
- Prioritize most recent information when there are conflicts
- tasks: max 6, source: "auto"
- waitingOn: max 5, source: "auto"
- flags: max 5, mix of ✅ wins and ⚠️ blockers
- dot: green=on track, amber=needs attention/in progress, red=blocked/urgent, grey=waiting on client
- If a field has no data, return empty array []"""


def call_claude_v3(client_name, date_str, combined_context):
    """
    Call Claude Haiku with combined multi-source context. Returns parsed JSON dict or raises.
    """
    api_key = get_anthropic_key()
    endpoint = "https://api.anthropic.com/v1/messages"

    user_prompt = USER_PROMPT_V3_TEMPLATE.format(
        client_name=client_name,
        date=date_str,
        combined_context=combined_context or "(no context available)"
    )

    payload = {
        "system": SYSTEM_PROMPT_V3,
        "messages": [{"role": "user", "content": user_prompt}],
        "max_tokens": 1000
    }

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    last_error = None
    for model in CLAUDE_MODELS:
        payload["model"] = model
        data_bytes = json.dumps(payload).encode("utf-8")

        req = urllib.request.Request(endpoint, data=data_bytes, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                result = json.loads(resp.read())
                text = result["content"][0]["text"].strip()
                if text.startswith("```"):
                    text = re.sub(r'^```[a-z]*\n?', '', text)
                    text = re.sub(r'\n?```$', '', text)
                parsed = json.loads(text)
                return parsed
        except urllib.error.HTTPError as e:
            if e.code == 404:
                last_error = f"404 for model {model}"
                continue
            body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP {e.code}: {body[:300]}") from e
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Invalid JSON from Claude: {e}") from e

    raise RuntimeError(f"All Claude models failed. Last error: {last_error}")


# ── Merge Logic ───────────────────────────────────────────────────────────────

def merge_client_update(existing_client, llm_output, today):
    """
    Smart merge: manual items preserved, auto items replaced.
    Promises are NEVER touched — manual only.
    """
    # Always replace
    existing_client['tagline'] = llm_output['tagline']
    existing_client['dot'] = llm_output['dot']
    existing_client['nextMilestone'] = llm_output.get('nextMilestone', existing_client.get('nextMilestone', ''))
    existing_client['lastTouched'] = today
    existing_client['autoUpdatedAt'] = datetime.now().astimezone().isoformat()

    # Remove stale autoUpdateError if present
    existing_client.pop('autoUpdateError', None)

    # Tasks: keep manual, replace auto
    manual_tasks = [t for t in existing_client.get('tasks', []) if t.get('source') == 'manual']
    auto_tasks = llm_output.get('tasks', [])  # all have source: "auto"
    existing_client['tasks'] = manual_tasks + auto_tasks

    # WaitingOn: keep manual, replace auto
    manual_waiting = [w for w in existing_client.get('waitingOn', []) if w.get('source') == 'manual']
    auto_waiting = llm_output.get('waitingOn', [])
    existing_client['waitingOn'] = manual_waiting + auto_waiting

    # Flags: replace entirely from LLM
    existing_client['flags'] = llm_output.get('flags', existing_client.get('flags', []))

    # Promises: NEVER touch — manual only
    # (do not modify existing_client['promises'])

    return existing_client


# ── Fallback (v1-style) ───────────────────────────────────────────────────────

def infer_dot_color(takeaways_list):
    """Fallback: infer green/amber/red dot from takeaway text."""
    text = " ".join(takeaways_list).lower()
    red_hits   = sum(1 for s in RED_SIGNALS   if s in text)
    amber_hits = sum(1 for s in AMBER_SIGNALS if s in text)
    green_hits = sum(1 for s in GREEN_SIGNALS if s in text)

    if red_hits > 0 and red_hits >= green_hits:
        return "red"
    if green_hits > amber_hits:
        return "green"
    if amber_hits > 0:
        return "amber"
    return None  # no change


def build_tagline_fallback(takeaways_list, existing_tagline):
    """Fallback: Build tagline from takeaway list. Max 120 chars."""
    if not takeaways_list:
        return existing_tagline
    top = takeaways_list[:2]
    joined = ". ".join(t.rstrip('.') for t in top)
    if len(joined) > 120:
        joined = joined[:117].rsplit(' ', 1)[0] + "..."
    return joined


def apply_fallback(client, takeaways_list, reason, today):
    """Apply v1-style fallback update to a client block."""
    new_dot = infer_dot_color(takeaways_list)
    if new_dot:
        client['dot'] = new_dot
    if takeaways_list:
        client['tagline'] = build_tagline_fallback(takeaways_list, client.get('tagline', ''))
    client['lastTouched'] = today
    client['autoUpdateError'] = f"LLM call failed: {reason}"
    return client


# ── GitHub Push ───────────────────────────────────────────────────────────────

def push_to_github(data):
    """Push ops-data.json to GitHub via Contents API."""
    token = get_gh_token()
    content_bytes = json.dumps(data, indent=2, ensure_ascii=False).encode('utf-8')
    content_b64 = base64.b64encode(content_bytes).decode('utf-8')

    api_url = f"https://api.github.com/repos/{GH_REPO}/contents/{GH_FILE}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json"
    }

    # Get current SHA
    req = urllib.request.Request(api_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            current = json.loads(resp.read())
            sha = current.get('sha')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            sha = None  # File doesn't exist yet
        else:
            raise

    # Push update
    payload = {
        "message": f"ops: auto-update v3 {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "content": content_b64
    }
    if sha:
        payload["sha"] = sha

    data_bytes = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(api_url, data=data_bytes, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        return result.get('content', {}).get('name') == GH_FILE


# ── Source Summary Line ───────────────────────────────────────────────────────

def format_source_summary(client_name, s, llm_success):
    """Format the ✓/⚠ source summary line for a client."""
    parts = []
    if s.get("slack"):
        parts.append(f"Slack ({s['slack']} msg{'s' if s['slack'] != 1 else ''})")
    if s.get("gmail"):
        parts.append(f"Gmail ({s['gmail']} thread{'s' if s['gmail'] != 1 else ''})")
    if s.get("memory"):
        parts.append(f"Memory ({s['memory']} para{'s' if s['memory'] != 1 else ''})")
    if s.get("fathom"):
        parts.append("Fathom (meeting)")

    if not parts:
        return f"  ⚠ {client_name} — no new data from any source"

    sources_str = ", ".join(parts)
    prefix = "  ✓" if llm_success else "  ⚠"
    return f"{prefix} {client_name} — updated from: {sources_str}"


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print(f"Ops Update v3 starting — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if DRY_RUN:
        print("  [DRY RUN — GitHub push disabled]")

    # Load current ops data
    ops = load_ops_data()
    clients_by_id = {c['id']: c for c in ops.get('clients', [])}
    today = datetime.now().strftime('%Y-%m-%d')

    # Collect all sources
    combined_context, source_stats, fathom_data = collect_all_sources()

    if not combined_context:
        print("  No new data from any source in last 25h — ops board timestamp updated")
        ops['meta']['lastUpdated'] = datetime.now().astimezone().isoformat()
        ops['meta']['updatedBy'] = 'Mollie (auto-v3)'
        save_ops_data(ops)
        if not DRY_RUN:
            push_to_github(ops)
            print(f"  ✓ Timestamp updated and pushed")
        else:
            print(f"  ✓ Timestamp updated (push skipped — dry run)")
        print(f"  Board: {OPS_URL}")
        return True

    print(f"  {len(combined_context)} client(s) have new data to process")

    updated_clients = []
    new_activity = []

    for client_id, ctx in combined_context.items():
        if client_id not in clients_by_id:
            print(f"  ⚠ {client_id} — not found in ops-data.json, skipping")
            continue

        client = clients_by_id[client_id]
        client_name = client.get('name', client_id)
        s = source_stats.get(client_id, {})

        # Get fallback takeaways list (from Fathom if available)
        fallback_ta_list = []
        if client_id in fathom_data:
            _, ta_list, _ = fathom_data[client_id]
            fallback_ta_list = ta_list

        # ── LLM path (v3 combined) ─────────────────────────────────────────
        llm_success = False
        try:
            llm_output = call_claude_v3(client_name, today, ctx)
            client = merge_client_update(client, llm_output, today)
            task_count = len(llm_output.get('tasks', []))
            print(format_source_summary(client_name, s, llm_success=True))
            if task_count:
                print(f"    → {task_count} task(s) extracted")
            llm_success = True
        except Exception as e:
            reason = str(e)[:200]
            print(f"  ⚠ {client_name} — LLM v3 failed: {reason}")
            print(f"    Falling back to v1 heuristics...")
            apply_fallback(client, fallback_ta_list, reason, today)
            print(format_source_summary(client_name, s, llm_success=False))

        updated_clients.append(client_name)

        # Activity log entry
        new_activity.append({
            "ts": datetime.now().astimezone().isoformat(),
            "text": f"{client_name} — {client.get('tagline', '')[:100]}"
        })

    # Update activity log (keep last 6)
    if new_activity:
        activity = ops.get('activity', [])
        activity = new_activity + activity
        ops['activity'] = activity[:6]

    # Update meta
    ops['meta']['lastUpdated'] = datetime.now().astimezone().isoformat()
    ops['meta']['updatedBy'] = 'Mollie (auto-v3)'

    # Save locally
    save_ops_data(ops)

    # Push to GitHub (unless dry run)
    if DRY_RUN:
        print(f"  ✓ Saved locally (push skipped — dry run)")
        if updated_clients:
            print(f"  Updated clients: {', '.join(updated_clients)}")
        print(f"  Board: {OPS_URL}")
        return True

    print(f"  Pushing to GitHub...")
    try:
        success = push_to_github(ops)
    except Exception as e:
        print(f"  ✗ GitHub push failed: {e}")
        return False

    if success:
        print(f"  ✓ Pushed successfully")
        if updated_clients:
            print(f"  Updated clients: {', '.join(updated_clients)}")
        print(f"  Board: {OPS_URL}")
        return True
    else:
        print(f"  ✗ Push returned unexpected result")
        return False


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
