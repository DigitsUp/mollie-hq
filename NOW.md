# NOW.md — Session Handoff
_Last updated: 2026-04-02 (end of day)_

---

## Active Queue

1. **Rho Nutrition — Days 8 + 21 briefs + copy** — Day 3 done and sent. Waiting on Shelbie approval before moving forward. On approval: build wireframe briefs for Marl (18 total). → Load `clients/rho-nutrition/context.md`
2. **Riversol campaign-ideas.html** — Add Sales Strategies section (all 11 plays documented in `clients/riversol/context.md`), then deploy to GitHub. → Load `clients/riversol/context.md`
3. **SFR Distillery intro call prep** — Call is Apr 7. Pre-call brief needed. → Load `clients/sfr-distillery/context.md`
4. **Hiba report — 3 pending fixes** — Teaser #1 fix, Jan note update, Ravenna section rewrite. Callie job was queued but not confirmed complete at Apr 2 session close. Check `callie-output/hiba-march-2026-report.html`.
5. **Axis Health post-purchase flow** — Tabled. Needs client context briefing first before starting.
6. **Mollie HQ dashboard — add Callie visually** — Still pending from Apr 1 queue.
7. **Notion invite from Debbie** — Accept or check with Michael? (mollie@digitsup.com invited to DigitsUp Notion workspace)

---

## Watching For

- **Arnaud Bussieres (Riversol)** — Replied to Michael's 4 questions about SPF 50 campaign. mollie@digitsup.com CC'd — watch inbox.
- **Ali (Riversol)** — Tier threshold confirmation (Bronze→Silver $300-399, Silver→Gold $600-749 — USD vs CAD unclear)
- **Shelbie Jarvis** — Rho Nutrition brief/copy review. Mollie should watch for reply and move forward automatically (flag to Michael, then proceed).
- **Brand Featured** — Waiting to hear if proposal is a go. No action until Michael confirms signed.
- **Mike OOO** — Friday Apr 3. Back Apr 7 (SFR call day).

---

## Hot Context

- **RVCA** — Kickoff done Apr 1. Onboarding phase. Follow Liverpool model: build automations first, then layer in campaign management. Contact: Clayton Dahl.
- **Outersignal/Rho pipeline confirmed:** Mike approves → Shelbie reviews briefs → Meaghan reviews copy → Marl designs. Callie handles builds. Mollie routes.
- **Client repo structure:** Each client gets own GitHub repo under DigitsUp org. Pattern: `digitsup.github.io/[client]/`. Live repos: riversol, hiba, mollie-hq.
- **Callie delegation is live** — sessions_spawn with agentId="callie" confirmed working. All heavy builds go to Callie. Handoff folder: `workspace/callie-output/`.
- **Token budget:** $59.23 spent / ~12% of $500 monthly. ($200 soft alert, $400 hard limit). Keep heavy builds in subagents.
- **Crons active:** Morning briefing 6am (job: 5b2b9a90), EOD recap 5pm (job: 54ba666d). Both deliver to Telegram 8745174447.

---

## Integrations

| Integration | Status | Notes |
|---|---|---|
| Gmail (mollie@digitsup.com) | ✅ Connected | Token: `~/.config/gmail/mollie_token.json` |
| Google Calendar (mike@digitsup.com) | ✅ Connected (read-only) | Token: `~/.config/gcal/mike_token.json` |
| Notion | ✅ Connected | Key: `~/.config/notion/api_key` |
| Slack | ✅ Bot connected (mention-only mode) | Tokens in `~/.config/slack/` |
| Klaviyo — Liverpool | ✅ Connected | Key: `~/.config/klaviyo/liverpool/api_key` · Account: JeMYJL |
| Klaviyo — Riversol | ✅ Connected | Key: `~/.config/klaviyo/riversol/api_key` · Account: TMwKL4 |
| Klaviyo — Hiba | ✅ Connected | Key: `~/.config/klaviyo/hiba/api_key` · Account: TrGDfH |
| Fathom | ✅ Connected | Key: `~/.config/fathom/api_key` · Webhook: `~/.config/fathom/webhook_secret` |
| GitHub | ✅ Connected | Token: `~/.config/github/token` · Org: DigitsUp |
| Figma | ✅ Connected (read-only) | Token: `~/.config/figma/token` · Team: 1278952831789382683 |

**Preflight script:** `workspace/scripts/preflight.py` — run to validate all integrations before a session.

---

## Client Context Files

Load these just-in-time (don't pre-load all):

- `clients/liverpool/context.md`
- `clients/riversol/context.md`
- `clients/rho-nutrition/context.md`
- `clients/hiba/context.md`
- `clients/rvca/context.md`
- `clients/stand-flagpoles/context.md`
- `clients/axis-health/context.md`
- `clients/brand-featured/context.md`
- `clients/sfr-distillery/context.md`
