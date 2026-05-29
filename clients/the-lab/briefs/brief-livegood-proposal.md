# Callie Build Brief — LiveGood Proposal Rebuild
**Project:** DigitsUp × LiveGood — 3-tab proposal page  
**Output file:** `/Users/minigrill/.openclaw/workspace/mollie-hq/projects/the-lab/proposal.html`  
**Live URL:** https://digitsup.github.io/thelab-livegood/  
**One pass. Get it right.**

---

## What You're Building

A complete rewrite of the existing proposal HTML. Three-tab page:
1. **Proposal** — existing pitch content, rebuilt for LiveGood
2. **Lifecycles** — visual flow architecture map (9 flows across 4 stages)
3. **Campaigns** — May campaign calendar with segments

The existing file is a proposal for "The LAB" (a kids gym). You are replacing ALL content for LiveGood — a DTC health supplement brand. Keep the HTML/CSS architecture quality (it's excellent) but retheme everything for LiveGood's brand.

---

## Brand Identity — Apply Exactly

```
Primary Background:   Deep Forest Green  #1A3A2A
Accent / CTA:         Gold / Amber        #D4A017  
Light Background:     Warm Cream          #F5F0E8
Text on Dark:         White               #FFFFFF
Text on Light:        Dark Green          #1A3A2A
Secondary Text:       Muted Green/Gray    #4A6B52
Border / Divider:     #C8D9C4
```

**Fonts:** Keep Barlow Condensed (headings) + Nunito Sans (body) — already in the file via Google Fonts. Just swap the color tokens.

**Visual language:**
- Premium wellness. Nature-backed authority.
- Gold = value signal (savings, CTAs, accents)
- Green = trust, health, natural
- Logo treatment: LIVEGOOD in all caps, with "OO" in the logo having a distinct orange treatment — use text only, write it as `Live<span style="color:#E8671A">G</span><span style="color:#E8671A">oo</span>d` or just `LIVEGOOD`
- CTA buttons: gold background (#D4A017), dark text (#1A3A2A), bold uppercase, rounded
- Cards on dark bg: rgba(255,255,255,0.06) with green-tinted border
- Cards on light bg: white with #C8D9C4 border

**Password:** Keep password gate. Password = `LG2026`

---

## Tab System

The page has three tabs. Navigation bar shows:
- **LIVEGOOD** (brand) | DigitsUp (sub-brand)
- Tab links: `Proposal` · `Lifecycles` · `Campaigns`
- Right side badge: `Klaviyo Platinum Partner`

Only one tab is visible at a time. Clicking a tab shows that section, hides the others. Use JS to toggle. Default: Proposal tab active.

Smooth tab switching — no page reload. Active tab link gets a gold underline or indicator.

---

## TAB 1: PROPOSAL

Adapt the existing proposal structure for LiveGood. Every word of The LAB content gets replaced. Keep the section types and CSS classes — just refill with LiveGood content.

### Hero Section
- Eyebrow: `Email & SMS Retention · May 2026`
- Headline (giant Barlow Condensed):
  ```
  More Revenue
  From the List
  You Already Have.
  ```
- Subhead: `Prepared for LiveGood · DigitsUp LLC · 2026`
- Body: "LiveGood has 1M+ subscribers and $3M in monthly revenue — and less than 10% of it is coming from email. That's not a gap. That's an opportunity. A 90-day retention build with DigitsUp activates the full value of what you've already earned."
- Pills: `Lifecycle Automations` · `Campaign Strategy` · `SMS Activation` · `Email + SMS` · `Full Service`
- Stats bar (4 across below hero): `90 Day Engagement` · `9 Flows Built` · `4× Campaigns/Week` · `11+ Years Experience`

### The Opportunity Section (dark bg)
Headline: `LiveGood Has the Audience. Now Let's Monetize It.`

Three opportunity cards:
1. **Email Is Doing Less Than 10% of the Work**  
   "Industry average for a healthy DTC email program is 20–30% of revenue. At $3M/month, that's $600K–$900K in reachable email revenue. Right now, LiveGood is leaving $400K+ on the table every single month."

2. **Ads Are Paused. Email Is the Only Channel.**  
   "With the website redesign underway and paid media on hold, email is the only revenue engine running. The next 30 days are critical — and we're ready to build while the window is open."

3. **The Membership Conversion Gap**  
   "Non-member buyers are paying more and churning faster. A structured post-purchase flow that pitches membership at exactly the right moment — when the math is personal — turns one-time buyers into high-LTV members."

### Why DigitsUp Section (light bg)
4 cards:
1. **Full Service, End to End** — "Strategy, design, copywriting, Klaviyo build, QA, send, and reporting. You don't touch it. You review it and approve it. That's the whole model."
2. **Built for Klaviyo** — "Klaviyo Platinum Partner with 11+ years and 45+ brands scaled. We know the platform at every level — flows, segments, A/B tests, deliverability, reporting."
3. **Design That Matches the Brand** — "Every email built on LiveGood's visual identity — forest green, gold, premium product photography, benefit-led copy. Not a template. A brand-built content system."
4. **Campaign Calendar Ownership** — "Monthly calendar approved by the 25th. Every send planned, segmented, built, and reported. You see results, not work."

Platinum badge block below cards:
"Klaviyo Platinum Partner — awarded to agencies in the top tier of Klaviyo expertise globally. Less than 1% of agencies hold Platinum status."

### Email Design Examples Section (light bg, cream)
Headline: `Design Built for LiveGood`
Subhead: `Every email built on your brand — not a template.`

Body text: "These are examples of the email template system we design for LiveGood — custom creative built around your product catalog, visual identity, and benefit-led copy. Four category variants, one modular system."

**4 example email mockup cards in a 2×2 grid.**  
These are PLACEHOLDER cards — Marl's real designs arrive Sunday. For now, build 4 styled cards that look like email preview panels. Each card should show:
- A styled card with a top color band (use LiveGood green)
- A label badge (the goal category)
- A title line ("Welcome Email Variation — [Goal]")
- A "DESIGN PREVIEW COMING SUNDAY" notice in gold text
- A small thumbnail area with a subtle placeholder pattern

Categories:
1. Focus & Mental Clarity
2. Sleep & Recovery  
3. Energy & Daily Wellness
4. Performance & Body

Style these to look intentional — not broken. Think "design coming soon" state, not error state.

### Pricing / Investment Section (dark bg)
Headline: `The Investment`

Two pricing tiers side by side:

**Tier 1 — Foundation**  
$X,XXX / month (leave amount blank — Michael fills in)  
- 1–2 Campaigns / Week (4–8/month)
- Full lifecycle automation suite (Phase 1, 5 flows)
- Campaign strategy, copy, design, build, send
- Monthly performance report
- Klaviyo account management

**Tier 2 — Growth** (highlight this one as recommended)  
$X,XXX / month (leave amount blank)
- 3–5 Campaigns / Week (12–20/month)
- Full lifecycle automation suite (all 9 flows, Phase 1 + 2)
- Advanced segmentation: member vs. non-member, goal cluster, purchase history
- SMS campaign cadence alongside email
- A/B testing on subject lines, CTAs, send times
- Monthly performance report + strategy session

### Closing / Next Steps Section (dark bg)
Headline: `Let's Build This.`

3 steps:
1. **Scope Call** — "30 minutes. We align on priorities, confirm Klaviyo access, and set the build order for Phase 1."
2. **Phase 1 Build** — "Welcome series, abandonment suite, and post-purchase flows live within 3 weeks. Campaign calendar starts Week 1."
3. **Results Review** — "30-day check-in. Revenue attributed, open rates, conversion rates, what's working, what we're optimizing."

Contact: mike@digitsup.com

---

## TAB 2: LIFECYCLES

Visual architecture map. Show all 9 flows organized into 4 lifecycle stages.

### Header
- Eyebrow: `Automation Architecture`
- Headline: `9 Flows. Every Stage of the Customer Journey.`
- Body: "This is the full retention engine — from the moment someone subscribes to the moment they become a long-term member. Every flow is built for LiveGood's catalog, membership model, and health-driven audience."

### Stage Architecture

Show 4 stage columns or sections with flows nested inside:

---

**STAGE 1: ACQUIRE**
Label: `ACQUIRE · New Subscribers`
Color accent: use a gold badge

**Flow: Welcome Series**
- Trigger: Popup subscribe (goal selection from form)
- 4 goal-based variants: Focus & Mental Clarity · Sleep & Recovery · Energy & Daily Wellness · Performance & Body
- Email count: 4 emails per variant
- SMS: Yes — fires on Email 4 if no purchase
- Phase: 1
- Email breakdown:
  1. Goal-personalized product stack + 10% off claim
  2. Brand story — "highest quality, wholesale price, here's why"
  3. Best sellers in your goal category + social proof
  4. Last chance 10% off + urgency
- Core theme: "Get the first purchase. Don't pitch membership yet — that comes after they buy."

---

**STAGE 2: RECOVER**
Label: `RECOVER · Abandonment Recovery`
Color accent: gold badge

**Flow 1: Browse Abandonment**
- Trigger: Product page view, no add to cart
- Emails: 2
- SMS: No
- Phase: 1
- Email 1 (4hr): Specific product viewed — benefit-led, category-matched copy
- Email 2 (24hr): Related products in the same goal cluster
- Core theme: "Re-engage before intent cools. Lead with the product they looked at."

**Flow 2: Cart Abandonment**
- Trigger: Add to cart, no checkout initiated
- Emails: 3
- SMS: No
- Phase: 1
- Email 1 (1hr): Product reminder + quick benefit recap
- Email 2 (24hr): Ingredient deep-dive — why this product
- Email 3 (48hr): Member pricing math — "members pay X less"
- Core theme: "The workhorse recovery flow. 3 touches, increasing value at each step."

**Flow 3: Checkout Abandonment**
- Trigger: Checkout started, no purchase
- Emails: 2
- SMS: Yes — alongside Email 2
- Phase: 1
- Email 1 (1hr): "You were so close" — product + member price side by side
- Email 2 (24hr): Trust signals — tested, guaranteed, ingredient transparency
- Core theme: "Highest-intent buyers. Urgency-forward. Reinforce the value proposition."

---

**STAGE 3: EXPAND**
Label: `EXPAND · Post-Purchase Growth`
Color accent: gold badge

**Flow 4: Post-Purchase — Non-Member**
- Trigger: First-ever order, no active membership
- Emails: 4
- SMS: Yes — Day 3 usage reinforcement
- Phase: 1
- Email 1 (immediate): Order confirmed, what to expect, build excitement
- Email 2 (day 3): Usage guide — build the habit, get the result
- Email 3 (day 7): **Membership pitch** — "Here's what you saved. Here's what you left on the table. $9.95/month pays for itself on your next order."
- Email 4 (day 14): Cross-sell based on goal cluster (goal captured at signup)
- Core theme: "Membership pitch AFTER purchase, when the savings math is personal. This is the highest-leverage non-member conversion moment."

**Flow 5: Post-Purchase — Member**
- Trigger: Purchase by active member (any order)
- Emails: 3
- SMS: No
- Phase: 1
- Email 1: Order confirmed + VIP member recognition
- Email 2 (day 5): Pack/bundle math — "You're buying these separately. Here's what a pack saves you."
- Email 3 (day 14): Replenishment nudge based on product purchase timing
- Core theme: "VIP treatment. Expand the basket. Drive toward bundles and higher AOV."

**Flow 6: Post-Purchase — Repeat Buyer (Phase 2)**
- Trigger: 3rd purchase onward
- Emails: 2
- SMS: No
- Phase: 2
- Email 1: Loyalty recognition — "You keep coming back. Here's why we love that."
- Email 2: Product education — introduce an adjacent category they haven't tried
- Core theme: "Deep relationship. Introduce the catalog breadth. Build the habit stack."

---

**STAGE 4: RETAIN**
Label: `RETAIN · Reactivation & List Health`
Color accent: gold badge

**Flow 7: Winback**
- Trigger: No purchase in 90 days
- Emails: 3
- SMS: Yes — final touchpoint alongside Email 3
- Phase: 1
- Email 1: "Here's what's new" — re-intro, product refreshes, new arrivals
- Email 2: Best sellers + social proof — "what members are loving right now"
- Email 3: Timed offer + membership reminder
- Core theme: "Re-engage with value first, offer second. SMS on final touch for last-chance urgency."

**Flow 8: Member Renewal Reminder (Phase 2)**
- Trigger: Annual membership expiring in 14 days
- Emails: 2
- SMS: Yes
- Phase: 2
- Email 1 (14 days out): "Your membership is up for renewal — here's what you've saved this year"
- Email 2 (3 days out): Urgency + easy renew link
- Core theme: "Protect the membership base. Show them the math on what they've saved."

**Flow 9: Sunset**
- Trigger: No engagement in 180 days
- Emails: 1
- SMS: No
- Phase: 1 (run this early — list health matters)
- Email 1: Honest last-chance — "We'll keep you on the list if you want to stay. One click."
- Suppress non-responders
- Core theme: "Clean the list. Protect deliverability. A smaller engaged list beats a bloated cold one."

---

### Visual Design for Lifecycles Tab

Lay this out as a visual flow map:
- 4 stage "lane" headers (Acquire / Recover / Expand / Retain) across the top
- Each flow is a card underneath its stage
- Cards show: Flow name, trigger, email count, SMS badge (yes/no), Phase badge (1 or 2)
- Expand/collapse or just show all cards in a grid
- Use gold for Phase 1 badges, muted for Phase 2
- SMS badge: small green pill
- A horizontal connection line or arrow between stages (optional but nice)

Make it feel like a strategy document, not a Klaviyo screenshot. This is what we show to win the business.

---

## TAB 3: CAMPAIGNS

### Header
- Eyebrow: `May 2026 · Campaign Calendar`
- Headline: `4 Sends/Week. Every One Intentional.`
- Body: "3 regular campaigns + 1 winback per week = 17 sends in May. Every campaign is pre-segmented, pre-planned, and built around the moments LiveGood's audience is paying attention."

### Segments Block

Show 4 segment definitions at the top before the calendar — styled as 4 cards in a row:

1. **🏆 Members** — Active paying members ($9.95/mo or $99.95/yr). Highest LTV. VIP treatment. Expand catalog, drive bundle upgrades, reward loyalty.

2. **💰 Non-Member Buyers** — Purchased but no membership. Biggest revenue unlock. Every campaign has a soft membership angle. The math closes itself.

3. **👋 Engaged Non-Buyers** — Subscribed, opening/clicking, haven't purchased. Welcome series running. Campaigns reinforce brand and drive first purchase.

4. **🔄 Lapsed Buyers** — No purchase in 60–90 days. Winback pool. Separate track — 1 dedicated send per week. Don't mix with regular sends.

### May Calendar

Display as a proper weekly calendar grid or structured week-by-week table. Show Week, Date range, Campaign name, Segment target, angle/theme. 17 sends total.

---

**WEEK 1 — May 1–7 · Foundation Week**

| Send | Date | Campaign | Segment | Theme |
|------|------|----------|---------|-------|
| 1 | May 1 | SMS Consent Drive | All Engaged | "We're coming to SMS. Opt in for member-only offers and early access." |
| 2 | May 5 | May Kickoff: Start Strong | Members + Engaged Non-Buyers | Foundational Five / Daily Essentials — new month, build your stack |
| 3 | May 7 | The Membership Math | Non-Member Buyers only | "You saved $X on your last order. Members would've saved $Y. Here's the math." |
| W | May 7 | Winback: Re-Intro | Lapsed 60–90 days | "A lot has changed. Worth a look." — soft re-intro, no hard sell |

---

**WEEK 2 — May 8–14 · Mother's Day**

| Send | Date | Campaign | Segment | Theme |
|------|------|----------|---------|-------|
| 4 | May 8 | Mother's Day Gift Guide | All Segments | Skincare Pack + wellness stacks — gift positioning |
| 5 | May 9 | Last Chance — Order by Today | All Segments | Delivery cutoff urgency |
| 6 | May 12 | Post-Mother's Day Pivot | Members + Engaged | Energy + Performance push — summer is coming |
| W | May 14 | Winback: Make an Offer | Lapsed 60–90 days | Incentive-forward — come back with a reason |

---

**WEEK 3 — May 15–21 · Education & Authority**

| Send | Date | Campaign | Segment | Theme |
|------|------|----------|---------|-------|
| 7 | May 15 | Ingredient Story: Super Greens | All Engaged | Deep-dive on what's actually in it — ingredient authority |
| 8 | May 19 | 92% of Americans Are Deficient | Non-Buyers + Lightly Engaged | LiveGood's own stat — awareness play drives first purchase |
| 9 | May 21 | Pack Math: Stop Buying Separately | Members + Non-Member Buyers | Bundle value — you're paying more buying individually |
| W | May 21 | Winback: Last Chance | Lapsed 90+ days | Final send before suppression |

---

**WEEK 4 — May 22–31 · Memorial Day + Summer**

| Send | Date | Campaign | Segment | Theme |
|------|------|----------|---------|-------|
| 10 | May 22 | Memorial Day — Perform Like It | Members + Non-Member Buyers | Fitness/performance/summer body — Muscle + Energy packs |
| 11 | May 26 | Memorial Day Send | All Engaged | Last day push — summer is here |
| 12 | May 28 | Summer Prep Stack | Engaged Non-Buyers + Non-Member Buyers | Weight management + hydration + energy — summer goal framing |
| 13 | May 30 | May Wrap + June Preview | Members | Keep momentum — tease what's coming in June |
| W | May 28 | SMS Winback Final | Lapsed — SMS opt-ins | Final SMS touchpoint before suppression |

---

### Design Notes for Calendar

- Make this visually clean — not a spreadsheet dump
- Week headers are big/bold (Barlow Condensed, gold or green accent)
- Each send is a card or row with: send number, date, campaign name, segment pill(s), angle text
- Segment pills match the 4 segments defined above — each gets a distinct color:
  - Members: gold pill
  - Non-Member Buyers: green pill
  - Engaged Non-Buyers: cream/outlined pill
  - Lapsed: muted gray pill
  - All: dark green pill
- Winback rows have a subtle visual distinction (slightly different background or left border)
- Show total send count: `13 regular sends · 4 winback sends · 1 SMS consent blast = 17 sends in May`

---

## Technical Notes

- **Output:** Single HTML file, self-contained. All CSS inline in `<style>`. No external JS libraries.
- **Password gate:** Keep existing password gate pattern. Password = `LG2026`
- **Tab switching:** Pure JS, no libraries. Tab state managed by toggling `display:none/block` on sections.
- **Responsive:** Keep existing mobile breakpoint (max-width: 900px). All grids collapse to 1 column.
- **Animations:** Keep the `fadeUp` and `reveal` scroll animations from the existing file — they look great.
- **Fonts:** Barlow Condensed + Nunito Sans via Google Fonts (already in file).
- **DO NOT** include any reference to The LAB, Mindbody, kids gym, martial arts, or anything from the previous proposal.
- **DO NOT** reference MLM, affiliates, network marketing, or multi-level anything.
- **DO** write all body copy in a premium, direct, benefit-led tone. No fluff. Michael's brand voice: direct, no buzzwords, every claim tied to revenue or impact.

---

## Final Output

Write the complete HTML to:  
`/Users/minigrill/.openclaw/workspace/mollie-hq/projects/the-lab/proposal.html`

This overwrites the existing file. One complete, clean, production-ready HTML document.
