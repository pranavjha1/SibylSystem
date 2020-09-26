on_string = """

**☑️ Connection successful!**

Welcome {Enforcer} {name}
You are a valid user!
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
$SCAN
Cymatic Scan request!
**Enforcer:** {enforcer} 
**User scanned:** {spammer}
**Reason:** `{reason}`
**Scan Source:** {chat}
**Target Message:** `{message}`
"""
forced_scan_string = """
$FORCED
**Inspector:** {ins}
**Target:** {spammer}
**Reason:** `{reason}`
**Scan Source:** {chat}
**Target Message:** `{message}`
"""

reject_string = """
$REJECTED
**Crime Coefficient:** `Under 100`
Not a target for enforcement action. 
The trigger will be locked.
"""

proof_string = """
**Case file for** - {proof_id} :
┣━**Reason**: {reason}
┗━**Message**
         ┣━[Nekobin]({paste})
         ┗━[DelDog]({url})"""

scan_approved_string = """
#LethalEliminator
**Target User:** {scam}
**Crime Coefficient:** `Over 300`
**Reason:** `{reason}`
**Enforcer:** `{enforcer}`
**Case Number:** `{proof_id}`
"""

bot_gban_string = """
#DestroyDecomposer
**Enforcer:** `{enforcer}`
**Target User:** {scam}
**Reason:** `{reason}`
"""

# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator

## Please edit this when you fork me.
repoMetadata = """
**Repository Metadata**

__This instance__
Repository Link: https://gitlab.com/ThePinsTeam-FedSupport/SpamSamplesCollector
Maintainer: [@AndreiJirohHaliliDev2006](https://github.com/AndreiJirohHaliliDev2006)

__Upstream Repo__
Upstream repository Link: https://github.com/AnimeKaizoku/SibylSystem
Maintainers: [Dragsama](https://github.com/Dragsama) & [TsunayoshiSawada](https://github.com/TsunayoshiSaada)
"""
