"""
Types for the defusekit.
"""

import curses
from typing import Any, Callable, Tuple, Dict


# Types for curses.
Window = Any             # mypy doesn't like curses.window
Coord = Tuple[int, int]  # row, col coordinate

# Types for menu logic.
KitProcedure = Callable[[Window], None]  # entry point to a kit module
Kitalogue = Dict[str, KitProcedure]  # collection of named module entry points
