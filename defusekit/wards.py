"""
Common helper functions for working with curses windows.
"""

import curses
from defusekit.kittypes import Window
from typing import Iterable, Tuple


def stdcolors() -> None:
    """
    Sets the standard window colors.
    """
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)

def stdsetup(scr: Window) -> None:
    """
    Standard procedure for window setup.
    """
    scr.clear()  # clear the window
    stdcolors()  # set colors


def print_controls(scr: Window, controls: Iterable[Tuple[str, str]]):
    scr.addstr("Controls:", curses.color_pair(0))
    maxkeysize = max(map(len, next(zip(*controls))))
    for key, action in controls:
        scr.addstr("\n")
        scr.addstr("- ".rjust(6))
        scr.addstr(key.ljust(maxkeysize + 1), curses.color_pair(3))
        scr.addstr(": " + action, curses.color_pair(0))
    scr.addstr("\n\n", curses.color_pair(0))
