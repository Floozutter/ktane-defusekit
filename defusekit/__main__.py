"""
The main menu and entry point for the kit's modules.
"""

import curses
from defusekit import wards
from defusekit import autocomplete

from defusekit.mods import dummy
from defusekit.mods import wires
from defusekit.mods import complicatedwires

from defusekit.cursetypes import Window, Coord
from typing import Any, Callable, Dict, List, Tuple


KitProcedure = Callable[[Any], None]

MODULES: Dict[str, KitProcedure] = {
    "dummy" : dummy.run,
    "wires" : wires.run,
    "complicated-wires" : complicatedwires.run
}


def menu(scr: Window) -> KitProcedure:
    def print_welcome() -> None:
        scr.addstr("Hi, welcome to ")
        scr.addstr("ktane-defusekit", curses.color_pair(2))
        scr.addstr("!\n", curses.color_pair(0))
        scr.addstr("This is an interactive bomb defusal manual ")
        scr.addstr("for Keep Talking and Nobody Explodes.")
        scr.addstr("\n\n")

    def print_controls() -> None:
        scr.addstr("Controls:")
        controls = [
            ("ESC", "Quit the program."),
            ("UP, DOWN", "Navigate the module list."),
            ("[type]", "Type module name into text prompt."),
            ("TAB", "Autocomplete module name."),
            ("ENTER", "Select module to run.")
        ]
        for pair in controls:
            scr.addstr("\n")
            scr.addstr("- ".rjust(6))
            scr.addstr(pair[0].ljust(10), curses.color_pair(3))
            scr.addstr(": " + pair[1], curses.color_pair(0))
        scr.addstr("\n\n")

    def setup_modulelist() -> List[Coord]:
        module_xys = []
        scr.addstr("Available Modules:")
        for i, mod in enumerate(MODULES):
            scr.addstr("\n")
            scr.addstr((str(i) + ") ").rjust(6))
            scr.addstr(mod, curses.color_pair(6))
            module_xys.append(scr.getyx())
        scr.addstr("\n\n")
        return module_xys

    def update_modulelist(module_xys: List[Coord], selectindex: int) -> None:
        for i, pos in enumerate(module_xys):
            scr.move(pos[0], pos[1])
            scr.clrtoeol()
            if i == selectindex:
                scr.addstr("  <--", curses.color_pair(2))

    def setup_inputbox() -> Coord:
        scr.addstr(">>> ", curses.color_pair(2))
        return scr.getyx()

    def update_inputbox(inputbox_xy: Coord, inputstring: str, valid: bool):
        scr.move(inputbox_xy[0], inputbox_xy[1])
        scr.clrtoeol()
        clr = curses.color_pair(0)
        if valid:
            clr = curses.color_pair(6)
        scr.addstr(inputstring, clr)

    def inputloop(module_xys: List[Coord], inputbox_xy: Coord):
        selectindex = None
        inputstring = ""
        valid = False
        while True:
            c = scr.getch()
            if c == 27:     # Esc
                return None
            elif c == 10 and valid:   # Enter
                return MODULES[inputstring]
            elif c in (258, 259):  # Down, Up
                if selectindex is None:
                    selectindex = 0
                elif c == 258:
                    selectindex += 1
                else:  # c == 259
                    selectindex -= 1
                selectindex = selectindex % len(module_xys)
                inputstring = list(MODULES.keys())[selectindex]
            elif c == 9:    # Tab
                prediction = autocomplete.predict(
                    MODULES.keys(),
                    inputstring
                )
                if prediction is not None:
                    inputstring = prediction
            elif c == 21:   # Ctrl-U
                inputstring = ""
            elif c == 8:    # Backspace
                inputstring = inputstring[:-1]
            elif 32 <= c <= 126:  # Printable
                inputstring += str(chr(c))
            valid = bool(inputstring in MODULES)
            # Update select arrow on module list
            update_modulelist(module_xys, selectindex)
            # Update user input box
            update_inputbox(inputbox_xy, inputstring, valid)
    
    wards.stdsetup(scr)
    print_welcome()
    print_controls()
    module_xys = setup_modulelist()
    inputbox_xy = setup_inputbox()
    
    return inputloop(module_xys, inputbox_xy)


def selectloop(scr: Window) -> None:
    while True:
        kitproc = menu(scr)
        if kitproc is None:
            break
        kitproc(scr)
    
    
if __name__ == "__main__":
    curses.wrapper(selectloop)
