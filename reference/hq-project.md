# Mollie HQ — Project Reference
_Read this before touching anything HQ-related. No exceptions._

---

## The 4 Pages

### 1. HQ (updated frequently)
Main operational view. Reflects what's happening right now across clients, inbox, calendar, and what needs attention. Update whenever significant things change — new deliverable, client status shift, new open item.

### 2. Workspace (vanity only — update by request)
3D animated scene with Mollie + Callie at desks. Cat, neon sign, vinyl player, corkboard, etc. Michael requests changes to this when he wants something added to the scene. Nothing here affects operations. Do not touch unless asked.

### 3. Pipeline (updated frequently)
Kanban-style board showing all active production and sales work. Each card has a client, column, owner, comms flag, and notes. Update whenever work moves, a new project starts, or something is closed.

### 4. Usage (updated Sundays or Mondays — manual input from Michael)
Shows monthly spend, daily cost chart, model, budget %. Michael provides the numbers. Do not guess or fabricate usage data. Wait for Michael to give you the figures.

---

## File Structure (do not change these paths)

```
workspace/
├── index.html              ← THE LIVE HQ. NEVER TOUCH THIS FILE.
├── data.json               ← Root copy. Always sync from mollie-hq/data.json.
├── mollie-hq/
│   ├── data.json           ← SOURCE OF TRUTH for HQ data. Edit this.
│   └── pipeline.html       ← Pipeline iframe page. DO NOT DELETE.
└── pipeline-data.json      ← Pipeline board data. Edit this for pipeline updates.
```

---

## "Update HQ" — Exact Steps Every Time

1. Edit `workspace/mollie-hq/data.json`
2. Run: `cp workspace/mollie-hq/data.json workspace/data.json`
3. Run: `git add data.json mollie-hq/data.json && git commit -m "HQ data update: [date] — [what changed]" && git push`
4. Wait 2 min. Validate: `curl -s "https://digitsup.github.io/mollie-hq/mollie-hq/data.json?v=$(date +%s)" | python3 -c "import sys,json; d=json.load(sys.stdin); print('OK:', d['meta']['lastUpdated'])"`
5. Confirm timestamp matches. Only then tell Michael it's live.

## "Update Pipeline" — Exact Steps Every Time

1. Edit `workspace/pipeline-data.json`
2. Run: `git add pipeline-data.json && git commit -m "Pipeline update: [date] — [what changed]" && git push`
3. Tell Michael it's updated.

---

## data.json — Full Schema (HQ tab)

```json
{
  "meta": {
    "lastUpdated": "2026-04-22T11:30:00-07:00",
    "updatedBy": "Mollie"
  },
  "needsYou": [
    { "text": "What needs Michael's attention", "chip": "Action|Deadline|Decision|FYI" }
  ],
  "watching": [
    { "dot": "green|yellow|amber|blue|grey|red", "text": "Client — what we're watching" }
  ],
  "clients": [
    {
      "name": "Client Name",
      "lastActivity": "One line status — what's happening",
      "dot": "green|amber|grey",
      "status": "active|prospect|watching"
    }
  ],
  "calendar": [
    { "time": "9:30 AM", "title": "Meeting title" }
  ],
  "inbox": {
    "summary": "One line inbox summary shown in the tile",
    "lastChecked": "2026-04-22T08:30:00-07:00"
  },
  "usage": {
    "monthLabel": "April 2026",
    "mtd": 419.19,
    "budget": 1000,
    "today": 0,
    "todayLabel": "Apr 22",
    "model": "Sonnet 4.6",
    "dailyCosts": [
      { "label": "Apr 13", "amount": 32.29 }
    ],
    "dailyNote": "Note about the data"
  }
}
```

**Critical field names — the HTML uses these exactly:**
- `needsYou` (NOT `reminders`)
- `watching[].text` (NOT `watching[].item`)
- `clients` (NOT `pulse`)
- `clients[].name` (NOT `clients[].client`)
- `clients[].lastActivity` (NOT `clients[].status`)
- `clients[].status` = `active|prospect|watching` — used for chip styling only
- `clients[].dot` = `green|amber|grey` — coloured dot

---

## pipeline-data.json — Full Schema

```json
{
  "lastUpdated": "2026-04-22T11:26:00-07:00",
  "cards": [
    {
      "id": "unique-id",
      "title": "Card Title",
      "client": "Client Name",
      "section": "sales|production",
      "column": "outreach|proposal-sent|negotiating|onboarding|strategy|copy|design|review|done|parking-lot",
      "owner": "Michael|Mollie|Callie|Kieran|Marl|Team|Client",
      "dueDate": "2026-04-27",
      "commsFlag": "none|action-needed|waiting-on-them|reply-needed|blocked",
      "notes": "Context notes for this card"
    }
  ]
}
```

---

## Never Do These Things

- **Never overwrite `index.html`** — it is the live HQ. It was correct as of commit `a2b2440`. If it breaks, revert to that commit.
- **Never delete `mollie-hq/pipeline.html`** — the Pipeline tab iframes it.
- **Never update only one `data.json`** — always copy mollie-hq/data.json to root after editing.
- **Never guess usage numbers** — wait for Michael.
- **Never report "done" without running the validation curl in step 4 above.**
- **Never touch the Workspace tab** unless Michael explicitly asks.

---

## Current Active Clients (as of Apr 22 2026)
- Liverpool LA — active
- RVCA — active
- Riversol — active
- Brand Featured — new, start Apr 27
- Hiba Academy — active
- Axis Health — active
- SFR Distillery — prospect (proposal out)
- Stand Flagpoles — CLOSED

---

## Repo
- GitHub: DigitsUp/mollie-hq
- Live URL: https://digitsup.github.io/mollie-hq/
- Password: Digi420
