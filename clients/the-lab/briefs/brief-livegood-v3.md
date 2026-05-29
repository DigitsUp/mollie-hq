# Callie Build Brief — LiveGood Proposal v3
**File to edit:** `/Users/minigrill/.openclaw/workspace/mollie-hq/projects/the-lab/proposal.html`
**One pass. Get it right. Do not ask questions.**

This brief covers 3 targeted changes to Tab 2 (Lifecycles) only. Tab 1 and Tab 3 are untouched.

---

## APPROACH: Use Python

Write `/tmp/livegood_v3.py`. Read the current HTML, make the 3 changes, write back. Do not use sed/echo.

---

## IMAGE ASSETS (already in file as base64 — do NOT re-embed unless replacing)

For reference only:
- img_191 = bundle/sampler banner
- img_192 = popup (10% off, 4 goal categories)
- img_197 = Focus & Mental Clarity welcome email
- img_198 = Performance & Body welcome email
- img_199 = Energy & Daily Wellness welcome email
- img_200 = Sleep & Recovery welcome email

---

## CHANGE 1: Welcome Email Anatomy — Replace with HTML wireframe diagram

**Find:** The current Section 1 in Tab 2 — the "Welcome Email Architecture" section with 7 stacked text blocks.

**Replace with:** An HTML-coded email wireframe mockup with labeled callouts. This should look like a product teardown / annotation diagram — a visual representation of the email structure, not a list.

The wireframe sits in the center of the section. Each section of the email has an annotation label pointing to it from the side (or overlaid). Style it to feel like a design document or strategy diagram.

### HTML structure to build:

```
Section wrapper: cream bg, same padding as other cream sections
Eyebrow: "Stage 1 · Acquire"
Headline: "Welcome Email Architecture"
Subhead: "Every subscriber selects a health goal at signup. That choice drives a fully personalized first email — the right products, the right message, from line one."

Then: a centered wireframe diagram, max-width 680px, centered with margin:auto
```

The wireframe should be a mock email rendered in HTML — forest green and cream palette, clearly "email-shaped" (narrow column, ~480px wide, boxed with a subtle shadow). Each section of the email is a distinct block inside the wireframe. To the left or right of each block (or as overlay labels with a connecting line/dot), show a gold-accented annotation label.

**7 sections of the email wireframe (top to bottom):**

1. **HERO IMAGE**
   Wireframe block: tall rectangle, forest green bg, subtle gradient, centered "HERO IMAGE" text in muted white. Height: ~100px.
   Annotation: "Goal-matched hero — lifestyle photography that signals 'this email was built for you'"

2. **HEADLINE + OFFER**
   Wireframe block: cream bg, centered bold headline mockup text "Welcome to LiveGood — [Goal] Edition" (slightly smaller, italicized placeholder feel), below it a gold pill badge "10% OFF YOUR FIRST ORDER"
   Annotation: "Interest-matched headline + welcome offer — personal from line one"

3. **PRODUCT RECOMMENDATIONS**
   Wireframe block: white bg, 3 small product card placeholders side by side (grey rectangles with product name lines below), labeled "Product 1", "Product 2", "Product 3"
   Annotation: "3 curated products based on goal selection — not best sellers, the right products"

4. **WHY THESE WORK**
   Wireframe block: cream bg, 3 short text lines (mock benefit copy, grey placeholder lines), one under each product
   Annotation: "Ingredient-level value props — builds credibility that converts"

5. **SOCIAL PROOF**
   Wireframe block: white bg, a quote mark icon, 2 lines of placeholder text (grey), a 5-star row, and a small avatar circle
   Annotation: "Testimonial matched to goal category — a Focus subscriber sees a cognitive performance review"

6. **SAMPLER PACK CTA**
   Wireframe block: forest green bg, centered bold text "Not sure where to start?" in white, below it a gold rounded button "Shop the Sampler Pack"
   Annotation: "Reduces decision fatigue — clear first step for subscribers overwhelmed by the catalog"

