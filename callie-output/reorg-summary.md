# Architecture Reorg Summary
_Completed: 2026-04-02 by Callie_

---

## What Was Created

### New Client Context Files (9 files)
- `clients/liverpool/context.md` — contacts, Klaviyo IDs, report format, file locations
- `clients/riversol/context.md` — contacts, Klaviyo IDs, all campaign ideas + sales strategies, pending items
- `clients/rho-nutrition/context.md` — 18-email flow structure, pipeline status, file locations
- `clients/hiba/context.md` — contacts, Klaviyo IDs, March 2026 data, report sections
- `clients/rvca/context.md` — kickoff status, contact, strategy doc locations
- `clients/stand-flagpoles/context.md` — scope, ownership, cadence requirements
- `clients/axis-health/context.md` — scope (strategy only, no build), pending item
- `clients/brand-featured/context.md` — prospect status, proposal note
- `clients/sfr-distillery/context.md` — prospect, contact, call date, referral source

### NOW.md (new)
- `NOW.md` — Active Queue (7 items), Watching For (5 items), Hot Context, Integrations table, Client Context Files index

---

## What Was Changed

### MEMORY.md
- **Before:** 193 lines
- **After:** 94 lines
- **Reduction:** -99 lines (-51%)
- **What was removed:** All client detail (moved to client context files), verbose session history/lessons (in daily notes), growth strategy detail, architecture cleanup plan (now executed), completed-task logs

### TOOLS.md
- Appended `## Integration Runbooks` section covering: Preflight script, Gmail, GCal, Notion, Slack, Klaviyo (all 3), GitHub, Figma, Fathom

---

## Judgment Calls

1. **Riversol sales strategies** — These were in the Apr 1 daily note as "still to do — not yet in HTML doc." I preserved them fully in `clients/riversol/context.md` with a clear pending flag. They're documented, not lost.

2. **Hiba context.md vs hiba-academy/** — Existing folder is `clients/hiba-academy/` (with notion-context.md and strategy HTML). I created `clients/hiba/context.md` (matching the task spec). Both exist — they serve different purposes (the new one is the operational brief, the old folder has strategy assets). No conflict, no deletion.

3. **MEMORY.md Active Queue** — Replaced verbose list with pointer to NOW.md, per spec. The actual items live in NOW.md now.

4. **Growth Strategy section** — This was in MEMORY.md (LinkedIn, Retention Report, digital products, YouTube). Removed from MEMORY.md as it was aspirational/deferred content, not operational data. It remains in daily notes (`memory/2026-03-30` or similar). If Michael wants to action it, it needs a dedicated file.

5. **Figma runbook** — Added to TOOLS.md even though it's read-only. Documented the read-only constraint explicitly so no one wastes time trying to write via API.

6. **Fathom** — Included in Integration Runbooks for completeness even though API doesn't return summaries. The workaround (email summaries to mollie@) is documented.

---

## Anything I Was Unsure About

- **Growth Strategy** — The LinkedIn/Retention Report/digital products plan was in MEMORY.md but had no active queue item. I removed it from MEMORY.md (it's still in daily notes). Recommend Michael or Mollie create a `growth/strategy.md` file if this is being actively planned.

- **Slack token paths** — MEMORY.md only said "not yet set up" originally, but Apr 2 notes say "Bot connected, mention-only mode." I wrote the runbook assuming standard Slack token paths (`~/.config/slack/bot_token`, `~/.config/slack/app_token`). Mollie should verify actual paths match.

- **Stand Flagpoles Klaviyo** — No API key exists yet. Left a note to check with Michael. If they connect, add the path and account ID to both this file and TOOLS.md runbooks.

---

## Git Checkpoints
1. `pre-architecture-reorg checkpoint` — before any changes
2. `architecture reorg: lean MEMORY.md, NOW.md, client context files, integration runbooks` — all changes committed
