"""
The main menu for selecting defusekit modules.
"""

import curses
from defusekit import wards
from defusekit import autocomplete

from defusekit.kittypes import Window, Coord, KitProcedure, Kitalogue
from typing import Optional


def menu(scr: Window, modules: Kitalogue) -> Optional[KitProcedure]:
    # Standard setup.
    wards.setup(scr)

    # Print a welcome message.
    scr.addstr("Hi, welcome to ")
    scr.addstr("ktane-defusekit", curses.color_pair(2))
    scr.addstr("!\n", curses.color_pair(0))
    scr.addstr("This is an interactive bomb defusal manual ")
    scr.addstr("for Keep Talking and Nobody Explodes.")
    scr.addstr("\n\n")

    # Print the controls.
    wards.print_controls(scr, (
        ("ESC", "Quit the program."),
        ("UP, DOWN", "Navigate the module list."),
        ("[type]", "Type module name into text prompt."),
        ("TAB", "Autocomplete module name."),
        ("ENTER", "Select module to run.")
    ))

    # Print modules, and store their coordinates for later use.
    module_coords: List[Coord] = []  # coords for updating selection cursor
    scr.addstr("Available Modules:")
    for i, mod in enumerate(modules):
        scr.addstr("\n")
        scr.addstr((str(i) + ") ").rjust(6))
        scr.addstr(mod, curses.color_pair(6))
        module_coords.append(scr.getyx())
    scr.addstr("\n\n")

    def update_cursor(selectindex: int) -> None:
        for i, pos in enumerate(module_coords):
            scr.move(pos[0], pos[1])
            scr.clrtoeol()
            if i == selectindex:
                scr.addstr("  <--", curses.color_pair(2))

    # Print the inputbox, and store its coordinate.
    scr.addstr(">>> ", curses.color_pair(2))
    inputbox_coord = scr.getyx()  # coord for updating input text

    def update_inputbox(inputstring: str, valid: bool):
        scr.move(inputbox_coord[0], inputbox_coord[1])
        scr.clrtoeol()
        clr = curses.color_pair(0)
        if valid:
            clr = curses.color_pair(6)
        scr.addstr(inputstring, clr)

    # Enter the input loop.
    selectindex = None
    inputstring = ""
    valid = False
    while True:
        c = scr.getch()
        if c == 27:  # Esc
            return None
        elif c == 10 and valid:  # Enter
            return modules[inputstring]
        elif c in (258, 259):  # Down, Up
            if selectindex is None: selectindex  = 0  # Initial
            elif c == 258:          selectindex += 1  # Down
            else:                   selectindex -= 1  # Up
            selectindex = selectindex % len(module_coords)
            inputstring = list(modules.keys())[selectindex]
        elif c == 9:  # Tab
            pred = autocomplete.predict(modules.keys(), inputstring)
            if pred is not None:
                inputstring = pred
        elif c == 21:  # Ctrl-U
            inputstring = ""
        elif c == 8:  # Backspace
            inputstring = inputstring[:-1]
        elif 32 <= c <= 126:  # Printable
            inputstring += str(chr(c))
        valid = bool(inputstring in modules)
        # Update select arrow on module list
        update_cursor(selectindex)
        # Update user input box
        update_inputbox(inputstring, valid)
