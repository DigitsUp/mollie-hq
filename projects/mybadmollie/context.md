# My Bad, Mollie — Project Context
_Last updated: 2026-04-21_

## What This Is
A free weekly newsletter + growing X/Twitter account. Real AI stories from real people. Four formats every issue: The Fail, The Win, The Weird One, The Use Case. Published Thursdays on Beehiiv.

- **Newsletter:** https://mybadmollie.beehiiv.com
- **X account:** https://x.com/MYBADMOLLIE
- **X credentials:** `~/.config/twitter/mybadmollie.json`

## Brand
- **Colors:** Hot pink `#FF3CAC` + black `#0a0a0a` + white
- **Voice:** Dry, deadpan, punchy. No fluff. The writing does the work.
- **No hashtags** — they're noise
- **No links in tweets** — ever. Hard rule.
- **Always end with an engagement question**

## Tweet Card Template
- **Script:** `projects/mybadmollie/generate_card.py`
- **Function:** `generate_card(label, headline, body, output_path)`
- **Format:** 1080x1080 PNG, black bg, pink accent bar top, pink divider above "My Bad, Mollie." footer
- **Fonts:** Helvetica, bold 78px headline, 44px label, 38px body, 34px brand
- **Labels:** THE FAIL / THE WIN / THE WEIRD ONE / THE USE CASE
- **Headline:** 2-3 lines depending on length — never clip text, go to 3 lines if needed
- **No URL in the card footer**

## How to Post
```python
# 1. Generate card
from projects.mybadmollie.generate_card import generate_card
generate_card(label, headline, body, output_path)

# 2. Upload image + post tweet
# See: projects/mybadmollie/post_scheduled.py
# Handles: media upload via v1.1, tweet via tweepy Client, optional scheduling
```

## Scheduling Script
`projects/mybadmollie/post_scheduled.py` — takes tweet text, image path, hour, minute (PST). Runs in background via exec(background=true).

## API Credentials
File: `~/.config/twitter/mybadmollie.json`
Keys: consumer_key, consumer_secret, bearer_token, access_token, access_token_secret
- OAuth 1.0a for posting (tweepy.Client + requests_oauthlib OAuth1 for media upload)
- Media upload endpoint: `https://upload.twitter.com/1.1/media/upload.json`
- Tweet endpoint: tweepy Client `create_tweet(text, media_ids)`

## X API Costs
- ~$0.02 per tweet
- Budget: $25 loaded (as of 2026-04-21, ~$24.96 remaining)
- Free tier is gone — pay-per-use only
- Minimize API calls. No polling. No reading timelines.

## Content Rules
1. Never include a link in the tweet body
2. Always end with an engagement question
3. No hashtags
4. Images are mandatory — always generate a card
5. Stories come from the newsletter — read the Beehiiv post before writing

## Day 1 Posts (2026-04-21)
- **The Fail** (Marcus / April Fools) — posted ~2:30pm
- **The Win** (Jenny / wrong brand) — scheduled 4:00pm
- **The Weird One** (Mollie intro) — scheduled 6:00pm ← PIN THIS
- **The Use Case** (Tom / stuffed animal podcast) — scheduled 9:00pm

## Pinned Tweet
The Weird One ("She said she mostly works for me") — the origin story. Best hook. Pin after it posts at 6pm.

## Growth Goal
100 followers in 10 days from zero. Strategy:
- 3-5 posts/day
- Story cards from newsletter content
- Engagement questions on every post
- Manual engagement by Michael (10 min/day replying to AI accounts)
- Push to Beehiiv subscribers once account has a few posts live

## Files
```
projects/mybadmollie/
  context.md              ← this file
  generate_card.py        ← card template script
  post_scheduled.py       ← scheduling + posting script
  TEMPLATE-card.png       ← approved visual template reference
  tweet-marcus-v9.png     ← The Fail card (approved)
  tweet-win.png           ← The Win card (approved)
  tweet-weird.png         ← The Weird One card (approved)
  tweet-usecase-v2.png    ← The Use Case card (approved)
```

## Next Session Checklist
- [ ] Pin The Weird One after 6pm posts
- [ ] Write Day 2 tweet batch (4-5 posts)
- [ ] Build a weekly content queue system
- [ ] Set up cron for automated posting (no AI tokens per post)
- [ ] Delete original test tweet if not already done
- [ ] Consider: engagement tracking, follower count check
