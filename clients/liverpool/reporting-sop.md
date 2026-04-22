# Liverpool LA — Reporting SOP

_Last updated: 2026-04-19_

---

## Two Report Types

| Type | Cadence | Due | Format |
|---|---|---|---|
| Weekly | Every week | Before Tue 11:30am call | HTML (password gated) |
| Quarterly | Q1/Q2/Q3/Q4 | Before first weekly call of new quarter | HTML (password gated) |

Password: `Liverpool2026`

---

## Who Does What

- **Michael:** Pulls data from Klaviyo Business Review → exports as PDF or PPTX → sends to Mollie
- **Mollie:** Reads the file, extracts all data, writes commentary and insights, confirms with Michael
- **Callie:** Builds the HTML report once Michael approves the brief
- **Mollie → Michael:** Delivers the link, no client contact

---

## Step-by-Step: Quarterly Report

### Step 1 — Michael Pulls the Data
Pull from Klaviyo → Analytics → Business Review. Set date range to the full quarter (e.g. Jan 1 – Mar 31).

**Screenshots to capture (these become the slides):**
1. Q1 Overview — Total revenue, attributed revenue, campaign vs flow split, email vs SMS split, monthly YoY breakdown (Jan / Feb / Mar)
2. Campaign Review — Total recipients, conversion value, full metric table (email + SMS)
3. Flow Review — Total recipients, conversion value, full metric table (email + SMS)
4. Top 5 — Top 5 campaigns and top 5 flows for current year vs prior year
5. Q1 YoY Dashboard — Full top-performing flows list

Export as PDF or PPTX and send to Mollie via Telegram.

**Note:** Include the prior year (same quarter) in the same pull so YoY is visible. The Business Review tool handles this automatically.

---

### Step 2 — Mollie Reads the File
Mollie converts the PDF to images and reads every slide to extract all data points. If anything is unclear or missing, Mollie asks one specific question before proceeding.

Mollie does NOT pull data independently from the Klaviyo API to replace Michael's data. API may be used to validate or dig deeper on specific items only.

---

### Step 3 — Mollie Writes Commentary
Using Michael's data as the source of truth, Mollie drafts commentary for each section:

**For each section (Campaigns / Flows / Overview):**
- What's Working — genuine wins, specific numbers
- Needs Attention — real gaps or declines, with context
- Opportunities — actionable next steps tied to the data

Mollie shares the commentary with Michael for review BEFORE briefing Callie.

---

### Step 4 — Michael Approves
Michael reviews the commentary draft. One of:
- "Looks good, build it" → Mollie briefs Callie
- "Change X" → Mollie revises, asks again

**No build starts without an explicit "go" or "build it."**

---

### Step 5 — Callie Builds the HTML
Mollie writes a tight brief for Callie including:
- All data (exact numbers from Michael's pull)
- All commentary (approved text, verbatim)
- Template reference (Riversol Q1 hub at `workspace/mollie-hq/projects/riversol/riversol-q1-hub.html`)
- Output path: `workspace/callie-output/liverpool-q1-[year]-report.html`
- Password gate, design specs

Callie builds in one pass. No iteration without Michael seeing the file first.

---

### Step 6 — Review and Publish
Mollie picks up the file from `callie-output/`, checks it looks right, then:
1. Copies to `workspace/projects/liverpool/reports/`
2. Pushes to GitHub → `DigitsUp/mollie-hq` → `clients/liverpool/`
3. Sends Michael the live URL

**Always ask Michael before pushing to GitHub.**

---

## Step-by-Step: Weekly Report

Same process, smaller scope:

**Michael provides (or Mollie pulls via API for weekly):**
- This week vs last week vs same week last year
- Top campaigns and flows for the week
- Any notable context (sale, launch, promo)

**Sections:**
- S1: Revenue summary (attributed, campaign, flow — WoW + YoY)
- S2: Top campaigns this week vs same week LY
- S3: Top flows this week vs last week
- S4: 30-day rolling YoY
- Commentary

For weeklies, Mollie can pull the Klaviyo data directly via API (email only — note SMS not included in API pull). If Michael wants SMS included, he pulls from Business Review.

---

## Metrics We Report (Liverpool Standard)

**Always use unique numbers, not rates as the headline.**

| Metric | Label |
|---|---|
| Total Recipients / Deliveries | Sends |
| Unique Opens | Opens |
| Unique Clicks | Clicks |
| Unique Conversions (Placed Order) | Conversions |
| Conversion Value | Revenue |
| Average Order Value | AOV |

Rates (open rate, click rate, conversion rate) go in the data table as secondary context — not the headline story.

---

## Files and Locations

| File | Location |
|---|---|
| Weekly reports | `workspace/projects/liverpool/reports/` |
| Quarterly reports | `workspace/projects/liverpool/reports/` |
| Client context | `workspace/clients/liverpool/context.md` |
| This SOP | `workspace/clients/liverpool/reporting-sop.md` |
| Live URL base | `https://digitsup.github.io/mollie-hq/clients/liverpool/` |
| Report template | `workspace/mollie-hq/projects/riversol/riversol-q1-hub.html` |
| Raw data saves | `workspace/projects/liverpool/` |

---

## Key Lessons Learned (2026-04-19)

- **Michael's Business Review pull is the source of truth** — it includes SMS which the API does not. Always start from his data.
- **PDF screenshots are readable** via PyMuPDF image conversion — standard workflow now.
- **Never spawn Callie without explicit approval** — "go" or "build it" required. No exceptions.
- **Commentary first, build second** — don't brief Callie until Michael has approved the commentary draft.
