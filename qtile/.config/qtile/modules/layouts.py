from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Columns(
        # border_focus_stack=["#d75f5f", "#8f3d3d"],
        margin=4,
        border_focus="FFE15D",
        border_normal="#2c5380",
        border_width=3,
    ),
    layout.MonadTall(
        margin=8,
        border_focus="FFE15D",
        border_normal="#2c5380",
        border_width=3,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pentablet"),  # xppen ui
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="zoom"),
    ]
)
