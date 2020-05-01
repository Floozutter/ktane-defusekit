"""
Entry point to the defusekit's main menu.
"""

import curses
from defusekit.mainmenu import menu

from defusekit.mods import dummy
from defusekit.mods import wires
from defusekit.mods import complicatedwires

from defusekit.kittypes import Window, KitProcedure, Kitalogue
from types import ModuleType
from typing import Optional, Iterable


def kitalogue(modules: Iterable[ModuleType]) -> Kitalogue:
    """Makes a Kitalogue out of Python modules. (The name's a verb.)"""
    return dict((mod.NAME, mod.main) for mod in modules)

# Note: The name MODULES refers to KTaNE modules, not Python modules.
MODULES: Kitalogue = kitalogue((
    dummy,
    wires,
    complicatedwires
))


def main(scr: Window) -> None:
    """Enters defusekit modules as returned by the main menu."""
    kitproc: Optional[KitProcedure]
    while True:
        kitproc = menu(scr, MODULES)
        if kitproc is not None: kitproc(scr)
        else:                   break
    
    
if __name__ == "__main__":
    curses.wrapper(main)
