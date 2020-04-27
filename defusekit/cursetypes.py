"""
Types related to the curses module.
"""

import curses
from typing import Any, Callable, Tuple

Window = curses.window   # curses window
Coord = Tuple[int, int]  # row, col coordinate
