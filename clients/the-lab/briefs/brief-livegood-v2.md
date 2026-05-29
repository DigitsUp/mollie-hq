# Callie Build Brief — LiveGood Proposal v2
**File to edit:** `/Users/minigrill/.openclaw/workspace/mollie-hq/projects/the-lab/proposal.html`
**One pass. Get it right. Do not ask questions.**

This is a full rebuild of Tab 1 (Proposal) and Tab 2 (Lifecycles). Tab 3 (Campaigns) stays untouched.

---

## APPROACH: Use Python

Write a Python script at `/tmp/livegood_v2.py` that reads the current HTML, makes all changes described below, and writes the result back. Run it. Do not use sed/echo for HTML with base64 content.

---

## BRAND TOKENS (unchanged)
```
--forest:     #1A3A2A
--forest-dk:  #122A1E
--gold:       #D4A017
--cream:      #F5F0E8
--border:     #C8D9C4
--orange:     #E8671A
Fonts: Barlow Condensed (headings) + Nunito Sans (body)
Password: LG2026
```

---

## IMAGE ASSETS

Load these via Python base64 before building:
```python
import base64

img_191 = base64.b64encode(open('/Users/minigrill/.openclaw/media/inbound/file_191---66ffeab3-c217-488c-8590-dad4cd1555bd.jpg','rb').read()).decode()
img_192 = base64.b64encode(open('/Users/minigrill/.openclaw/media/inbound/file_192---8285251d-3d23-4561-bf84-bbcd1e99df12.jpg','rb').read()).decode()
img_197 = base64.b64encode(open('/Users/minigrill/.openclaw/media/inbound/file_197---c4c71c9b-60c3-417a-9150-3a0ec9f7ef9f.jpg','rb').read()).decode()
img_198 = base64.b64encode(open('/Users/minigrill/.openclaw/media/inbound/file_198---9aea094a-e672-40d0-ab36-b3f1cada772e.jpg','rb').read()).decode()
img_199 = base64.b64encode(open('/Users/minigrill/.openclaw/media/inbound/file_199---a5b2f351-e6fd-437b-a09f-e3411b9a5ff1.jpg','rb').read()).decode()
img_200 = base64.b64encode(open('/Users/minigrill/.openclaw/media/inbound/file_200---66c5e95b-d0e9-4e7d-a4da-fa23df9a54c3.jpg','rb').read()).decode()
```

Image assignments:
- img_191 = bundle/sampler value banner
- img_192 = popup (10% off, 4 goal categories)
- img_197 = Focus & Mental Clarity welcome email
- img_198 = Performance & Body welcome email
- img_199 = Energy & Daily Wellness welcome email
- img_200 = Sleep & Recovery welcome email

---

## TAB 1: PROPOSAL — FULL REBUILD

Replace the entire `#tab-proposal` div content. Keep the outer `<div id="tab-proposal" class="tab-section active">` wrapper and closing `</div>`.

### Section order for Tab 1:
1. Hero
2. The Opportunity (4 cards, 2×2)
3. Why DigitsUp (6 cards)
4. Automation Suite (9 flow rows)
5. 90-Day Roadmap (3 phases)
6. Pricing / Investment (2 tiers)
7. Next Steps / Closing CTA
8. Footer

**Remove entirely:** Email Design / Creative section — it no longer exists on Tab 1.

---

### 1. HERO

Two-column layout on desktop: left = headline + body + pills, right = stats panel.

```
Left column (60%):
- Eyebrow: "Email & SMS Retention · May 2026"
- Headline (Barlow Condensed, giant, uppercase):
  "The Work
  Starts
  Day One."
  
- Subline (small, muted): "Prepared for LiveGood · DigitsUp LLC · 2026"

- Body:
  "LiveGood has built something real — 1M+ subscribers, a product catalog people believe in, and a membership model that earns loyalty. We're here to build the retention engine that matches the brand you've already earned. Full service. Every flow. Every campaign. Day one."

- Pills: "Lifecycle Automations" · "Campaign Strategy" · "SMS Activation" · "Full Service" · "Klaviyo Platinum"

Right column (40%) — stats panel, dark card:
  4 stats stacked or 2×2:
  - 90 Day / Engagement Build
  - 9 Flows / Built & Live
  - 4× / Campaigns/Week
  - 11+ Yrs / Retention Experience
```

