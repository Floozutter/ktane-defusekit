import curses
from defusekit import wards
from enum import Emum


class Color(Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    YELLOW = 3
    BLUE = 4

def get_instruction(wires, is_even):
    if len(wires) == 3:
        if all(w is not Color.RED for w in wires):
            return "Cut the second wire"
        elif wires[-1] is Color.WHITE:
            return "Cut the last wire"
        elif sum(1 for w in wires if w is Color.BLUE) > 1):
            return "Cut the last blue wire"
        else:
            return "Cut the last wire"
    elif len(wires) == 4:
        pass
    elif len(wires) == 5:
        pass
    elif len(wires) == 6:
        pass
    else:
        raise ValueError("number of wires is not within [3, 6]")  

def run(scr):
    return
