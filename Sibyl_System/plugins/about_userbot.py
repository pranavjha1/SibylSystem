from Sibyl_System import System, system_cmd
from Sibyl_System.strings import repoMetadata

@System.on(system_cmd("repo"))
async def pullRepoMeta(event):
    await event.reply(repoMetadata)

__plugin_name__ = "aboutUserbot"

help_plus = """
**Help for About Userbot**

_Getting repo info__
`repo` -  Get information about the repository.

**Notes:**
`/` `?` `.` `!` are supported prefixes.
**Example:** `/repo` or `?repo` or `.repo`
"""