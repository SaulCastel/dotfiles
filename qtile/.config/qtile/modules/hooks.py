from libqtile import hook
import subprocess
import os


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])

@hook.subscribe.screen_change
def sceenChange():
    backgound = os.path.expanduser('~/.fehbg')
    subprocess.call([background])
