from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="block",
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    other_screen_border="#2b588c",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f",
                ),
                widget.TextBox(text="", padding=0, fontsize=28, foreground="#2f343f"),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground="#ebdbb2", fmt="{}"),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format=" {updates} Updates ",
                    foreground="#ffffff",
                    mouse_callbacks={
                        "Button1": lambda: qtile.cmd_spawn(terminal + " -e yay -Syu")
                    },
                    background="#2f343f",
                ),
                widget.Sep(),
                widget.CurrentLayout(),
                widget.KeyboardLayout(
                    background="2f343f",
                    configured_keyboards=["latam", "us"],
                    display_map={"latam": "LA", "us": "US"},
                    fmt=" kbmap: {} ",
                ),
                widget.Systray(icon_size=20),
                widget.TextBox(text="", padding=0, fontsize=28, foreground="#2f343f"),
                volume,
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground="#2f343f",
                ),
                widget.TextBox(text="", padding=0, fontsize=28, foreground="#2f343f"),
                widget.Clock(
                    # format=' %Y-%m-%d %a %I:%M %p',
                    format=" \uf073  %a %d, %b. | \uf43a %H:%M:%S ",
                    background="#2f343f",
                    foreground="#ebdbb2",
                ),
                widget.TextBox(
                    text="",
                    padding=0,
                    fontsize=28,
                    foreground="#2f343f",
                ),
                widget.Backlight(
                    backlight_name="intel_backlight",
                    format=' 󰃝 {percent:2.0%} ',
                    padding=0,
                    margin=0,
                ),
                widget.Battery(
                    format=" {char} {percent:2.0%} ",
                    charge_char='󰢝',
                    discharge_char='󱊢',
                    full_char='󱊣',
                    background="404552",
                    low_percentage=0.3,
                    low_background="F3E15D",
                    low_foreground="000000",
                    update_interval=15,
                ),
            ],
            24,  # height in px
            background="#404552",  # background color
        ),
    ),
    Screen(),
]
