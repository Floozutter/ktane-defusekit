"""
Types for the defusekit.
"""

import curses
from typing import Any, Callable, Tuple, Dict


# Types for curses.
Window = curses.window   # curses window
Coord = Tuple[int, int]  # row, col coordinate

# Types for menu logic.
KitProcedure = Callable[[Window], None]  # entry point to a kit module
Kitalogue = Dict[str, KitProcedure]  # named collection of module entry points
