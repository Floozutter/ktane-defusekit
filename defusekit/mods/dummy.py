NAME = "dummy"

import curses
from defusekit import wards

from defusekit.kittypes import Window


def main(scr: Window):
    wards.setup(scr)
    wards.print_modulename(scr, NAME)
    scr.addstr("This is a dummy module!\n\n", curses.color_pair(0))
    scr.addstr("Press any key to exit.", curses.color_pair(3))
    scr.getch()
