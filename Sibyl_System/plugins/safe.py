from Sibyl_System import System, system_cmd
import os
import sys
import subprocess

@System.on(system_cmd(pattern = r"ssc update"))
async def gitpull(event):
    subprocess.Popen('git pull', stdout=subprocess.PIPE, shell=True)
    await event.reply('Git pulled probably.')
    os.system('restart.bat')
    os.execv('start.bat', sys.argv)
    
@System.on(system_cmd(pattern = r"ssc restart"))
async def reboot(event):
    if event.fwd_from:
        return
    await event.reply('Rebooting the API server, this will not take an hour...')
    await System.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)


@System.on(system_cmd(pattern = r"ssc shutdown"))
async def shutdown(event):
    if event.fwd_from:
        return
    await event.reply("Shutting down, please start me manually afterwards to use me...")
    await System.disconnect()
