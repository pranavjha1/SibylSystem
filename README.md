# Retarded Cases Watcher
An Telethon userbot that made to fban pajeets on Telegram.

## Getting Started

1. [Fork the repo](https://gitlab.com/RetardedCasesOnTG/RetardedCasesWatcher-TGUserbot/-/forks/new) to the namespace you have access.
2. Sign in to Heroku, create an new app for your fork then generate an new API token (**Account Settings** -> **Applications**).
2. Open the **CI/CD Settings**, expand the **Variables** section, then add your app name as `HEROKU_APP_NAME` and your
API key as `HEROKU_PRODUCTION_KEY`.
3. Before deploying to Heroku, see the detailed configuration list below before editing strings or doing some code edits.

## Configuration
| Environment Variable | Description | Type |
| --- | --- | --- |
| `ENV` | To enable env mode. | Boolean |
| `API_ID_KEY` | Telegram API app ID, generted from <https://my.telegram.org> | Interger |
| `API_HASH_KEY` | Telegram API app hash, generted from <https://my.telegram.org> | String |
| `STRING_SESSION` | String session, generated from the `rcw-cli generate-string-session`. | String |
| `BOT_TOKEN` | Bot API token, generated from BotFather, for inline stuff | String |
| `HEROKU_API_KEY` | Heroku API key, generated from **Account Settings** -> **Applications**. | String | 
| `HEROKU_APP_NAME` | Your Heroku app slug. | String |
| `MONGO_DB_URL` | MongoDB URL, must be the 3.4+ URL format. | String |
| `SIBYL` | ID of Users who have full access to the userbot. | Intergers, speraated by spaces |
| `INSPECTORS` | ID of users who can force an approval on scans, can manage blacklists, etc. | Intergers, speraated by spaces |
| `ENFORCERS` | ID of users who can send ban requests. | Intergers, speraated by spaces |
| `Sibyl_logs` | Chat ID where ban requests are sent. | Interger
| `Sibyl_approved_logs` | Chat ID where approved requests are being logged. | Interger
| `GBAN_MSG_LOGS` | Chat ID where triggeres `/fban` command. | Interger

## Credits
* Original repo where we forked: https://github.com/AnimeKaizoku/SibylSystem
