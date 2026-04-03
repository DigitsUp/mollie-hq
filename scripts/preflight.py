#!/usr/bin/env python3
"""
Preflight token refresh — run at session start.
Refreshes Gmail + GCal OAuth tokens before they're needed.
Safe to run multiple times (no-op if token still fresh).
"""

import json
import urllib.request
import urllib.parse
import datetime
import sys

SERVICES = {
    "Gmail": "/Users/minigrill/.config/gmail/mollie_token.json",
    "GCal":  "/Users/minigrill/.config/gcal/mike_token.json",
}

VERIFY_URLS = {
    "Gmail": "https://gmail.googleapis.com/gmail/v1/users/me/profile",
    "GCal":  "https://www.googleapis.com/calendar/v3/users/me/calendarList",
}

def is_expired(expiry_str):
    """Return True if token expires within the next 10 minutes."""
    try:
        expiry = datetime.datetime.fromisoformat(expiry_str.replace("Z", "+00:00"))
        now = datetime.datetime.now(datetime.timezone.utc)
        return expiry - now < datetime.timedelta(minutes=10)
    except Exception:
        return True  # Assume expired if we can't parse

def refresh_token(name, path):
    with open(path) as f:
        creds = json.load(f)

    expiry = creds.get("expiry", "")
    if expiry and not is_expired(expiry):
        print(f"  {name}: token still valid, skipping refresh")
        return creds["token"]

    print(f"  {name}: refreshing expired token...")
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": creds["refresh_token"],
        "client_id": creds["client_id"],
        "client_secret": creds["client_secret"],
    }).encode()

    req = urllib.request.Request(creds["token_uri"], data=data, method="POST")
    resp = urllib.request.urlopen(req, timeout=10)
    result = json.loads(resp.read())

    new_token = result["access_token"]
    creds["token"] = new_token
    creds["expiry"] = (
        datetime.datetime.utcnow()
        + datetime.timedelta(seconds=result.get("expires_in", 3600))
    ).isoformat() + "Z"

    with open(path, "w") as f:
        json.dump(creds, f, indent=2)

    print(f"  {name}: token refreshed OK")
    return new_token

def verify(name, token):
    url = VERIFY_URLS[name]
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
        if name == "Gmail":
            print(f"  {name}: live ✓ ({data.get('emailAddress')})")
        else:
            count = len(data.get("items", []))
            print(f"  {name}: live ✓ ({count} calendars)")
    except Exception as e:
        print(f"  {name}: VERIFY FAILED — {e}", file=sys.stderr)

def main():
    print("=== Preflight Token Refresh ===")
    all_ok = True
    for name, path in SERVICES.items():
        try:
            token = refresh_token(name, path)
            verify(name, token)
        except Exception as e:
            print(f"  {name}: FAILED — {e}", file=sys.stderr)
            all_ok = False

    print("=== Preflight complete ===")
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