Mobile: stacks to single column, stats below content.

---

### 2. THE OPPORTUNITY

Dark bg section. Headline: `LiveGood Has the Audience. Now Let's Activate It.`

Subhead: "LiveGood's model is built around a passionate, health-driven community with high repeat purchase potential. Most of that lifetime value is sitting dormant in the list — recoverable through the right automation architecture and a consistent campaign cadence."

4 cards in a 2×2 grid:

1. **Abandoned Revenue Recovery** — Cart, checkout, and browse abandonment are the highest-ROI flows in retention. Without a complete abandonment suite, LiveGood is leaving meaningful first-party revenue on the table every single day.

2. **Welcome Experience & First Purchase** — The popup subscriber who never converts is a common leak point. A segmented welcome series — built around LiveGood's product categories and health goals — drives that first purchase before interest fades.

3. **Post-Purchase LTV Expansion** — LiveGood's catalog is deep — vitamins, greens, protein, skincare, bundles. A structured post-purchase flow cross-sells related products, educates on benefits, and builds the habit loop that drives membership and repeat orders.

4. **Win-Back & List Health** — Lapsed members and dormant subscribers are high-intent when re-engaged correctly. A proper winback sequence — with a sunset to protect deliverability — keeps the list clean and the engaged segment growing.

---

### 3. WHY DIGITSUP

Cream bg. Headline: `Klaviyo Platinum Partner. 11+ Years of Retention.`

Subhead: "We work exclusively with DTC and ecommerce brands. That focus means faster setup, better creative, and a team that already knows what works for a health-product catalog like LiveGood's."

6 cards in a 2×3 or 3×2 grid:

1. 🏆 **Klaviyo Platinum Partner** — Platinum-tier designation means Klaviyo has vetted our work, our results, and our processes. We get early access to features and dedicated Klaviyo support for your account.

2. ⚡ **Flows Live in Week One** — No 6-week ramp. Cart, checkout, and browse abandonment flows are prioritized first so revenue recovery starts before Month 1 is over.

3. 📊 **Revenue-First Reporting** — Every report ties back to dollars — flow-attributed revenue, campaign revenue per recipient, and list health metrics that tell you what the next move is.

4. 🧬 **Health Brand Fluency** — We understand supplement, wellness, and health product copywriting — benefit-led, claim-compliant, and customer-trust-forward. No generic campaigns.

5. 🔁 **Retention Systems, Not One-Offs** — We build architecture that compounds. The flows, segments, and campaign logic we build in Month 1 get smarter in Month 3 — because everything is connected and tracked.

6. 🤝 **A Real Team, Not a Solopreneur** — Strategy, copy, design, and QA are handled by a dedicated team. You get consistent execution and a single point of contact.

Below cards: Platinum badge block (dark bg card) — "Klaviyo Platinum Partner — awarded to agencies in the top tier of Klaviyo expertise globally. Less than 1% of agencies hold Platinum status."

---

### 4. AUTOMATION SUITE

Dark bg. Eyebrow: "Automation Suite". Headline: `9 Flows. All Signal, No Waste.`

Body: "Every automation below is built to fire at exactly the right moment, with logic designed for LiveGood's membership model, product catalog depth, and health-conscious customer base."

9 flow rows (same style as current — dark cards, flow name + trigger + description + Phase badge):

1. **Browse Abandonment** · product page view, no add-to-cart · Phase 1
   Re-engages browsers before intent cools. Copy leans on the specific product viewed — ingredient callouts, benefits, member pricing advantage. 2–3 emails over 48 hours.

2. **Cart Abandonment** · add-to-cart, no checkout initiated · Phase 1
   The workhorse recovery flow. 3-touch sequence with a product reminder, social proof or ingredient deep-dive, and a soft incentive on touch 3 if still unconverted.

