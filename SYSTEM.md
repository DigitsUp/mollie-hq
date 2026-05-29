# SYSTEM.md — System State
_Read this before answering any system question. Last updated: 2026-05-26_

---

## Active Crons

| ID (short) | Name | Schedule | Purpose | Last Status |
|---|---|---|---|---|
| b060cf31 | Inbox Monitor | 7am, 12pm, 5pm · M–F | Gmail scan, GCal, Reminders, NOW.md, callie-output check. 7am reads yesterday's reflection + preflight. Sends Telegram. Fathom emails marked read only — filing handled by Fathom Transcript Sync. | ✅ ok |
| f7a3c921 | Fathom Transcript Sync | 6am, 11am, 4pm · daily | Pulls meetings + full transcripts from Fathom API. Files to clients/[name]/meetings/. Deduplicates via memory/fathom-processed.json. Silent unless error. | ✅ new 2026-05-28 |
| b37f5d09 | Nightly Reflection | 11pm · daily | Reads today's memory, writes reflection to memory/reflection-YYYY-MM-DD.md, sends full text to Telegram. Friday adds Week in Review. | ✅ ok |
| 6049f5c9 | Daily Preflight | 5am · daily | Runs scripts/preflight.py, writes preflight-YYYY-MM-DD.md. Alerts Telegram only on failure. Silent if healthy. | ✅ ok |
| 39c5b86f | Daily Disk Space Check | 7am · daily | Checks root volume free space. Alerts if <20GB. Silent otherwise. | ✅ ok |
| 8a3b8338 | Saturday Check-In | 12pm · Saturday | Gmail, GCal, Reminders, NOW.md scan. Sends Telegram if anything needs attention. | ✅ idle (runs Sat) |
| 6e993c5a | Sunday Wind-Down | 5pm · Sunday | Gmail, GCal, Reminders, NOW.md, client pulse. Sends Telegram. Then updates + pushes mollie-hq/data.json to GitHub Pages. | ✅ ok |

---

## Known Issues / Watch Items

- **Inbox Monitor — noon hallucination (May 26):** Noon run completed in 8.5 seconds. Model ran `ls` in a wrong directory (Python library repo), hit an `ls -T` flag error, and bailed immediately. Output: garbage repo listing. Confirmed one-off — all other noon runs May 19–25 ran 118–227 seconds and delivered correctly. Timeout already increased to 270s, failure alert enabled. Do NOT change the prompt unless it recurs. Monitor next 3 noon runs.
- **Sunday Wind-Down HQ push:** Updates meta.lastUpdated and activity entries only. Does NOT update client statuses — those are always manual. Client list drift is expected between Sunday runs.

---

## System Fixes Applied

| Date | What Broke | Fix Applied |
|---|---|---|
| 2026-05-24 | gateway.err.log growing unbounded, eating disk | Redirected stderr to /dev/null in launchd plist. Permanent fix. |
| 2026-05-24 | Doctor --fix: 14 orphan transcript files | Archived. No errors, no security flags. |
| 2026-05-26 | Inbox Monitor timeout too short, failure alerts off | Timeout increased to 270s. Failure alert enabled (Telegram after 1 error). |
| 2026-05-26 | Log rotation cron added then removed | Michael: bandaid ≠ fix. Correct call. Removed. |

---

## Fathom Integration — IMPORTANT (updated 2026-05-28)
**Method changed from email-parsing to direct API.** Do not revert to email-based filing.

- API base: `https://api.fathom.ai/external/v1`
- Auth header: `X-Api-Key` (key at `~/.config/fathom/api_key`)
- Endpoints used: `GET /meetings`, `GET /recordings/{id}/transcript`, `GET /recordings/{id}/summary`
- Script: `workspace/scripts/fathom_sync.py`
- Dedup: `memory/fathom-processed.json` (stores processed recording IDs)
- Routing: title + attendee email matching → `clients/[folder]/meetings/`. Unknown → `clients/unknown/meetings/`
- Standing ignores: meetings where only external attendee is David (davidcwoodward@gmail.com)
- Inbox Monitor Step A now ONLY marks Fathom emails as read — does NOT file them
- Fathom Transcript Sync (cron f7a3c921) handles all filing, runs 1hr before Inbox Monitor

## Voice Note Transcription — STANDING RULE (added 2026-05-28)
**Always use local Whisper. Never call OpenAI API for audio transcription.**

- Local Whisper is installed: `python3 -c "import whisper; m = whisper.load_model('base'); result = m.transcribe('/path/to/audio.ogg'); print(result['text'])"`
- Use model `base` by default (fast, accurate enough)
- Do NOT use the openai-whisper-api skill or any OpenAI API endpoint for audio
- If local Whisper fails for any reason, tell Michael and ask him to type it out — do not fall back to OpenAI API

## Pending System Work

- **OpenClaw update to 2026.5.22** — ON HOLD until after June 4 (Salehe deadline). Do not update until Michael gives the go-ahead.
- **Inbox Monitor noon prompt** — possible tightening needed if hallucination recurs. Flag to Michael before touching.
- **Sunday Wind-Down client status** — could be enhanced to pull current client statuses from SESSION.md and write to data.json automatically. Not approved — discuss with Michael first.
- **Per-client AM agent system** — high priority, scoped, not started. Full plan in memory/2026-05-22.md + SESSION.md.
- **Morning pre-meeting brief cron** — 8am pull of calendar + client context → Telegram brief. Not approved yet.
