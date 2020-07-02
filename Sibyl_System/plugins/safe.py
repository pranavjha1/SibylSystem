from Sibyl_System import System, system_cmd
import os
import sys

@System.on(system_cmd(pattern = r"rcw reboot"))
async def reboot(event):
    if event.fwd_from:
        return
    await event.reply('Rebooting the API server, this will not take an hour...')
    await System.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@System.on(system_cmd(pattern = r"rcw shutdown"))
async def shutdown(event):
    if event.fwd_from:
        return
    await event.reply("Shutting down, please start me manually afterwards to use me...")
    await System.disconnect()
