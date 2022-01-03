# Qtile based on Derek Taylor config
# https://gitlab.com/dwt1/dotfiles

# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401

from gruvbox.gruvbox import *
from theme import *

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice

# variables
defaultFont = "Mononoki Nerd Font"
colors = [[background, background], # panel background
          [black0, black0], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          [aqua0, aqua0], # border line color for 'other tabs' and color for 'odd widgets'
          ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
          [aqua, aqua], # window name
          [aqua0, aqua0], # backbround for inactive screens
          [yellow, yellow],
          [yellow0, yellow0],
          [green, green]]


# Functions
def separator(lwidth, pad, fg, bg):
    return widget.Sep(
            linewidth = lwidth,
            padding = pad,
            foreground = fg,
            background = bg
        )

def text_box(txt, bg, fg, pad, fsize, cb = {}):
    return widget.TextBox(
            text = txt,
            background = bg,
            foreground = fg,
            padding = pad,
            fontsize = fsize,
            mouse_callbacks = cb
        )


keys = [
        ### The essentials
        Key([mod], "Return",
            lazy.spawn(myTerm+" -e fish"),
            desc='Launches My Terminal'
            ),
        Key([mod], "Tab",
            lazy.next_layout(),
            desc='Toggle through layouts'
            ),
        Key([mod, "shift"], "c",
            lazy.window.kill(),
            desc='Kill active window'
            ),
        Key([mod, "shift"], "r",
            lazy.restart(),
            desc='Restart Qtile'
            ),
        Key([mod, "shift"], "q",
            lazy.shutdown(),
            desc='Shutdown Qtile'
            ),
        ### Switch focus to specific monitor (out of three)
        Key([mod], "w",
            lazy.to_screen(0),
            desc='Keyboard focus to monitor 1'
            ),
        Key([mod], "e",
            lazy.to_screen(1),
            desc='Keyboard focus to monitor 2'
            ),
        ### Switch focus of monitors
        Key([mod], "period",
            lazy.next_screen(),
            desc='Move focus to next monitor'
            ),
        Key([mod], "comma",
            lazy.prev_screen(),
            desc='Move focus to prev monitor'
            ),
        ### Treetab controls
        Key([mod, "shift"], "h",
            lazy.layout.move_left(),
            desc='Move up a section in treetab'
            ),
        Key([mod, "shift"], "l",
            lazy.layout.move_right(),
            desc='Move down a section in treetab'
            ),
        ### Window controls
        Key([mod], "j",
            lazy.layout.down(),
            desc='Move focus down in current stack pane'
            ),
        Key([mod], "k",
            lazy.layout.up(),
            desc='Move focus up in current stack pane'
            ),
        Key([mod, "shift"], "j",
            lazy.layout.shuffle_down(),
            lazy.layout.section_down(),
            desc='Move windows down in current stack'
            ),
        Key([mod, "shift"], "k",
            lazy.layout.shuffle_up(),
            lazy.layout.section_up(),
            desc='Move windows up in current stack'
            ),
        Key([mod], "h",
            lazy.layout.shrink(),
            lazy.layout.decrease_nmaster(),
            desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
            ),
        Key([mod], "l",
            lazy.layout.grow(),
            lazy.layout.increase_nmaster(),
            desc='Expand window (MonadTall), increase number in master pane (Tile)'
            ),
        Key([mod], "n",
            lazy.layout.normalize(),
            desc='normalize window size ratios'
            ),
        Key([mod], "m",
            lazy.layout.maximize(),
            desc='toggle window between minimum and maximum sizes'
            ),
        Key([mod, "shift"], "f",
            lazy.window.toggle_floating(),
            desc='toggle floating'
            ),
        Key([mod], "f",
            lazy.window.toggle_fullscreen(),
            desc='toggle fullscreen'
            ),
        ### Stack controls
        Key([mod, "shift"], "Tab",
            lazy.layout.rotate(),
            lazy.layout.flip(),
            desc='Switch which side main pane occupies (XmonadTall)'
            ),
        Key([mod], "space",
            lazy.layout.next(),
            desc='Switch window focus to other pane(s) of stack'
            ),
        Key([mod, "shift"], "space",
            lazy.layout.toggle_split(),
            desc='Toggle between split and unsplit sides of stack'
            ),
        Key([mod, "shift"], "m",
        lazy.spawn("rofi -show drun"),
        desc="Launch menu"
        ),
        # Valume control lower
        Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
        Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

        # Brightness
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

        # Printscreens
        Key([mod], "s", lazy.spawn("scrot")),
        Key([mod, "shift"], "s", lazy.spawn("scrot -s")),
    ]

