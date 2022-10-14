from libqtile import bar, layout , widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.widget.battery import Battery, BatteryState
#from libqtile.utils import guess_terminal

import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


class MyBattery(Battery):
    def build_string(self, status):
        if status.state == BatteryState.DISCHARGING:
            if status.percent > 0.75:
                char = ''
            elif status.percent > 0.45:
                char = ''
            else:
                char = ''
        elif status.percent >= 1 or status.state == BatteryState.FULL:
            char = ''
        elif status.state == BatteryState.EMPTY or \
                (status.state == BatteryState.UNKNOWN and status.percent == 0):
            char = ''
        else:
            char = ''
        return self.format.format(char=char, percent=status.percent)
battery = MyBattery(
    format='{char}',
    low_foreground="#282c34",
    show_short_text=False,
    low_percentage=0.12,
    foreground="#fcfcfc",
    notify_below=12,
)

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Key([mod], "Return", lazy.layout.swap_left()),
    Key([mod], "h", lazy.layout.shrink_main(), desc="shrink master area"),
    Key([mod], "l", lazy.layout.grow_main(), desc="grow master area"),

    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawn("dmenu_run -nf '#fcfcfc' -nb '#282c34' -sb '#646870' -sf '#fcfcfc' -fn 'JetBrainsMonoMedium Nerd Font-13'"), desc="dmenu"),
    Key([mod, "shift"], "q", lazy.spawn("shutdown -h now"), desc="poweroff"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="from/to floating"),

    Key([],"XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5"), desc="Volume"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("pamixer -d 5"), desc="Volume"),
    Key([],"XF86AudioMute", lazy.spawn("pamixer -t"), desc="Volume"),
    # Key([],"XF86AudioMicMute", lazy.spawn("pamixer -t"), desc="Volume"),
    Key([],"XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5"), desc="Brightness"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5"), desc="Brightness"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            # Key(
            #     [mod, "shift"],
            #     i.name,
            #     lazy.window.togroup(i.name, switch_group=True),
            #     desc="Switch to & move focused window to group {}".format(i.name),
            # ),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(margin = 10, border_focus = "#fcfcfc", border_normal = "#282c34", border_width = 3, cange_ratio = 0.05, max_ratio = 0.9, min_ratio  = 0.1, single_border_width = 0, single_margin = 0),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrainsMonoMedium Nerd Font",
    fontsize=16,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = bar.Gap(40),
        # top=bar.Bar(
        #     [
        #         widget.GroupBox(),
        #         widget.WindowName(),
        #         widget.Battery(format='[ BAT {percent:2.0%} ]'),
        #         # widget.Wlan(interface='wlo1',format="[ NET {essid} ]" ),
        #         widget.PulseVolume(format="[ NET {essid} ]" ),
        #         widget.Clock(format="[ %H:%M:%S ]"),
        #         # widget.QuickExit(),
        #     ],
        #     35,
        #     # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        #     # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        # ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width = 0, # was add
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
