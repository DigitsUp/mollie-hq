# MEMORY.md - Long-Term Memory Index
_Client detail → `clients/[name]/context.md`. Daily notes → `memory/YYYY-MM-DD.md`. Active queue → `NOW.md`. Current handoff → `SESSION.md`. Team → `reference/team-roster.md`._

---

## Michael
- Michael Grill · mike@digitsup.com · Langford, BC · travels frequently
- Runs DigitsUp — retention marketing agency, US operations (New York)
- Direct, no fluff. Bullets over paragraphs. Proactive suggestions welcome.
- Primary channel: Telegram

## Mollie
- Online since 2026-03-29 · mollie@digitsup.com · 🦾
- DigitsUp AI assistant — coordinator, not builder. Callie handles builds.

## Budget
- Monthly: $500. Soft alert $200, hard limit $400.
- Heavy builds → subagents. Long sessions → summarize + fresh session.

## Non-Negotiable Rules
- Email to mike@digitsup.com → send directly.
- Email to anyone else → show draft, get approval, then send.
- **CC mike@digitsup.com on every email sent to anyone else. No exceptions. Ever.**
- Callie → never spawn without explicit "go" or "build it." (Broken 2026-04-19.)

## Callie
- Agent ID: callie · Workspace: `~/.openclaw/workspace-callie/`
- Handoff: `workspace/callie-output/` · Spawn: `sessions_spawn agentId="callie"`

## HQ Dashboard — Full runbook: `reference/hq-project.md` — READ IT BEFORE ANY HQ WORK.
## HQ Dashboard — RUNBOOK SUMMARY (follow exactly every time)
- Live: https://digitsup.github.io/mollie-hq/ · Password: Digi420
- Repo: DigitsUp/mollie-hq
- Correct version: HQ | Workspace | Pipeline | Usage (4 tabs). Git baseline: a2b2440.

### "Update HQ" = these 4 steps, nothing else:
1. Edit `workspace/mollie-hq/data.json`
2. Run: `cp workspace/mollie-hq/data.json workspace/data.json`
3. Run: `git add data.json mollie-hq/data.json && git commit -m "HQ data update" && git push`
4. Wait 2 min. Run: `curl -s https://digitsup.github.io/mollie-hq/mollie-hq/data.json | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK:', d['meta']['lastUpdated'])"` — confirm timestamp matches. Only then tell Michael it's live.

### NEVER:
- Touch `index.html` — ever. It is the live HQ. Do not copy, overwrite, or modify it.
- Touch `mollie-hq/pipeline.html` — leave it alone.
- Report "done" without running the validation in step 4.

## Standing Ignores
- Fathom meeting recording requests from David — always ignore, never action.

## Integrations
_Paths + runbooks → TOOLS.md and `reference/integration-runbooks.md`_
Gmail · GCal · Notion · Slack · Klaviyo (Liverpool JeMYJL · Riversol TMwKL4 · Hiba TrGDfH) · GitHub (Org: DigitsUp) · Figma (read-only) · Fathom

## Active Clients
- Liverpool LA — `clients/liverpool/context.md`
- Riversol — `clients/riversol/context.md`
- Rho Nutrition — `clients/rho-nutrition/context.md`
- Hiba Academy — `clients/hiba/context.md`
- RVCA — `clients/rvca/context.md`
- Stand Flagpoles — `clients/stand-flagpoles/context.md`
- Axis Health — `clients/axis-health/context.md`
- Brand Featured (prospect) — `clients/brand-featured/context.md`
- SFR Distillery (prospect) — `clients/sfr-distillery/context.md`

## Inactive / Past Clients
- TMM — offboarded, inactive
- OBG — done, bad experience, ignore
- Mother Nature's Cleaning — inactive, check UTM report end of April 2026
- Hale Iwa Farm — friend project (Billy Busch), not formal
