from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import keys, mod

groups = [
            Group("1"),
            Group("2"),
            Group("3"),
            Group("4"),
            Group("5"),
            Group("6",
                label="",
                matches=[
                    Match(wm_class=["spectacle"]),
                    Match(wm_class=["pentablet"]),
                ]
            )
          ]


for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
