from libqtile import bar, layout, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy

import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])


mod = "mod4"

keys = [
    # Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    # Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Return", lazy.layout.swap_left()),
    Key([mod], "h", lazy.layout.shrink_main(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.grow_main(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # KeyChord([mod], "r", [
    #     Key([], "h", lazy.layout.grow_left()),
    #     Key([], "l", lazy.layout.grow_right()),
    #     Key([], "j", lazy.layout.grow_down()),
    #     Key([], "k", lazy.layout.grow_up()),
    #     Key([], "r", lazy.ungrab_chord()()),
    #     Key([mod], "r", lazy.ungrab_chord()()),
    #     Key([mod], "h", lazy.layout.grow_left()),
    #     Key([mod], "l", lazy.layout.grow_right()),
    #     Key([mod], "j", lazy.layout.grow_down()),
    #     Key([mod], "k", lazy.layout.grow_up())],
    #     mode = "Resize"),
    #
    # KeyChord([mod], "w", [
    #     Key([], "h", lazy.layout.shuffle_left()),
    #     Key([], "l", lazy.layout.shuffle_right()),
    #     Key([], "j", lazy.layout.shuffle_down()),
    #     Key([], "k", lazy.layout.shuffle_up()),
    #     Key([], "w", lazy.ungrab_chord()()),
    #     Key([mod], "w", lazy.ungrab_chord()()),
    #     Key([mod], "h", lazy.layout.shuffle_left()),
    #     Key([mod], "l", lazy.layout.shuffle_right()),
    #     Key([mod], "j", lazy.layout.shuffle_down()),
    #     Key([mod], "k", lazy.layout.shuffle_up()),
    #     Key([mod], "w", lazy.ungrab_chord()())],
    #     mode = "Move windows"),

    Key([mod, "shift"], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key([mod, "shift"], "q", lazy.spawn("shutdown -h now"), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="from/to floating"),

    Key(['mod4'], 'p', lazy.run_extension(extension.DmenuRun(
        dmenu_bottom = True,
        dmenu_font="JetBrainsMonoMedium Nerd Font-13",
        background="#282c34",
        foreground="#fcfcfc",
        selected_background="#5c6667",
        selected_foreground="#fcfcfc",
        dmenu_ignorecase = True,
        dmenu_prompt = "dmenu",
    ))),
    # Key([],"XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), desc="Volume"),
    # Key([],"XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), desc="Volume"),
    # Key([],"XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Volume"),
    # Key([],"XF86AudioMicMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Volume"),
    Key([],"XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+"), desc="Volume"),
    Key([],"XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-"), desc="Volume"),
    Key([],"XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="Volume"),
    Key([],"XF86AudioMicMute", lazy.spawn("amixer set Master toggle"), desc="Volume"),
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
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(margin = 10, border_focus = "#fcfcfc", border_normal = "#282c34", border_width = 3, cange_ratio = 0.05, max_ratio = 0.9, min_ratio  = 0.1, single_border_width = 0, single_margin = 0),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrainsMono NF",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # wallpaper = '/home/nikita/.local/share/backgrounds/wave-dark-arch.png',
        # wallpaper_mode = 'fill',
        top = bar.Gap(34),
        # top=bar.Bar(
        #     [
        #         widget.CurrentLayout(),
        #         widget.GroupBox(),
        #         widget.Prompt(),
        #         widget.WindowName(),
        #         widget.BatteryIcon(),
        #         widget.Battery(update_interval = 2, font = 'JetBrainsMono NF',
        #                         unknown_char='', charge_char = '', 
        #                         discharge_char = '',
        #                         format = '{char} {percent:2.0%}'),
        #         widget.Clock(format="%H:%M:%S"),
        #     ],
        #     30,
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
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width = 0
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
