import curses
from defusekit import wards

from enum import Enum
from defusekit.kittypes import Window
from typing import List


class Color(Enum):
    WHITE = 1
    BLACK = 2
    RED = 3
    YELLOW = 4
    BLUE = 5


def get_instruction(wires: List[Color], is_odd: bool) -> str:
    if len(wires) == 3:
        if wires.count(Color.RED) == 0:
            return "Cut the second wire"
        elif wires[-1] is Color.WHITE:
            return "Cut the last wire"
        elif wires.count(Color.BLUE) > 1:
            return "Cut the last blue wire"
        else:
            return "Cut the last wire"
    elif len(wires) == 4:
        if is_odd and (wires.count(Color.RED) > 1):
            return "Cut the last red wire"
        elif (wires[-1] is Color.YELLOW) and \
             (wires.count(Color.RED) == 0):
            return "Cut the first wire"
        elif wires.count(Color.BLUE) == 1:
            return "Cut the first wire"
        elif wires.count(Color.YELLOW) > 1:
            return "Cut the last wire"
        else:
            return "Cut the last wire"
    elif len(wires) == 5:
        if is_odd and (wires[-1] is Color.BLACK):
            return "Cut the fourth wire"
        elif (wires.count(Color.RED) == 1) and \
             (wires.count(Color.YELLOW) > 1):
            return "Cut the first wire"
        elif wires.count(Color.BLACK) == 0:
            return "Cut the second wire"
        else:
            return "Cut the first wire"
    elif len(wires) == 6:
        if is_odd and (wires.count(Color.YELLOW) == 0):
            return "Cut the third wire"
        elif (wires.count(Color.YELLOW) == 1) and \
             (wires.count(Color.WHITE) > 1):
            return "Cut the fourth wire"
        elif wires.count(Color.RED) == 0:
            return "Cut the last wire"
        else:
            return "Cut the fourth wire"
    else:
        raise ValueError("number of wires is not within [3, 6]")  


def run(scr: Window):
    wards.stdsetup(scr)
    scr.addstr("Module: ", curses.color_pair(0))
    scr.addstr("wires\n\n", curses.color_pair(6))

    scr.addstr("Controls", curses.color_pair(0))
    controls = (
        ("ESC", "Quit the module."),
        ("[1, 5]", "Add wire of corresponding color."),
        ("TAB", "Reset.")
        )
    for pair in controls:
        scr.addstr("\n")
        scr.addstr("- ".rjust(6))
        scr.addstr(pair[0].ljust(8), curses.color_pair(3))
        scr.addstr(": " + pair[1], curses.color_pair(0))
    scr.addstr("\n\n")

    scr.addstr("This module is not yet completed!\n\n", curses.color_pair(0))
    scr.addstr("Press any key to exit.", curses.color_pair(3))
    scr.getch()
