# Integration Runbooks
_Full operational detail for all integrations. Load this file when actively using an integration._

---

### Preflight Script
- **Location:** `workspace/scripts/preflight.py`
- **Purpose:** Validates all integrations are live before starting a session. Run at session start if any integration looks stale.
- **Usage:** `python3 workspace/scripts/preflight.py`

---

### Gmail
- **Account:** mollie@digitsup.com
- **Token:** `~/.config/gmail/mollie_token.json`
- **OAuth creds:** `workspace/gmail_credentials/`
- **Refresh:** Re-run OAuth flow using credentials if token expires. Token is stored as JSON (access + refresh token).
- **Test endpoint:** `GET https://gmail.googleapis.com/gmail/v1/users/me/profile` — returns email address on success.

---

### Google Calendar
- **Account:** mike@digitsup.com (read-only)
- **Token:** `~/.config/gcal/mike_token.json`
- **Refresh:** OAuth refresh token stored in JSON. Re-authorize if expired.
- **Test endpoint:** `GET https://www.googleapis.com/calendar/v3/users/me/calendarList` — returns calendars on success.

---

### Notion
- **Key:** `~/.config/notion/api_key`
- **Version header:** `Notion-Version: 2022-06-28`
- **Workspace:** DigitsUp (owned by Debbie Taylor — Mollie has API access, not admin)
- **Test endpoint:** `GET https://api.notion.com/v1/users/me` — returns bot user on success.

---

### Slack
- **Bot token:** `~/.config/slack/bot_token` (xoxb-...)
- **App token:** `~/.config/slack/app_token` (xapp-...) — for Socket Mode
- **Mode:** Mention-only (bot responds when @mentioned)
- **Note:** Bot connected. Join new channels as needed when Michael adds them.

---

### Klaviyo — All 3 Accounts

| Account | Path | Account ID |
|---|---|---|
| Liverpool LA | `~/.config/klaviyo/liverpool/api_key` | JeMYJL |
| Riversol Skincare | `~/.config/klaviyo/riversol/api_key` | TMwKL4 |
| Hiba Academy | `~/.config/klaviyo/hiba/api_key` | TrGDfH |

- **Access level:** Read-only (client data safety is top priority)
- **Test endpoint:** `GET https://a.klaviyo.com/api/accounts/` with `Authorization: Klaviyo-API-Key {key}` and `revision: 2024-02-15`

---

### GitHub
- **Token:** `~/.config/github/token`
- **Org:** DigitsUp
- **Repo pattern:** `DigitsUp/[client-name]` (e.g., DigitsUp/riversol, DigitsUp/hiba, DigitsUp/mollie-hq)
- **Pages pattern:** `digitsup.github.io/[repo-name]/[path]`
- **Internal HQ:** DigitsUp/mollie-hq → https://digitsup.github.io/mollie-hq/
- **Test:** `GET https://api.github.com/user` with `Authorization: Bearer {token}`

---

### Figma
- **Token:** `~/.config/figma/token`
- **Team ID:** 1278952831789382683
- **Access:** Read-only via REST API. Writing requires Plugin API (runs inside Figma app) — not available here.
- **Rho Nutrition file key:** TkoU9zovIP1VvPTIxqS7SG
- **Test endpoint:** `GET https://api.figma.com/v1/me` with `X-Figma-Token: {token}`

---

### Fathom
- **API key:** `~/.config/fathom/api_key`
- **Webhook secret:** `~/.config/fathom/webhook_secret`
- **Access:** Meeting metadata only (not summaries/transcripts via personal key)
- **Workaround:** mollie@digitsup.com added to Fathom email summaries
