# Callie Brief — BrandFeatured Welcome Series Copy Doc

## Your Job
Write a complete copy doc for BrandFeatured's Welcome Series and Popup. Output a single `.docx` file using the Copy_Doc_Template.docx format. No industry splits. General voice throughout. File goes to `callie-output/BrandFeatured-Welcome-Series-Copy-Doc-v1.docx`.

---

## Client: BrandFeatured

**What they sell:**
Press release writing and distribution. Gets brands published on real media outlets — USA Today, Benzinga, Medium, Digital Journal, Yahoo Finance, AP News affiliates, NBC/CBS/Fox/ABC regional partners. One-time packages, no contracts.

**Price ladder:**
- $99 — Digital Journal single placement
- $239 — Limited
- $339 — Essential
- $595 — Influence
- $999 — Premium
- $1,499 — Premium+

**Core promise:**
Real media coverage, written by real humans, distributed in 5–8 business days. One free revision. Full refund if they fail to publish.

**Key differentiator (the moat):**
Dynamic "As Seen On" badge. Only BrandFeatured offers this. Badge auto-updates every time the brand earns new coverage. Everyone else ships static logos.

**Who buys:**
Startups raising or launching. DTC brands fighting skepticism on PDPs. Service businesses that get Googled before hired. Personal brands chasing verification. Agencies needing white-label PR.

**Brand voice:**
Transparent. Anti-hype. The site literally says "we don't guarantee placements and we're upfront about that." Authority without puffery. Specific outlets over vague claims. Proof over promises.

**Buyer psychology:**
Default state is skeptical. The PR category is full of mills and scams. Every trust signal matters. The offer alone will not close them. Process clarity plus proof will.

---

## Voice Guardrails

**Write like this:**
- Name specific outlets: USA Today, Benzinga, Medium, Digital Journal
- Lead with outcomes: traffic, credibility, conversions, verification
- Own the transparency: "We don't guarantee placements"
- Short sentences. Active voice. Concrete nouns.
- Talk to the skeptic in their head, not around them
- Real numbers over vague claims (8 premium outlets, 5–8 day turnaround)

**Never write this:**
- No em dashes anywhere. Use periods or commas.
- No guaranteed placement language. Legal boundary.
- No "world's best," "viral," "explode your reach"
- No filler words: literally, basically, very, really, just
- No generic "trusted by thousands" without a number or a name
- No emoji stacking (one max, purposeful)

---

## Offer
- **$50 off first order** (code: `{{ discount_code }}`)
- Expires 7 days from signup
- Applies to all packages (assume yes on $99 Digital Journal unless noted)

---

## Scope: What You're Writing

### Section 1 — Popup (3 Steps)

**Step 1 — Interest Question**
- The question is locked: *"What best describes your brand?"*
- Six options: DTC / Fashion · Service Business · Hospitality · Agency / Reseller · Personal Brand · Tech / Startup
- Write: the surrounding headline, subhead, and any supporting framing copy around the question
- Note: This data is captured for post-purchase personalization later. It does NOT affect welcome copy.

**Step 2 — Name + Email Capture**
- Reveal the $50 offer here
- Write: headline (carry the $50 number), subhead (explain what it unlocks), CTA button
- Tone: reassuring, not begging. No "sign up for our newsletter" framing.

**Step 3 — SMS Activation**
- Frame as activation, not another opt-in
- Write: headline, subhead, CTA button, TCPA-compliant consent line beneath the field
- Angle: "Add your number to activate your $50 off"

---

### Section 2 — SMS 1 (Immediate · T+0)

- Under 160 characters
- Must include: BrandFeatured sender ID, discount code clearly called out, short CTA link to packages page, STOP/HELP compliance
- Tone: direct, friendly, minimal. One line of warmth, code, link. Done.
- Variables: `{{ first_name | default:"" }}`, `{{ discount_code }}`, `{{ packages_url }}`

---

### Section 3 — Email 1 (Immediate · T+0)

**Campaign name:** BF Welcome — Email 1

**Goal:** Deliver the code in email form, introduce who BrandFeatured is, set the transparent tone, make the first offer-to-package connection.