3. **Checkout Abandonment** · checkout started, no purchase · Phase 1
   Highest-converting abandonment flow. 2-email sequence, urgency-forward, reinforcing the member value proposition and 60-day guarantee.

4. **Welcome Series** · popup subscribe, no prior purchase · Phase 1
   4 goal-based variants (Focus, Sleep, Energy, Performance). Brand-first, product-second welcome that earns trust before it asks for a sale. 4 emails over 10 days.

5. **Post-Purchase — Non-Member** · first order, no membership · Phase 1
   Celebrates the first purchase, then at Day 7 delivers the membership pitch — "here's what you saved, here's what you left on the table." The math closes the sale.

6. **Post-Purchase — Member** · purchase by active member · Phase 1
   VIP treatment. Recognizes loyalty, expands catalog, drives bundle upgrades.

7. **Post-Purchase — Repeat Buyer** · 3rd purchase onward · Phase 2
   Deep relationship. Introduces adjacent catalog categories, builds the habit stack.

8. **Winback** · no purchase in 90 days · Phase 2
   3-touch reactivation sequence. SMS touchpoint on the final send.

9. **Sunset** · no engagement in 180 days · Phase 1
   Clean, honest last-chance flow. Suppress non-responders. Protect deliverability.

---

### 5. 90-DAY ROADMAP

Cream bg. Eyebrow: "90-Day Roadmap". Headline: `Built to Generate Revenue in Week One.`

Body: "Three distinct phases — foundation, activation, and scale — each building on the last. By Day 90, LiveGood has a fully operational retention engine running without manual intervention."

3 phases (same style as current build — large faded number left, content right):

**01 — Days 1–30 · Foundation — Klaviyo Audit, Architecture & Phase 1 Flows Live**
- Full Klaviyo account audit — flows, lists, segments, deliverability
- Suppression lists and engagement tiers built from day one
- Abandoned cart, checkout, and browse flows built and live
- Welcome series (4 goal variants) built and live
- Post-purchase (non-member) flow built and live
- Campaign calendar for Month 1 approved and first sends launched

**02 — Days 31–60 · Activation — Phase 2 Flows, Segmentation Depth & Optimization**
- Post-purchase (member + repeat buyer) flows live
- Winback and sunset flows built and live
- SMS flows layered into abandonment and winback sequences
- Full segmentation matrix live: product line, health goal, engagement tier, purchase recency
- Phase 1 flow performance reviewed — optimization round 1 completed
- Month 1 performance report delivered

**03 — Days 61–90 · Scale — Full Engine Running — Test, Learn, Compound**
- A/B testing running across top-performing flows and campaign sequences
- Segment performance analysis — identifying highest-value cohorts
- Full system optimization: timing, frequency, cadence, suppression
- Month 2 performance report delivered
- 90-day retrospective + renewal scope delivered by Day 85

---

### 6. PRICING / INVESTMENT

Dark bg. Eyebrow: "Investment". Headline: `Transparent Pricing. No Setup Fee.`

Body: "Two tiers. Both full service. The difference is volume, velocity, and depth of segmentation."

2 cards side by side. Mark Tier 2 as "Recommended":

**Tier 1 — Foundation — $5,250 / month**
- 1–2 Campaigns / Week (4–8/month)
- Full lifecycle automation suite — Phase 1, 5 flows
- Campaign strategy, copy, design, build, send
- Monthly performance report
- Klaviyo account management

**Tier 2 — Growth — $8,750 / month** ← RECOMMENDED badge
- 3–5 Campaigns / Week (12–20/month)
- Full lifecycle automation suite — all 9 flows, Phase 1 + 2
- Advanced segmentation: member vs. non-member, goal cluster, purchase history
- SMS campaign cadence alongside email
- A/B testing on subject lines, CTAs, send times
- Monthly performance report + strategy session

---

### 7. NEXT STEPS / CLOSING CTA

Dark bg. Eyebrow: "Next Steps". Headline: `Let's Build This.`

3 step cards:
1. **Scope Call** — 30 minutes. We align on priorities, confirm Klaviyo access, and set the build order for Phase 1.
2. **Phase 1 Build** — Welcome series, abandonment suite, and post-purchase flows live within 3 weeks. Campaign calendar starts Week 1.
3. **Results Review** — 30-day check-in. Revenue attributed, open rates, conversion rates, what's working, what we're optimizing.

