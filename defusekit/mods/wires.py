import curses
from defusekit import wards
from enum import Enum


class Color(Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 3
    BLUE = 4

def get_instruction(wires, is_odd):
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

def run(scr):
    wards.stdsetup(scr)
    scr.addstr("This module is not yet completed!\n\n", curses.color_pair(0))
    scr.addstr("Press any key to exit.", curses.color_pair(3))
    scr.getch()
