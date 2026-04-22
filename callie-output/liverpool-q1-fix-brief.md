# Callie Brief — Liverpool Q1 2026 Report: Fix Pass
_Prepared by Mollie · 2026-04-19_

## Source File
`/Users/minigrill/.openclaw/workspace-callie/callie-output/liverpool-q1-2026-final.html`

Make these three targeted changes only. Do not touch anything else.

---

## Change 1 — §05 Top 5: Added2Cart callout

In the 2025 top flows comparison, Added2Cart currently appears in "What's working."

**Move it to "Needs attention"** and reframe the copy to:

> **Added to Cart YoY decline** — 2025 ran two flows (Added2Cart 2024 + Added2Cart 2025) combining for $150.8K. 2026 consolidated to one flow at $112K — a real decline of ~$38.8K (−26%) year over year. Not a regression in the flow itself, but the combined baseline makes this a genuine watch item heading into Q2.

Remove it from "What's working" entirely.

---

## Change 2 — §06 Business Context: Remove returns callout

Find the callout block that highlights returns +37% (the orange/amber "!" warning block that says "Returns the watch item" / "Returns climbed +37% YoY to $430K"). Remove it entirely — the surrounding data table (gross/net/discounts/returns/shipping) can stay, just remove the standalone callout card/block.

---

## Change 3 — Hero image: Shift background position to right

The hero background image currently has the two women centred, causing their heads to be cropped. Change the `background-position` on the `.cover-bg` element (or wherever the hero background image is set) from `center` or `center center` to `right center`.

This will anchor the women to the right side of the hero, keeping their full bodies visible, while the text sits naturally over the darker left portion of the image.

---

## Deployment
- Overwrite `callie-output/liverpool-q1-2026-final.html` with the updated file
- Push to GitHub: `DigitsUp/liverpool-reports` → `q1-2026/index.html`
- Confirm live URL and that all three changes are in place
