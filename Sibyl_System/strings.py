on_string = """
**Retarded Cases Watcher Status**
**Status**: ✅ Successfully connected to the server!
**Description**: You can send ban requests to the dumps. 
"""

# Make sure not to change these too much
# If you still wanna change it change the regex too
scan_request_string = """
**Ban request received**
**Enforcer:** `{enforcer}` 
**User scanned:** `{spammer}`
**Request Reason:** `{reason}`
**Chat Originated from:** {chat}
**Target Message:** `{message}`
$SCAN
"""
forced_scan_string = """
**Forced ban request received**
**Inspector:** {ins}
**User scanned:** `{spammer}`
**Request Reason:** `{reason}`
**Chat Originated from:** {chat}
**Target Message:** `{message}`
$FORCED
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