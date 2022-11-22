from libqtile import bar, layout , widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.widget.battery import Battery, BatteryState, BatteryStatus

import os
import subprocess

from libqtile import hook

# Autostart script
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

# Custom battery icon widget
class BatteryIcon(Battery):
    def build_string(self, status: BatteryStatus) -> str:
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
        return self.format.format(char=char)

class VolumeIcon(widget.Volume):
    def _update_drawer(self):
        if self.volume == -1:
            self.text = "婢"
            self.padding = 12
        elif self.volume <= 10:
            self.text = "奄"
        elif self.volume <= 40:
            self.text = "奔"
        elif self.volume > 40:
            self.text = "墳"
        else:
            self.text = "{}".format(self.volume)

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
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", 
        lazy.spawn("""dmenu_run -nf '#fcfcfc' -nb '#282c34' -sb '#646870'
                   -sf '#fcfcfc' -fn 'JetBrainsMonoMedium Nerd Font-13'"""),
        desc="dmenu"),
    Key([mod, "shift"], "q", lazy.spawn("shutdown -h now"), desc="poweroff"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="from/to floating"),

    Key([],"XF86AudioRaiseVolume", lazy.spawn("pamixer -i 5"), desc="Volume"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("pamixer -d 5"),
        desc="Volume"),
    Key([],"XF86AudioMute", lazy.spawn("pamixer -t"), desc="Volume"),
    # Key([],"XF86AudioMicMute", lazy.spawn("pamixer -t"), desc="Volume"),
    Key([],"XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5"),
        desc="Brightness"),
    Key([],"XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5"),
        desc="Brightness"),
    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
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
    layout.MonadTall(margin = 10, border_focus = "#fcfcfc", 
                     border_normal = "#282c34", border_width = 3, 
                     cange_ratio = 0.05, max_ratio = 0.9, min_ratio  = 0.1, 
                     single_border_width = 0, single_margin = 0),
    layout.Max(),
]

widget_defaults = dict(font="JetBrainsMonoMedium Nerd Font", fontsize = 17,
                       padding=0)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # top = bar.Gap(30),
        top = bar.Bar(
            [
                widget.GroupBox(highlight_method = "block",
                                margin = 0,
                                padding = 8,
                                margin_y = 3,
                                rounded = False,
                                block_highlight_text_color = "#fcfcfc",
                                this_current_screen_border = "#646870"),

                widget.Sep(linewidth = 10, foreground = "#282c34"),
                widget.WindowName(),

                widget.TextBox(text = "", fontsize = 26, padding = 12),
                widget.KeyboardLayout(configured_keyboards=['us', 'ru']),
                widget.Sep(linewidth = 17, foreground = "#282c34"),

                # VolumeIcon(fontsize = 30, padding = 8, update_interval = 1),
                widget.TextBox(text = "奔", fontsize = 30, padding = 8),
                widget.Volume(update_interval = 0.5),
                widget.Sep(linewidth = 7, foreground = "#282c34"),

                BatteryIcon(format = '{char}', padding = 18, fontsize = 18),
                widget.Battery(format="{percent:2.0%}"),
                widget.Sep(linewidth = 15, foreground = "#282c34"),

                widget.TextBox(text = "", fontsize = 21, padding = 10),
                widget.Memory(update_interval = 2, format = "{MemUsed:.0f}{mm}"),
                widget.Sep(linewidth = 11, foreground = "#282c34"),

                widget.TextBox(text = "", fontsize = 21, padding = 14),
                widget.Wlan(update_interval = 5, interface="wlo1", format = "{essid}"),
                widget.Sep(linewidth = 13, foreground = "#282c34"),

                widget.TextBox(text = "", fontsize = 22, padding = 12),
                widget.Clock(update_interval = 60, format="%H:%M"),
                widget.Sep(linewidth = 10, foreground = "#282c34"),
            ],
            30,
            background="#282c34"
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
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
