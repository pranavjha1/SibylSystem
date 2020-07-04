# Retarded Cases Watcher
An Telethon userbot that made to fban pajeets on Telegram.

## Getting Started

1. [Fork the repo](https://gitlab.com/RetardedCasesOnTG/RetardedCasesWatcher-TGUserbot/-/forks/new) to the namespace you have access.
2. Sign in to Heroku, create an new app for your fork then generate an new API token (**Account Settings** -> **Applications**).
2. Open the **CI/CD Settings**, expand the **Variables** section, then add your app name as `HEROKU_APP_NAME` and your
API key as `HEROKU_PRODUCTION_KEY`.
3. Before deploying to Heroku, see the detailed configuration list below before editing strings or doing some code edits.

## Configuration
| Environment Variable | Description | Required |
| --- | --- | --- |
| `ENV` | To enable env mode. | true, especially if you need to deploy it to Heroku. |
| `API_ID_KEY` | Telegram API app ID, generted from <https://my.telegram.org> | true |
| `API_HASH_KEY` | Telegram API app hash, generted from <https://my.telegram.org> | true |
| `STRING_SESSION` | String session, generated from the `rcw generate-string-session`. | true |
| `BOT_TOKEN` | Bot API token, generated from BotFather, for inline stuff | true |
| `HEROKU_API_KEY` | Heroku API key, generated from **Account Settings** -> **Applications**. | true | 
| `HEROKU_APP_NAME` | Your Heroku app slug. | true |
| `MONGO_DB_URL` | MongoDB URL, must be the 3.4+ URL format. | true |



## Credits
* Original repo where we forked: https://github.com/AnimeKaizoku/SibylSystem