**Theme:** "Welcome. Here's your $50. Here's what we actually do."

**Structure:**
- Hero: Offer reveal with code block, single primary CTA
- What you actually get: 4-point list — Press release written for you · Distribution to real outlets · Full report with live links · Dynamic "As Seen On" badge
- Proof strip reference: Outlet logos (USA Today, Benzinga, Medium, Digital Journal, Yahoo Finance) — note placement in copy
- Primary CTA: See Packages
- Secondary CTA: See a sample report

**Subjects:**
- A — Benefit-led: "Your $50 off is live, {{ first_name }}"
- B — Curiosity-led (write a version here, use brand language)

**Preheader:** Write one that supports whichever subject is live

**Tone:** Warm welcome, zero salesy superlatives. Lean into the anti-hype positioning from the start. Buyer should feel they found the adults in a category full of noise.

**Variables:** `{{ first_name }}`, `{{ discount_code }}`

---

### Section 4 — Email 2 (T+1 Day)

**Campaign name:** BF Welcome — Email 2

**Goal:** Dismantle the "is this legit" objection. This is the email that earns the click in Email 3.

**Theme:** "You're probably wondering how this actually works. Here's the whole process."

**Structure:**
- Opening hook: Acknowledge the skepticism directly. PR space is full of scams. Name it.
- 3-step process: Strategy Call → Writing and Approval → Media Distribution
- The humans angle: "Real people write your release. You review it before anything goes out. Nothing is automated until distribution."
- Timeline: 5–8 business days from approval to live links
- Risk reversal: One free revision if copy misses. Full refund if they fail to publish.
- The moat: Dynamic "As Seen On" badge. Auto-updates. Nobody else offers this.
- Soft CTA: See Packages. Secondary: reminder that $50 off is still active.

**Subjects:**
- A — Objection hook: "Is BrandFeatured a scam? Fair question."
- B — Process hook: "What happens after you place an order"

**Preheader:** Write one

**Tone:** Confident, matter-of-fact. No hype. Quietly authoritative. Sounds like a smart founder explaining things over coffee.

**Variables:** `{{ first_name }}`, `{{ discount_code }}`, `{{ days_remaining }}`

---

### Section 5 — Email 3 (T+2 Days · Offer Expires)

**Campaign name:** BF Welcome — Email 3

**Goal:** Convert the remaining warm list with social proof and a clean expiry. This is the close.

**Theme:** "Real brands. Real results. Your $50 off expires tonight."

**Structure:**
- Hero: Testimonial-forward. One strong quote (write a plausible representative testimonial in the style of the brand's Trustpilot reviews — founder-voice, outcome-specific, no puffery)
- Outcomes block: Quantifiable wins — traffic lift, conversion rate change, client inquiries, verification. Specific language.
- Trustpilot aggregate: Note placement — rating + review count, link to reviews page
- "As Seen On" badge visual: reference in copy — "Here's what your site looks like with the badge installed"
- Hard urgency: Countdown framing or end-of-day expiry line. Be honest — only the discount expires, not the ability to buy.
- Primary CTA: Claim $50 off
- Expiry language: Write 3 versions of the closing urgency line — soft / mid / hard

**Subjects:**
- A — Proof-led: write a version using a result or outcome
- B — Urgency-led: "Last chance: $50 off ends tonight"

**Preheader:** Write one

**Tone:** Confident close. Proof does the talking. Urgency is real, not manufactured. One clean CTA.

**Variables:** `{{ first_name }}`, `{{ discount_code }}`, `{{ expires_at }}`

---

## Output Format

Use the Copy_Doc_Template.docx structure:
- **Section 1:** Popup (3 steps — each step clearly labeled)
- **Section 2:** SMS 1
- **Section 3:** Email 1 (campaign name, subject A, subject B, preheader, hero headline, body copy, CTAs)
- **Section 4:** Email 2 (same structure)
- **Section 5:** Email 3 (same structure + 3 expiry variants)

Output file: `callie-output/BrandFeatured-Welcome-Series-Copy-Doc-v1.docx`

One file. No extras. No HTML. Docx only.
