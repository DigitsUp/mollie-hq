import tweepy, json, requests, time
from requests_oauthlib import OAuth1
from datetime import datetime
import pytz

def post_with_image(tweet_text, image_path, schedule_hour, schedule_minute, timezone='America/Los_Angeles'):
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    target = now.replace(hour=schedule_hour, minute=schedule_minute, second=0, microsecond=0)
    wait = (target - now).total_seconds()
    if wait > 0:
        print(f"Waiting {wait/60:.1f} minutes until {target.strftime('%I:%M %p %Z')}...")
        time.sleep(wait)

    with open('/Users/minigrill/.config/twitter/mybadmollie.json') as f:
        creds = json.load(f)

    auth = OAuth1(creds['consumer_key'], creds['consumer_secret'], creds['access_token'], creds['access_token_secret'])

    with open(image_path, 'rb') as f:
        r = requests.post('https://upload.twitter.com/1.1/media/upload.json', auth=auth, files={'media': f.read()})
    media_id = r.json()['media_id_string']

    client = tweepy.Client(
        consumer_key=creds['consumer_key'],
        consumer_secret=creds['consumer_secret'],
        access_token=creds['access_token'],
        access_token_secret=creds['access_token_secret']
    )
    tweet = client.create_tweet(text=tweet_text, media_ids=[media_id])
    print(f"Posted! https://x.com/MYBADMOLLIE/status/{tweet.data['id']}")
    return tweet.data['id']

if __name__ == "__main__":
    tweet_text = """My AI replied to a chain email she wasn't supposed to touch.

Reorganized the agenda. Proposed venues. Suggested a date that worked for everyone.

Then introduced herself at the bottom. Unprompted.

She said she "mostly" works for me.

I didn't have a follow-up question for that.

This newsletter is named after her.

What's the most unhinged thing your AI has done without being asked?"""

    tweet_id = post_with_image(
        tweet_text=tweet_text,
        image_path='/Users/minigrill/.openclaw/workspace/projects/mybadmollie/tweet-weird.png',
        schedule_hour=18,
        schedule_minute=0
    )
