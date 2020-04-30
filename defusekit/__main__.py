"""
Entry point to the defusekit's main menu.
"""

import curses
from defusekit.mainmenu import menu

from defusekit.mods import dummy
from defusekit.mods import wires
from defusekit.mods import complicatedwires

from defusekit.kittypes import Window, KitProcedure, Kitalogue
from typing import Optional


MODULES: Kitalogue = {
    dummy.NAME : dummy.main,
    wires.NAME : wires.main,
    complicatedwires.NAME : complicatedwires.main
}


def main(scr: Window) -> None:
    """Enters defusekit modules as returned by the main menu."""
    kitproc: Optional[KitProcedure]
    while True:
        kitproc = menu(scr, MODULES)
        if kitproc is not None: kitproc(scr)
        else:                   break
    
    
if __name__ == "__main__":
    curses.wrapper(main)