Below steps: two CTA buttons:
- Primary gold button: "Accept & Move Forward" → mailto:mike@digitsup.com?subject=LiveGood%20Proposal%20—%20Let's%20Move%20Forward
- Ghost/outline button: "Ask a Question" → mailto:mike@digitsup.com?subject=LiveGood%20Proposal%20—%20Question

---

### 8. FOOTER
`DigitsUp — Klaviyo Platinum Partner` | `Prepared for LiveGood · May 2026` | `mike@digitsup.com`

---

## TAB 2: LIFECYCLES — FULL REBUILD

Replace the entire `#tab-lifecycles` div content. Keep the outer wrapper.

### Structure — 5 sections:

---

### SECTION 1: ACQUIRE — Welcome Email Anatomy (infographic)

Header (dark bg):
- Eyebrow: "Stage 1 · Acquire"
- Headline: `Welcome Email Architecture`
- Body: "Every subscriber selects a health goal at signup. That single data point drives a personalized email sequence — the right products, the right message, from email one."

Body (cream bg): Visual infographic-style breakdown of the welcome email anatomy. Show 7 stacked blocks, each representing a section of the email:

```
Block 1: HERO
Label: "Full-width hero image — goal-matched photography"
Description: Visual immediately signals "this email was built for you." Forest green palette, lifestyle imagery matching the goal selected.

Block 2: HEADLINE + WELCOME OFFER
Label: "Interest-matched headline + 10% off offer"
Description: "Welcome to LiveGood, [Goal] Edition." The discount is framed as a goal-specific reward, not a generic coupon. Creates personal relevance from line one.

Block 3: PRODUCT RECOMMENDATIONS
Label: "3 curated products based on interest logic"
Description: Not the best sellers. The right products for this subscriber's stated goal. Each shown with a benefit callout, not just a product name.

Block 4: WHY THESE WORK
Label: "Value props — why these products deliver"
Description: Short, benefit-led copy for each recommendation. Ingredient-level specifics. Builds the credibility that converts browsers into buyers.

Block 5: SOCIAL PROOF
Label: "Testimonial matched to interest category"
Description: The review shown matches the subscriber's goal. A Focus subscriber sees a cognitive performance testimonial. A Sleep subscriber sees a recovery story.

Block 6: SAMPLER PACK CTA
Label: "Value starter pack — 'Not sure where to start?'"
Description: "Start with our best-selling Sampler Pack." Reduces decision fatigue. Gives subscribers who are overwhelmed by the catalog a clear, low-risk first step.

Block 7: FOOTER
Label: "Value props + pause method above unsubscribe"
Description: Final trust signals — guarantee, quality commitment, member pricing reminder. Pause option presented before unsubscribe to reduce opt-out rate.
```

Style each block as a horizontal card with: a gold left-border accent, block number, label in Barlow Condensed, description in Nunito Sans. Alternate cream/white backgrounds for visual rhythm.

---

### SECTION 2: WELCOME SERIES — Popup + 4 Email Variants

Header (dark bg):
- Eyebrow: "The Trigger"
- Headline: `One Goal Selected. Four Journeys Begin.`
- Body: "The popup captures the subscriber's goal in a single click. That choice routes them into a fully personalized welcome series — four distinct email tracks, each built for a different health priority."

Body (cream bg):

**First: Popup example**
Show img_192 as a full-width or prominent image with a caption:
- Label badge: "The Popup"
- Caption: "Subscribers select one goal category. That single data point drives everything — product recommendations, email copy, testimonials, and campaign targeting."

**Then: 4 email variant cards in a 2×2 grid**

Each card:
- Header band (forest green)
- Goal category badge (gold pill)
- Real image embedded (full width, rounded corners)
- Short descriptor note below

