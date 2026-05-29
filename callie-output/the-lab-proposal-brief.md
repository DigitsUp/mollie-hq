# Callie Brief — The LAB Life Proposal Rebuild
**Date:** 2026-05-28
**Output file:** `callie-output/the-lab-proposal-v2.html`
**Based on:** `clients/the-lab/proposals/proposal.html` (existing file — read it fully before building)

---

## The Job

Rebuild the existing LAB Life proposal HTML from scratch — same visual design and code quality, completely new content. The original was built before we had any real intel on the client. Everything has changed. This is the real version.

Do NOT start from a blank file. Read the original proposal at `clients/the-lab/proposals/proposal.html` first. Steal the entire CSS, design system, password gate, nav, animations, footer, and component patterns. Only the content changes.

---

## Client Context

**The LAB Life** — Travis's business. A 25,000 sq ft gamified fitness facility in Arizona built around kids and families. Ninja courses, airbags, gamified treadmills (the games only work when you're moving), basketball court, Peloton studio coming, golf simulator coming. Birthday parties, summer camps, field trips. Membership-based. High energy, incredible in-person experience, community-driven.

**Travis** — the client. High energy, not a micromanager, told Michael "go to town, I want it badass." He already believes in DigitsUp. This proposal isn't about convincing him — it's about showing we understand his business and have a clear vision for what we'd build.