7. **FOOTER**
   Wireframe block: dark forest (#122A1E) bg, 3 small icon+text pairs (guarantee / quality / member pricing), below them small muted text "Pause emails · Unsubscribe"
   Annotation: "Value props reinforce trust — pause option above unsubscribe reduces opt-out rate"

**Annotation style:** Each annotation is a short label in a small pill or inline tag (gold left border, cream bg, 13px Nunito Sans, dark green text). Position them to the RIGHT of the wireframe column on desktop. On mobile, stack below each section. Connect with a subtle dashed line or just align them vertically.

**Overall container:** On desktop, use a 2-column grid — left column is the wireframe, right column is the stacked annotations aligned to their respective wireframe sections. On mobile, stack vertically.

---

## CHANGE 2: Welcome Series — Replace with flow journey diagram

**Find:** The current Section 2 in Tab 2 — "One Goal Selected. Four Journeys Begin." with popup image and 4 email variant cards.

**Replace with:** A visual flow diagram showing the full welcome series journey.

### Structure:

```
Header (dark bg — keep existing header style):
Eyebrow: "The Welcome Series"
Headline: "One Goal Selected. Four Journeys Begin."
Body: "The popup captures a single data point — the subscriber's top health goal. Email 1 is fully personalized to that goal. Emails 2–5 build the relationship with consistent themes, goal-relevant products, and a clear path to first purchase."
```

```
Body (cream bg):
```

**Part A: Popup image**
Show img_192 in a clean card with label "The Trigger — Goal Selection Popup" and caption "Subscribers choose one of four health goals. That click routes them into a personalized email track."

**Part B: Flow diagram**

Build this as an HTML flow chart. Layout: vertical flow with connecting arrows, responsive.

```
TOP ROW: "SIGNUP" box → arrow → "GOAL SELECTION" box (4 options shown as gold pills: Focus & Mental Clarity · Sleep & Recovery · Energy & Daily Wellness · Performance & Body) → arrow → "4 EMAIL TRACKS"
```

```
EMAIL 1 ROW: Show 4 columns side by side (or 2x2 on mobile), one per goal variant
Each column shows a small card with:
  - Goal category label (gold badge)
  - Thumbnail of the real email image (img_197/198/199/200 respectively, small, ~200px wide)
  - "Fully personalized — goal-matched products, copy, and imagery"
Label above this row: "EMAIL 1 · Day 1 · Personalized by Goal"
```

```
THEN: A converging arrow pointing down to a single column — "EMAILS 2–5: UNIFIED JOURNEY"
Label: "All four paths continue with the same themed sequence"
```

```
EMAILS 2–5: Show as 4 stacked horizontal rows, each spanning full width
Each row: Email number (large gold Barlow Condensed) · Day · Theme name · Short description

Email 2 · Day 3 · BRAND EDUCATION
"The LiveGood story — highest quality ingredients, wholesale pricing, why it's different. Builds trust before asking for a second look."

Email 3 · Day 5 · CATALOG EXPANSION  
"Introduce adjacent products in the subscriber's goal cluster. Show the depth of the catalog relevant to them."

Email 4 · Day 7 · SAMPLER PACK
"'Not sure where to start? Start here.' The best-selling Sampler Pack as a low-risk first purchase. Last chance 10% off reminder."

Email 5 · Day 9 · SOCIAL PROOF + URGENCY
"Real customer results in the subscriber's goal category. Final urgency push — offer expires soon."
```

```
BOTTOM: Arrow → "FIRST PURCHASE" box (gold bg, dark text, Barlow Condensed, prominent)
```

Style the flow rows (Emails 2–5) as clean horizontal cards: email number in large gold type on the left (~60px), day badge, theme name in Barlow Condensed uppercase, description in Nunito Sans. Alternate cream/white bg for visual rhythm.

---

## CHANGE 3: Post-Purchase — Replace with side-by-side journey layout

**Find:** The current Section 4 in Tab 2 — "Every Order Is the Beginning of Something Bigger" — the post-purchase section with the 2-column explainer and 4 flow cards.

**Replace with:** A clean side-by-side journey map — Non-Member track (left) vs Member track (right) — showing emails by day with clear trigger logic. No dynamic "here's what you saved" language.

### Structure:

```
Header (dark bg — keep existing header style):
Eyebrow: "Stage 3 · Expand"
Headline: "Member or Not — Every Buyer Has a Path."
Body: "Post-purchase is LiveGood's biggest LTV lever. The strategy splits cleanly: non-members get a journey designed to show them the value of membership. Members get VIP treatment — recognition, catalog expansion, and bundle logic. Each path is triggered by membership status at the time of purchase."
```

```
Body (cream bg):
```

**Part A: Membership explainer bar**
A dark green bar (not full black — use var(--forest)) spanning full width, with two halves:
- Left half: "NON-MEMBER" label (muted), key stat: "$9.95/mo or $99.95/yr unlocks wholesale pricing. The goal: show them the value, convert to membership."
- Right half: "MEMBER" label (gold), key stat: "Already unlocked wholesale. The goal: expand the catalog relationship, drive bundles, increase AOV."
Divider line between them.

**Part B: Side-by-side journey**

Two columns side by side (50/50 on desktop, stacked on mobile):

**LEFT COLUMN — Non-Member Journey**
Header: "NON-MEMBER TRACK" (muted label, forest green left border)
Trigger: "First order placed · No active membership"

Show as stacked email cards (day by day):

Email 1 · Immediate
**Order Confirmed**
"Your order is on its way. What to expect, how to get the most from your products. Sets a premium tone from the first touchpoint."

Email 2 · Day 3
**Build the Habit**
"Usage guide — how to take your products, when, and why consistency matters. Reinforces the purchase decision."

Email 3 · Day 7 · [GOLD ACCENT — KEY CONVERSION MOMENT]
**The Membership Case**
"Members pay wholesale on everything. Here's what membership costs, here's what it saves. $9.95/month pays for itself on the next order."
Style this card with a gold left border and a subtle gold bg tint — it's the key moment.

Email 4 · Day 14
**What Else Works For You**
"Cross-sell based on goal cluster from signup. Introduce complementary products in the same health category."

**RIGHT COLUMN — Member Journey**
Header: "MEMBER TRACK" (gold label, gold left border)
Trigger: "Any order placed · Active membership"

Email 1 · Immediate
**VIP Order Confirmed**
"Gold-treatment order confirmation. You're a member — you get the best price. Reinforces membership value."

Email 2 · Day 5
**The Bundle Math**
"You're buying these separately. Here's what a bundle saves you. Member pricing + bundle = highest value per dollar."

Email 3 · Day 14
**Time to Restock?**
"Replenishment nudge based on product type and typical usage timing. Keeps the purchase cycle consistent."

---

**Part C: Repeat Buyer note**
Below the two columns, a single full-width callout card (dark bg):
"FOR REPEAT BUYERS (2nd order+): Flows update based on order history. Second-time buyers get catalog expansion — new categories introduced based on what they've already bought. Members on their 3rd+ order receive loyalty recognition and deeper product education."

---

**Part D: Bundle banner**
Below Part C, show img_191 full width (max 800px, centered) with caption:
"Bundle and pack logic drives higher AOV — members see the wholesale savings, non-members see the value case for upgrading."

---

## TECHNICAL

- Python script: `/tmp/livegood_v3.py`
- Read current file, find each section by its existing HTML markers, replace only those 3 sections
- Do not touch Tab 1, Tab 3, Section 3 (Abandoned Suite), Section 5 (Retain), or the summary bar
- Keep all existing CSS variables
- Add any new CSS needed as inline styles or append to the `<style>` block
- Responsive: all side-by-side layouts collapse to single column at max-width: 900px

---

## VERIFICATION

```bash
grep -c "Welcome Email Architecture" [file]     # → 1
grep -c "BRAND EDUCATION\|Brand Education" [file]  # → 1
grep -c "NON-MEMBER TRACK\|Non-Member Track" [file] # → 1
grep -c "MEMBER TRACK\|Member Track" [file]     # → 1
grep -c "The LAB\|thelab" [file]                # → 0
grep -c "data:image/jpeg;base64" [file]         # → 6 (unchanged)
```

Report all results.
