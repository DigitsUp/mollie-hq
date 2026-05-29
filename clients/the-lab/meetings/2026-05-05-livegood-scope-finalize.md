# LiveGood — Scope & Terms Finalization
**Date:** May 5, 2026 | **Duration:** 48 min | **Source:** Fathom recap

## Meeting Purpose
Finalize the scope and terms for DigitsUp's email marketing engagement with LiveGood.

## Key Takeaways
- **Engagement Approved:** LiveGood approved the $8,700/mo retainer for 90 days, with a 30-day "cancel anytime" clause
- **Data Fix Required:** Ordered Product event only logs the last item in a multi-item order — blocks accurate product segmentation. Top priority fix for dev team (Chris)
- **Phased Rollout:** Launch revenue campaigns immediately; build core flows (Abandoned Suite, Welcome Series) in parallel
- **Triple Whale Rejected:** Ben Glinsky rejected Triple Whale integration — past negative experience, prefers in-house dev for all tracking

## Topics

### Data & Tracking
- Ordered Product event fires only for last item in multi-item orders → bad segmentation
- Dev team (Chris) must fix to fire per product per order
- Triple Whale proposed by Travis Zielasko (90-day cancel, 50% off first months) — rejected by Ben

### Flow Strategy (Phased)
- Phase 1 (Days 1–45): Abandoned Suite (Browse, Cart, Checkout) + Welcome Series
- Phase 2 (Month 2): Post-Purchase Flow — cross-sells, upsells, subscriptions + dynamic replenishment by product consumption rate
- Phase 3 (Month 3): Win-back & Sunset Flows
- Abandoned Suite: 3-email sequence, optimize by adding emails if CTR > 2%, split new vs. returning

### Campaigns
- Launch warm member campaigns immediately for revenue + deliverability warmup
- Content pillars: Quality/Price value prop, ingredient transparency, education (deficiency self-diagnosis), video

### Scope & Terms
- $8,700/mo retainer | 90-day term | 30-day cancel anytime
- Post-90 days: re-scope to lower maintenance fee
- Shared Slack channel as primary comms hub

## Next Steps
**Michael:**
- Send formal agreement with 30-day cancel clause
- Run internal DigitsUp kickoff
- Share project management boards with LiveGood
- Send event-tracking docs to Chris; coordinate Ordered Product fix

**LiveGood team:**
- Provide brand assets + Klaviyo access
- Chris (dev) to fix Ordered Product event tracking

**Travis Zielasko:**
- Audit Klaviyo for tracking discrepancies
- Send checkout friction recs to Ben/Chris
