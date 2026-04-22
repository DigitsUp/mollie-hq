# Callie Brief — Liverpool LA Q1 2026 Report
_Prepared by Mollie · 2026-04-19_

## Task
Take the existing Liverpool Q1 2026 HTML report, add a new **§07 List Health** section (audience growth/churn data), renumber the existing §07 Summary to **§08**, add password protection with `LPSQ1`, and push to GitHub Pages.

---

## Source File
`/Users/minigrill/.openclaw/media/inbound/LPS_Q1_2026_Review---cdf1c556-d12b-42b7-9b94-094c2f15d755`

This is a complete, fully styled HTML file. Use it as the base — do not rebuild from scratch.

---

## Section Renumbering
- §01–§06 — unchanged
- **§07 — NEW: Audience & List Health** (insert before existing §07)
- **§08 — Q1 in Summary & Q2 Priorities** (was §07, renumber only)

Update the nav links to match. The nav currently has: Overview, Campaigns, Flows, Top 5, Summary — add **List Health** between Top 5 and Summary.

---

## §07 — Audience & List Health (NEW SECTION)

### Section Header
- Eyebrow: `§ 07`
- H2: `Audience &` / `list health`
- Intro copy: `The list grew on both channels, but email churn ran ahead of acquisition in Q1. SMS is the brighter story — churn is actively improving month over month.`

### Email Subscriber Data

**Q1 2026 — Email**
| Month | New Subscribers | Unsubscribes |
|-------|----------------|--------------|
| January | 4,091 | 7,996 |
| February | 4,369 | 7,795 |
| March | 5,564 | 8,523 |
| **Q1 Total** | **14,024** | **24,314** |

- Net email change Q1: **−10,290**
- Bounce suppressions added Q1: **2,399**
- March note: highest unsubscribes (8,523) — correlates with heaviest campaign send volume. Worth monitoring ratio as volume scales.
- Positive signal: new subscriber acquisition is trending up (4,091 → 4,369 → 5,564)

**What's working:** Acquisition momentum building into Q2.
**Needs attention:** Unsubscribes running ~1.7× acquisition rate — list is contracting. Tighter segmentation and frequency management are the levers.

---

### SMS Subscriber Data

**Q1 2026 — SMS**
| Month | New Subscribers | Unsubscribes |
|-------|----------------|--------------|
| January | 2,389 | 4,215 |
| February | 2,390 | 2,685 |
| March | 3,057 | 2,658 |
| **Q1 Total** | **7,836** | **9,558** |

- Net SMS change Q1: **−1,722**
- Key signal: SMS churn dropped from 4,215 in January to 2,658 in March — **churn nearly halved** over the quarter.
- March is the first month where churn is close to matching acquisition pace.

**What's working:** SMS churn curve is reversing — the list is stabilising.
**Needs attention:** Net negative for the quarter, but trajectory is the story here — March is a near-breakeven month.

---

### Design Direction
Match the existing section style — same card/stat layout as §06 Business Context. Use:
- The existing CSS variables (--denim, --sage, --rust, --gold, --cream, etc.)
- Two side-by-side cards: Email and SMS
- Monthly breakdown table styled like the campaigns table (§03)
- "What's working / Needs attention" callout blocks — same format as other sections
- Stat highlights: Net −10,290 email (--rust), SMS churn nearly halved (--sage)
- Section background: `var(--paper)` (alternate from adjacent sections)
- Section ID: `id="listhealth"` for nav anchor

---

## Password Protection
Gate the entire page with password `LPSQ1`.

Use a full-page overlay approach (same style/feel as the existing report design):
- Overlay covers everything on load
- Password field + submit button, styled to match the report aesthetic (cream/denim palette)
- On correct password: overlay fades out, page becomes visible
- Store in `sessionStorage` so refresh doesn't re-prompt
- Wrong password: shake animation + error message

---

## GitHub Deployment
- **Repo:** `DigitsUp/liverpool-reports` (create if it doesn't exist)
- **File:** `q1-2026/index.html`
- **GitHub Pages URL:** `https://digitsup.github.io/liverpool-reports/q1-2026/`
- Push via the GitHub token at `~/.config/github/token`
- Confirm the live URL when done

---

## Output
- Save final HTML to: `callie-output/liverpool-q1-2026-final.html`
- Then push to GitHub as above
- Report back with: live URL, password, and a brief confirmation of what was changed

---

## Hard Rules
- Do not spawn sub-agents
- Do not send any emails
- Do not push to GitHub without completing the full file first
- Output file goes to `callie-output/` — Mollie will review before anything is delivered to the client
