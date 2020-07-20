on_string = """
**Retarded Cases Watcher Status**

**Status**: ✅ Successfully connected to the server!
**Description**: You can send ban requests to the dumps. 
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
**Ban request received**

**Enforcer:** {enforcer} 
**User scanned:** {spammer}
**Request Reason:** `{reason}`
**Chat Originated from:** {chat}
**Target Message:** `{message}`
$SCAN
"""
forced_scan_string = """
**Forced ban request received**

**Inspector:** {ins}
**User scanned:** {spammer}
**Request Reason:** `{reason}`
**Chat Originated from:** {chat}
**Target Message:** `{message}`

$FORCED
"""

autoscan_string = """
**Susicipious activity found due to RegExp/AI detection**

**Scanned user:** [{event.from_id}](tg://user?id={event.from_id})
**Reason:** 0x{c}
**Chat:** {link}
**Hue Color:** Yellow-green
**Message:** {event.text}

$AUTOSCAN
"""

name_blacklist_autoscan_string = """
**Susicipious activity found due to RegExp/AI detection**

**Scanned user:** [{user.id}](tg://user?id={user.id})
**Reason:** 1x{c}
**User joined and blacklisted string in name**
**Matched String:** {word}

$AUTOSCAN
"""

reject_string = """
**Request rejected**
**Crime Coefficient:** `Under 100`
**Reason**: No enforcement action will take effect and the trigger's lock was applied.

$REJECTED
"""

proof_string = """
**Retarded Case file for** - {proof_id} :
┣━**Reason**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""

scan_approved_string = """
**Request approval**

**Target User:** `{scam}`
**Crime Coefficient:** `Over 300`
**Reason:** `{reason}`
**FedAdmin:** `{enforcer}`
**Retarded Case Number:** `{proof_id}`

#LethalEliminator
"""

bot_gban_string = """
**User Banned Alert**

**Enforcer:** `{enforcer}`
**Target User:** `{scam}`
**Reason:** `{reason}`

#DestroyDecomposer
"""

## Please edit this when you fork me.
repoMetadata = """
**Repository Metadata**

__This instance__
Repository Link: https://gitlab.com/RetardedCasesOnTG/RetardedCasesWatcher-TGUserbot
Maintainer: @AJHalili2006 ([@AndreiJirohHaliliDev2006 on GitLab](https://gitlab.com/AndreiJirohHaliliDev2006))

__Upstream Repo__
Upstream repository Link: https://github.com/AnimeKaizoku/SibylSystem
Maintainers: @Dragsama and @Sawada
"""