Cards:
1. **Focus & Mental Clarity** — img_197 — "Nootropics, greens, and cognitive performance. Built for subscribers who chose brain health."
2. **Performance & Body** — img_198 — "Protein, creatine, and strength stack. Built for subscribers who chose athletic performance."
3. **Energy & Daily Wellness** — img_199 — "Daily essentials, hydration, sustained energy. Built for subscribers who chose everyday vitality."
4. **Sleep & Recovery** — img_200 — "Magnesium, sleep aids, recovery stack. Built for subscribers who chose rest and repair."

---

### SECTION 3: RECOVER — Abandoned Suite

Header (dark bg):
- Eyebrow: "Stage 2 · Recover"
- Headline: `3 Flows. Every Drop of Lost Revenue Recovered.`
- Body: "Browse, cart, and checkout abandonment fire at different stages of intent — each with a distinct message and escalating urgency. 3 emails + 2 SMS across the suite."

Body (cream bg): 3 flow cards, detailed:

**Browse Abandonment** — Phase 1 — 2 emails
Trigger: Product page view, no add-to-cart
- Email 1 (4hr): Specific product viewed — benefit-led, category-matched copy
- Email 2 (24hr): Related products in the same goal cluster
Theme: "Re-engage before intent cools."

**Cart Abandonment** — Phase 1 — 3 emails
Trigger: Add to cart, no checkout initiated
- Email 1 (1hr): Product reminder + quick benefit recap
- Email 2 (24hr): Ingredient deep-dive — why this product
- Email 3 (48hr): Member pricing math — "members pay X less"
Theme: "The workhorse recovery flow. 3 touches, increasing value at each step."

**Checkout Abandonment** — Phase 1 — 2 emails + 2 SMS
Trigger: Checkout started, no purchase
- Email 1 (1hr): "You were so close" — product + member price side by side
- Email 2 (24hr): Trust signals — tested, guaranteed, ingredient transparency
- SMS 1 (alongside Email 1): Short urgency nudge
- SMS 2 (alongside Email 2): Final push with member pricing callout
Theme: "Highest-intent buyers. Urgency-forward."

Show each as a detailed card with trigger, email/SMS breakdown as numbered steps, and a theme callout. Use the existing lc-flow-card styling pattern.

---

### SECTION 4: EXPAND — Post-Purchase Strategy

Header (dark bg):
- Eyebrow: "Stage 3 · Expand"
- Headline: `Every Order Is the Beginning of Something Bigger.`
- Body: "Post-purchase is where LiveGood's membership model creates the biggest LTV opportunity. The strategy splits by member status and order number — because a first-time non-member buyer needs a completely different message than a third-time member."

Body (cream bg): This section needs to feel like deep strategic thinking. Layout:

**Top: 2-column explainer**
Left: "The Member vs. Non-Member Split"
- Members pay wholesale on everything. $9.95/month or $99.95/year unlocks up to 75% savings vs. competitors.
- Every non-member post-purchase flow has one strategic goal: show them the math and convert them to membership.
- Members get VIP treatment — recognition, catalog expansion, bundle logic.

Right: "The Order Number Split"
- 1st order = onboarding. Build the habit. Earn trust.
- 2nd order = deepen. They came back — now expand the catalog relationship.
- 3rd+ order = loyalty. They're a customer. Treat them like one.

**Then: Flow cards**

**Flow 1: Post-Purchase — Non-Member (1st Order)** — Phase 1 — 4 emails + SMS
Trigger: First-ever order, no active membership
- Email 1 (immediate): Order confirmed, what to expect, build excitement. Forest green, premium feel.
- Email 2 (Day 3): Usage guide — build the habit, get the result. SMS reinforcement alongside.
- Email 3 (Day 7): **MEMBERSHIP PITCH** — "You just saved [X]. Members would've saved [Y]. $9.95/month pays for itself on your next order." Show the math. Make it personal.
- Email 4 (Day 14): Cross-sell based on goal cluster captured at signup.
Theme: "The membership pitch lands here — after purchase, when the savings math is real and personal."

**Flow 2: Post-Purchase — Member (Any Order)** — Phase 1 — 3 emails
Trigger: Purchase by active member
- Email 1 (immediate): Order confirmed + VIP member recognition. Gold treatment.
- Email 2 (Day 5): Pack/bundle math — "You're buying these separately. Here's what a pack saves you."
- Email 3 (Day 14): Replenishment nudge based on product purchase timing.
Theme: "VIP treatment. Expand the basket. Drive toward bundles and higher AOV."

