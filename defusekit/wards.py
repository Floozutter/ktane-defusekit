"""
Common helper functions for working with curses windows.
"""

import curses
from defusekit.kittypes import Window


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
