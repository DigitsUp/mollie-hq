# Callie Brief — Liverpool Q1 2026 Report: Correction Pass
_Prepared by Mollie · 2026-04-21_

---

## Overview

Five targeted fixes to the Liverpool Q1 2026 HTML report. Surgical edits only — do NOT rebuild or restructure sections you're not touching.

**Source file:** `callie-output/liverpool-q1-2026-final.html`
**Output file:** `callie-output/liverpool-q1-2026-final.html` (overwrite in place)
**Then push to GitHub:** `DigitsUp/liverpool-reports` → `q1-2026/index.html`
**Live URL:** https://digitsup.github.io/liverpool-reports/q1-2026/ · pw: LPSQ1

---

## Fix 1 — §01 Hero Card: Relabel left card as Shopify Total

The large left summary card (class: `summary-cell klaviyo sc-8 hero-metric`) currently shows:
- Tag: "Klaviyo Attributed Revenue"
- Headline: "$1.34M"

This needs to change. The left card must lead with **Shopify Total**, and Klaviyo Attributed moves into the hero-split as the first line item.

**New left card structure:**
- Tag: `Shopify Total Revenue`
- Headline: `$2.4M`
- Blurb: `Total Q1 2026 revenue across all channels — the business context.`

**New hero-split (inside the card, below the blurb):**
1. Label: `Klaviyo Attributed` · Value: `$1.34M` · Change: `↘ −10.4% YoY · 55% of total revenue` (RED/DOWN — this is a decline)
2. Label: `Flows` · Value: `$816K` · Change: `↗ +0.8% YoY` (green/up)
3. Label: `SMS (within attributed)` · Value: `$461K` · Change: `↗ +63% YoY · 34% of attributed` (green/up)

The −10.4% on Klaviyo Attributed MUST use the down arrow class and red/rust color — it is a YoY decline, not a win.

---

## Fix 2 — §02 Performance Overview: Rewrite "bore the brunt" copy

Find this line (around line 704):
> "Flows carried the program; campaigns bore the brunt."

Replace with:
> "Flows held the baseline while campaigns, more exposed to demand contraction, felt more of the market pressure."

---

## Fix 3 — §04 Flows Table: Add missing YoY % on Unique Clicks and Unique Conversions

In the flows metrics table, the Unique Clicks and Unique Conversions rows are missing their YoY deltas. Add them:

| Metric | Email | SMS |
|--------|-------|-----|
| Unique Clicks | 26.6K | 25.6K **(+354.1%)** |
| Unique Conversions | 3,070 | 2,320 **(+67.6%)** |

The Email column Unique Clicks (26.6K) and Email Unique Conversions (3,070) do not have a confirmed prior-year number — do NOT invent a delta. Leave the Email column deltas blank (—) if not already present. Only add the confirmed SMS deltas as shown above.

---

## Fix 4 — §08 Q2 Priorities: Add Shelbie's 10-Flow Roadmap

In the §08 section, after the existing 4 Q2 priority cards, add a new subsection titled **"Q2 Flow Roadmap"** with the following 10 flows Shelbie has queued. Style it as a clean list or simple grid — match the existing report aesthetic (cream/denim palette, same typography).

**Header:** `Q2 Flow Roadmap · 10 flows in motion`

**The 10 flows:**
1. Loyalty Expiry Points
2. Loyalty Expiry Tier
3. Loyalty Anniversary
4. Loyalty Review Add-on
5. Loyalty Redemption Reminder
6. Sunset
7. Wallet Pass
8. One-Hit Wonder
9. Email Pause
10. Return Winback ← _tied to returns +37% YoY_

**Intro copy (above the list):**
"The Q2 build is already in motion. Ten flows are queued — led by a full loyalty lifecycle suite and three behavioral flows designed to protect margin and reduce churn."

---

## Hard Rules

- Do NOT rebuild from scratch. Surgical edits only.
- Do NOT send any emails.
- Do NOT spawn sub-agents.
- Do NOT push to GitHub until the full file is saved.
- Output: `callie-output/liverpool-q1-2026-final.html` — overwrite in place.
- Report back with: live URL, password confirmation, and a bullet list of every change made.
