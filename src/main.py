import curses
import wards

MODULE_NAMES = [
    "test apple",
    "test banana",
    "quiz"
    ]

def dummy(scr):
    print("Test!")

def menu(scr):
    def print_welcome():
        scr.addstr("Hi, welcome to ")
        scr.addstr("ktane-defusekit", curses.color_pair(2))
        scr.addstr("!\n", curses.color_pair(0))
        scr.addstr("This is an interactive bomb defusal manual ")
        scr.addstr("for Keep Talking and Nobody Explodes.")
        scr.addstr("\n\n")

    def print_controls():
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

    def setup_modulelist():
        module_xys = []
        scr.addstr("Available Modules:")
        for i, name in enumerate(MODULE_NAMES):
            scr.addstr("\n")
            scr.addstr((str(i) + ") ").rjust(6))
            scr.addstr(name, curses.color_pair(6))
            module_xys.append(scr.getyx())
        scr.addstr("\n\n")
        return module_xys

    def update_modulelist(module_xys, selectindex):
        for i, pos in enumerate(module_xys):
            scr.move(pos[0], pos[1])
            scr.clrtoeol()
            if i == selectindex:
                scr.addstr("  <--", curses.color_pair(2))

    def setup_inputbox():
        scr.addstr(">>> ", curses.color_pair(2))
        return scr.getyx()

    def update_inputbox(inputbox_xy, inputstring, valid):
        scr.move(inputbox_xy[0], inputbox_xy[1])
        scr.clrtoeol()
        clr = curses.color_pair(0)
        if valid:
            clr = curses.color_pair(6)
        scr.addstr(inputstring, clr)

    def inputloop(module_xys, inputbox_xy):
        selectindex = None
        inputstring = ""
        valid = False
        while True:
            # Handle user input
            c = scr.getch()
            #print(c)
            if c == 27:     # Esc
                return None
            elif c == 10:   # Enter
                if valid:
                    return dummy
            elif c in (258, 259):  # Down, Up
                if selectindex is None:
                    selectindex = 0
                elif c == 258:
                    selectindex += 1
                else:  # c == 259
                    selectindex -= 1
                selectindex = selectindex % len(module_xys)
                inputstring = MODULE_NAMES[selectindex]
            elif c == 9:    # Tab
                pass
            elif c == 21:   # Ctrl-U
                inputstring = ""
            elif c == 8:    # Backspace
                inputstring = inputstring[:-1]
            elif 32 <= c <= 126:  # Printable
                inputstring += str(chr(c))
            valid = bool(inputstring in MODULE_NAMES)
            # Update select arrow on module list
            update_modulelist(module_xys, selectindex)
            # Update user input box
            update_inputbox(inputbox_xy, inputstring, valid)
        
    
    # Standard setup
    wards.stdsetup(scr)
    
    # Display welcome message
    print_welcome()

    # Display controls help using list
    print_controls()

    # Display modules using list
    module_xys = setup_modulelist()

    # Setup user input box
    inputbox_xy = setup_inputbox()
    
    # Input loop and get module function
    return inputloop(module_xys, inputbox_xy)


def menu_selectloop(stdscr):
    while True:
        modulefunc = menu(stdscr)
        if modulefunc is None:
            break
        modulefunc(stdscr)

def main():
    curses.wrapper(menu_selectloop)
    
if __name__ == "__main__":
    main()
