# TOOLS.md
_Quick reference only. Full runbooks: `reference/integration-runbooks.md`_

## Integrations

| Integration | Token / Key Path | Account / ID | Notes |
|---|---|---|---|
| Gmail | `~/.config/gmail/mollie_token.json` | mollie@digitsup.com | OAuth, refresh token included |
| Google Calendar | `~/.config/gcal/mike_token.json` | mike@digitsup.com | Read-only |
| Notion | `~/.config/notion/api_key` | DigitsUp workspace | Debbie owns admin. Mollie has API access. |
| Slack | `~/.config/slack/bot_token` + `app_token` | DigitsUp workspace | Mention-only mode |
| Klaviyo / Liverpool | `~/.config/klaviyo/liverpool/api_key` | JeMYJL | Read-only |
| Klaviyo / Riversol | `~/.config/klaviyo/riversol/api_key` | TMwKL4 | Read-only |
| Klaviyo / Hiba | `~/.config/klaviyo/hiba/api_key` | TrGDfH | Read-only |
| GitHub | `~/.config/github/token` | Org: DigitsUp | Pages: `digitsup.github.io/[repo]/` |
| Figma | `~/.config/figma/token` | Team: 1278952831789382683 | Read-only via REST |
| Fathom | `~/.config/fathom/api_key` | — | Metadata only. Summaries via email. |

## Preflight
Run if any integration looks stale: `python3 workspace/scripts/preflight.py`