**Flow 3: Post-Purchase — Repeat Buyer (2nd Order)** — Phase 2 — 2 emails
Trigger: Second purchase
- Email 1: "You came back. Here's what that means." — loyalty recognition, introduce adjacent category.
- Email 2: Membership pitch (if still non-member) or bundle expansion (if member).
Theme: "The return visit is a signal. Don't miss it."

**Flow 4: Post-Purchase — Loyal Buyer (3rd+ Order)** — Phase 2 — 2 emails
Trigger: 3rd purchase onward
- Email 1: Deep loyalty recognition — "You keep coming back. Here's why we love that."
- Email 2: Product education — introduce a category they haven't tried based on purchase history.
Theme: "Deep relationship. Build the habit stack. Expand the catalog relationship."

Below flows: Show img_191 (bundle/sampler banner) as a full-width example with caption: "Bundle and pack logic drives higher AOV from existing customers — members see the savings math, non-members see the value case for membership."

---

### SECTION 5: RETAIN — Winback + Member Renewal

Header (dark bg):
- Eyebrow: "Stage 4 · Retain"
- Headline: `Win Them Back. Keep Members Renewing.`
- Body: "Two distinct retention tracks — one for lapsed buyers, one for members approaching renewal. Both built to protect revenue that's already been earned."

Body (cream bg): 3 flow cards:

**Winback** — Phase 1 — 3 emails + SMS
Trigger: No purchase in 90 days
- Email 1: "Here's what's new" — re-intro, product refreshes, new arrivals
- Email 2: Best sellers + social proof — "what members are loving right now"
- Email 3: Timed offer + membership reminder
- SMS (alongside Email 3): Final urgency push
Theme: "Re-engage with value first, offer second."

**Member Renewal — Monthly** — Phase 2 — 1 email + SMS
Trigger: 7 days before monthly renewal
- Email 1: "Your membership renews in 7 days — here's what you've saved this month." Easy renew confirmation.
- SMS (3 days out): Short renewal reminder with direct link.
Theme: "Protect the monthly base. Low friction, high clarity."

**Member Renewal — Annual** — Phase 2 — 2 emails + SMS
Trigger: Annual membership expiring in 14 days
- Email 1 (14 days out): "Your membership is up for renewal — here's what you've saved this year." Full savings summary.
- Email 2 (3 days out): Urgency + easy renew link.
- SMS (alongside Email 2): Final push.
Theme: "Show them the math. The annual renewal sells itself."

---

### SUMMARY BAR (bottom of Lifecycles tab, before footer)

Dark bg bar showing:
- "9 Flows · 4 Stages · Full Retention Engine"
- Stats: 7 Phase 1 Flows · 2+ Phase 2 Flows · 5 SMS-Enabled · 4 Welcome Variants

---

## TECHNICAL REQUIREMENTS

- Single HTML file, self-contained. All images base64-encoded inline.
- Password gate unchanged. Password = LG2026.
- Tab switching JS unchanged — Tab 3 (Campaigns) untouched.
- Keep all existing CSS variables and class names where possible. Add new CSS inline or in `<style>` block.
- Scroll reveal animations: keep `.reveal` class on new sections.
- Responsive: all grids collapse to 1 column at max-width: 900px.
- No MLM, affiliate, network marketing references anywhere.
- No "The LAB" references anywhere.

---

## VERIFICATION

After writing, run these checks:
```bash
grep -c "opp-card" [file]         # → 4
grep -c "data:image/jpeg;base64" [file]  # → 6 (popup + bundle + 4 emails)
grep -c "Membership Pitch\|membership pitch\|MEMBERSHIP PITCH" [file]  # → at least 1
grep -c "Annual\|annual" [file]   # → at least 2
grep -c "The LAB\|thelab" [file]  # → 0
python3 -c "open('[file]').read(); print('HTML valid - no encoding error')"
```

Report all results.