**Current tech stack:**
- GoHighLevel — CRM + automations (this is where we're building month 1)
- Constant Contact — large email list, barely used (Klaviyo migration, month 2)
- Spark — member/billing CRM (we're leaving this alone for now)

**Our relationship:** We audited their GHL setup. RV (DigitsUp team) went through the automations. We have not touched anything yet. This proposal is our vision for what we build together.

---

## Tone — Critical

- **Celebratory and opportunity-first.** The LAB has built something incredible. We're here to build the digital system that matches the in-person experience.
- **No negativity.** Do not frame anything as broken, missing, or failing. Everything is an opportunity.
- **No client stats.** Do not cite their open rates, conversion numbers, or any metrics from their account. We show we did our homework on the stack, not their numbers.
- **Growth partner, not auditor.** We're not presenting a report. We're presenting a vision.
- **Clean and simple.** Travis is high energy, not corporate. Direct, confident, warm.

---

## Design System — Carry Over Exactly

From the original proposal — do not change any of this:
- Fonts: `Barlow Condensed` (headings, heavy weights) + `Nunito Sans` (body)
- Colors: `--navy: #0D1B4B`, `--navy-dk: #0A1538`, `--cyan: #33B5E8`, `--cyan-dark: #1A8FBF`
- Dark hero (navy background, cyan accents, dot grid, glow effects, ambient light orbs)
- Light sections alternate with dark sections
- Card patterns: rounded-corner cards, border + subtle bg, hover states
- Password gate (password: `LABLIFE`)
- Fixed nav with brand + links + Klaviyo Platinum badge
- Scroll-reveal animations (`.reveal` class + IntersectionObserver)
- Footer with logo, tagline, contact email

---

## Section Structure & Content

### PASSWORD GATE
Same as original. Password: `LABLIFE`

---

### NAV
- Brand: `LAB` / `DigitsUp`
- Links: Overview · GHL Build · Klaviyo Layer · Why Us · Next Steps
- Badge: `Klaviyo Platinum Partner`

---

### SECTION 1 — HERO (dark, full-height)

**Eyebrow:** `GoHighLevel Strategy · May 2026`

**Title:**
```
The
LAB
Life.
```
(same giant Barlow Condensed treatment, "LAB" in cyan)

**Subtitle:** `Stronger Kids. Closer Families. Bigger Business.`

**Body copy:**
"The LAB has built something genuinely special — a 25,000 sq ft experience that transforms how families move, compete, and connect. This is the system we'd build to make sure every family that finds The LAB, stays for life."

**Pills (solid):** GHL Automation · 9 Lifecycle Flows · Campaign Engine · Email + SMS
**Pills (outline):** Klaviyo Migration · Constant Contact · Member Retention

---

### SECTION 2 — WHAT YOU'VE BUILT (light bg)

**Eyebrow:** The Foundation

**Title:** "You've built the experience. Now let's build the system."

**Body:** "The LAB's in-person product is exceptional — gamified fitness, structured progression, family community, and a concept that genuinely doesn't exist anywhere else at this scale. The opportunity in front of us is building a digital infrastructure that matches that same level of energy and intention. GoHighLevel is already in place. The audience is warm. The timing is right."

**3 highlight cards:**
1. `The Concept` — Gamified fitness meets family community. A product parents believe in and kids love.
2. `The Platform` — GoHighLevel is already running. We're not starting from scratch — we're leveling it up.
3. `The Audience` — A warm, engaged community of families who've already raised their hand.

---

### SECTION 3 — WHAT WE FOUND (dark bg)

**Eyebrow:** The GHL Audit

**Title:** "We went in. Here's what we saw."

**Body:** "RV (our systems lead) did a full audit of The LAB's GoHighLevel account. The pipeline staging is solid. The foundation is there. What's missing is the full lifecycle system — the flows that run between every stage of the parent journey, from first inquiry to long-term member."

**2 column layout:**

Left — "What's running":
- Trial booking confirmations
- No-show follow-up (SMS)
- VIP pass workflows
- Internal pipeline notifications

Right — "What we'd add":
- Full inquiry nurture sequence
- Pre-trial attendance experience
- Post-trial membership conversion
- New member onboarding (90 days)
- Long-term retention + re-engagement
- Winback for inactive families
- Birthday party → trial funnel
- Summer camp → membership conversion

No stats. No numbers. Just the picture.

---

### SECTION 4 — THE GHL BUILD (light bg) — MAIN SECTION

**Eyebrow:** Month 1 · GoHighLevel

**Title:** "9 flows. 40+ touchpoints. Built in GoHighLevel."

**Body:** "Every flow is triggered by real behavior — a booking, an attendance check, a pipeline stage change. This isn't a batch-and-blast strategy. It's a system that responds to what each family actually does."

**Flow cards — use the same flow card design from the original (featured card + grid cards). Build all 9.**

Present as: pill label (FLOW 01, FLOW 02, etc.) + title + trigger line + 4–6 timeline steps + primary goal.

---

**FLOW 01 — FEATURED CARD (full width, dark)**
`FLOW 01 · Highest Impact`
**Title:** Lead Capture / Inquiry Nurture
**Trigger:** Website inquiry, Facebook lead form, summer camp inquiry, waiver completed without booking
**Goal:** Convert cold parent inquiries into booked trial classes
**Timeline:**
- Immediate · SMS — Fast reassurance. Speed-to-lead.
- +2 Hours · Email — Welcome to The LAB. Emotional trust building.
- Day 1 · SMS — Parent social proof. Community reassurance.
- Day 2 · Email — Transformation stories. Identity + progress.
- Day 4 · Email — Programs + experience education.
- Day 6 · SMS — Simple direct CTA. Low friction.
- Day 8 · Email — Momentum + urgency. Schedule first class.
**Footer:** Primary goal · Booked trial class

---

**FLOW 02**
**Title:** Trial Booked Experience
**Trigger:** Trial class booked · Pipeline: Trial Booked
**Goal:** Increase attendance and emotional investment before the visit
**Timeline:**
- Immediately · Email — Trial confirmation + excitement
- Immediately · SMS — "We're excited to meet you"
- 2 Days Before · Email — What to expect. Reduce uncertainty.
- 1 Day Before · SMS — Attendance reminder
- 1 Day Before · Email — Meet the coaches. Human connection.
- 3 Hours Before · SMS — Final reminder
- 1 Hour After · Email — Thank you + momentum
- Evening · SMS — Low pressure membership CTA
**Footer:** Primary goal · Show up ready

---

**FLOW 03**
**Title:** No Show Recovery
**Trigger:** Pipeline moved to No Show
**Goal:** Recover missed trials. Remove guilt and friction.
**Timeline:**
- 2 Hours After · SMS — Empathy follow-up. Warm recovery.
- Next Morning · Email — "We'd still love to meet you"
- Day 2 · SMS — Easy rebooking. Low friction.
- Day 4 · Email — Student success stories. Reignite excitement.
**Footer:** Primary goal · Rebooked trial

---

**FLOW 04**
**Title:** Membership Conversion
**Trigger:** Trial attended · Pipeline: Trial Attended
**Goal:** Convert trial attendees into long-term members
**Timeline:**
- Day 0 · SMS — "Your child did amazing." Confidence reinforcement.
- Day 1 · Email — Student confidence recap. Transformation positioning.
- Day 2 · Email — Why consistency matters. Long-term growth.
- Day 3 · Email — Parent testimonials. Social proof.
- Day 5 · Email — Program roadmap. Progression + future vision.
- Day 6 · SMS — Enrollment reminder. Gentle urgency.
- Day 7 · Email — Limited spot momentum.
- Day 9 · Email — Final invitation. Join The LAB family.
**Footer:** Primary goal · Membership purchased

---

**FLOW 05**
**Title:** New Member Onboarding
**Trigger:** Membership purchased · Pipeline: Closed Won
**Goal:** Increase retention during the first 90 days
**Timeline:**
- Day 0 · Email — Welcome to The LAB family. Belonging.
- Day 2 · SMS — Attendance encouragement. Routine building.
- Week 1 · Email — What success looks like. Expectation setting.
- Week 2 · Email — Parent expectations. Alignment.
- Week 3 · Email — Community involvement. Family integration.
- Month 1 · SMS — Milestone celebration.
**Footer:** Primary goal · First 90-day retention

---

**FLOW 06**
**Title:** Engagement & Retention
**Trigger:** Member active 30+ days
**Goal:** Maintain engagement. Reduce churn before it happens.
**Timeline:**
- Monthly · Email — Student achievements + recognition
- Monthly · Email — Community spotlights
- Bi-Weekly · SMS — Attendance nudge. Consistency reinforcement.
- Monthly · Email — Referral opportunity
**Footer:** Primary goal · Long-term member retention

---

**FLOW 07**
**Title:** Winback / Reactivation
**Trigger:** Membership inactive · No attendance 30–60 days
**Goal:** Recover inactive families. Reconnect emotionally, no pressure.
**Timeline:**
- Day 0 · Email — "We miss seeing your family." Emotional reconnection.
- Day 2 · SMS — Friendly check-in
- Day 4 · Email — Student progress reminder. Momentum.
- Day 7 · Email — Easy restart offer
- Day 10 · Email — Limited-time incentive. Urgency.
**Footer:** Primary goal · Re-enrollment

---

**FLOW 08 — SPECIAL**
`SPECIAL FLOW`
**Title:** Birthday Party → Membership Funnel
**Trigger:** Waiver signed at party · Party attended
**Goal:** Convert birthday party guests into trial leads
**Timeline:**
- Day 0 · Email — Thank you recap. Event memory reinforcement.
- Day 1 · SMS — Trial invitation. "Would your child love classes too?"
- Day 3 · Email — Parent testimonials. Trust building.
**Footer:** Primary goal · New trial bookings from every event

---

**FLOW 09 — SPECIAL**
`SPECIAL FLOW`
**Title:** Summer Camp → Membership Conversion
**Trigger:** Summer camp completed · Camp participant tagged
**Goal:** Convert camp participants into recurring members
**Timeline:**
- Day 0 · Email — Camp highlights. Positive emotional recap.
- Day 2 · Email — Student transformation. Growth reinforcement.
- Day 4 · SMS — Keep the momentum going
- Day 6 · Email — Membership invitation. Become a member.
**Footer:** Primary goal · Camp → member conversion

---

### SECTION 5 — THE KLAVIYO LAYER (dark bg)

**Eyebrow:** Month 2 · The Klaviyo Layer

**Title:** "33,000 warm contacts. A campaign engine to match."

**Body:** "The LAB's Constant Contact list is one of the most underleveraged assets in the business. Month 2, we migrate it to Klaviyo — warming the list properly, setting up domain authentication, and building the campaign infrastructure that turns that audience into consistent revenue."

**3 cards:**
1. `List Migration` — Full Constant Contact → Klaviyo migration. Clean data, proper warm-up, domain setup done right.
2. `Campaign Engine` — Seasonal pushes, enrollment drives, camp promotions, referral campaigns. The right message at the right moment.
3. `GHL + Klaviyo` — Both systems talk to each other. GHL handles the pipeline and transactional side. Klaviyo handles marketing campaigns and lifecycle at scale.

**Note at bottom:** "Month 1 may include light test sends from Constant Contact to keep the audience warm while we build. Timeline is flexible based on what makes most sense for your current season."

---

### SECTION 6 — WHY DIGITSUP (light bg)

**Eyebrow:** Why DigitsUp

**Title:** "What we bring to the table."

**Body:** Same as original — Klaviyo Platinum Partner, retention-first philosophy, systems not one-offs, revenue you can see. Update one card:

**4 cards:**
1. `Expertise` — GoHighLevel + Klaviyo. We know both platforms and how to make them work together. Most agencies pick one. We build the stack.
2. `Philosophy` — Retention over acquisition. Keeping a member costs a fraction of acquiring one. We build for the long game.
3. `Approach` — Systems, not sends. Every flow responds to real behavior. Every campaign is tied to your business calendar.
4. `Reporting` — Revenue you can see. Monthly reporting showing exactly what the system drove. No vanity metrics.

**Platinum wrap block** — same as original, keep it.

---

### SECTION 7 — NEXT STEPS (dark bg)

**Eyebrow:** Let's Build

**Title:** "Ready when you are."

**3 conversation cards:**
1. `Month 1` — GHL audit review + full 9-flow build. Email design, SMS sequences, pipeline integration. We go to town.
2. `Month 2` — Constant Contact → Klaviyo migration. List warm-up, domain setup, campaign calendar live.
3. `Ongoing` — Monthly reporting, campaign execution, flow optimization. A system that compounds over time.

**CTA block:**
"Questions? Let's talk."
`mike@digitsup.com`

---

### FOOTER
Same as original.
`DigitsUp — Klaviyo Platinum Partner`
`Prepared for The LAB Life · May 2026`
`mike@digitsup.com`

---

## Technical Notes for Callie

- Output: `callie-output/the-lab-proposal-v2.html` — single self-contained HTML file
- Copy the full CSS block from the original verbatim — do not rewrite it
- Password gate: same JS logic, password `LABLIFE`
- Flow cards: reuse `.flow-card`, `.flow-pill`, `.flow-step`, `.flow-channels`, `.flow-footer` classes from original
- Featured card (Flow 01) = `.flow-card.featured` (full width, dark bg) — same as original Flow 01
- Flows 02–09 = standard grid cards, 2-column layout
- Flows 08 + 09 tagged as SPECIAL FLOW in the pill
- Scroll reveal: `.reveal` class on all section bodies + card grids
- All sections: keep `border-bottom: 1px solid #D8E4F0` between light sections
- Dark sections: `background-color: #0A1538` or `#0D1B4B` (alternate as in original)
- Do not add any external dependencies beyond the Google Fonts already in the original
- Test: password gate hides content, pressing Enter or clicking button reveals it

---

## What Success Looks Like

Michael opens it in a browser, enters LABLIFE, and it reads like a premium agency proposal built specifically for The LAB — not a template. The flows are detailed enough to show real strategic thinking. The tone is warm and confident throughout. No negativity, no stats, no filler. Travis reads it and thinks "these guys actually get it."