groups = [
    Group("", layout='monadtall'),
    Group("", layout='monadtall'),
    Group("", layout='monadtall'),
    Group("", layout='monadtall'),
    Group("嗢", layout='monadtall'),
    Group("ﱮ", layout='monadtall'),
]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 5,
                "border_focus": yellow,
                "border_normal": "#1D2330"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font = "Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background = colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    return [
            separator(0, 6, colors[2], colors[0]),
            text_box('', colors[0], colors[5], 0, 25, {'Button1': lambda: qtile.cmd_spawn(myTerm)}),
            separator(0, 6, colors[2], colors[0]),
            widget.GroupBox(
                font = "Ubuntu Bold",
                fontsize = 20,
                margin_y = 3,
                margin_x = 0,
                padding_y = 5,
                padding_x = 5,
                borderwidth = 3,
                active = colors[2],
                inactive = colors[8],
                rounded = False,
                highlight_color = colors[1],
                highlight_method = "line",
                this_current_screen_border = colors[9],
                this_screen_border = colors [8],
                other_current_screen_border = colors[9],
                other_screen_border = colors[8],
                foreground = colors[2],
                background = colors[0]
            ),
            widget.Prompt(
                prompt = prompt,
                font = "Ubuntu Mono",
                padding = 10,
                foreground = colors[3],
                background = colors[1]
            ),
            separator(0, 40, colors[2], colors[0]),
            widget.WindowName(
                foreground = colors[6],
                background = colors[0],
                padding = 0
            ),
            separator(0, 6, colors[0], colors[0]),
            text_box('', colors[0], colors[5], 0, 37),
            widget.Net(
                interface = "wlan0",
                format = '{down} ↓↑ {up}',
                foreground = colors[2],
                background = colors[5],
                padding = 5
            ),
            text_box('', colors[5], colors[10], 0, 37),
            text_box('🌡', colors[10], colors[2], 2, 12),
            widget.ThermalSensor(
                foreground = colors[2],
                background = colors[10],
                threshold = 90,
                padding = 5,
                tag_sensor = 'coretemp-isa-0000'
            ),
            text_box('', colors[10], colors[5], 0, 37),
            text_box(' ', colors[5], colors[2], 2, 18),
            widget.CheckUpdates(
                update_interval = 1800,
                distro = "Arch_checkupdates",
                display_format = "{updates} Updates",
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                foreground = colors[2],
                background = colors[5]
            ),
            text_box('', colors[5], colors[10], 0, 37),
            text_box('', colors[10], colors[2], 0, 20),
            widget.Memory(
                foreground = colors[2],
                background = colors[10],
                mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                padding = 5
            ),
            text_box('', colors[10], colors[5], 0, 37),
            text_box('', colors[5], colors[2], 0, 12),
            widget.Battery(
                background = colors[5],
                foreground = colors[2],
                low_percentage=0.20,
                low_foreground='fa5e5b',
                update_delay=10,
                format='{percent:.0%} {hour:d}:{min:02d} ' '{watt:.2}W'
            ),
            text_box('', colors[5], colors[10], 0, 37),
            widget.CurrentLayoutIcon(
                custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                foreground = colors[0],
                background = colors[10],
                padding = 0,
                scale = 0.7
            ),
            widget.CurrentLayout(
                foreground = colors[2],
                background = colors[10],
                padding = 5
            ),
            text_box('', colors[10], colors[5], 0, 37),
            widget.Clock(
                foreground = colors[2],
                background = colors[5],
                format = "%A, %B %d - %H:%M "
            ),
            widget.Systray(
                background = colors[0],
                padding = 5
            )
        ]

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]            # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))
        ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
