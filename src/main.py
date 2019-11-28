import curses
import wards

MODULE_NAMES = [
    "test apple",
    "test banana",
    "quiz"
    ]

def dummy(stdscr):
    print("Test!")

def menu(stdscr):
    # Standard setup
    wards.stdsetup(stdscr)
    
    # Display welcome message
    stdscr.move(0, 0)
    stdscr.addstr("Hi, welcome to ")
    stdscr.addstr("ktane-defusekit", curses.color_pair(2))
    stdscr.addstr("!\n", curses.color_pair(0))
    stdscr.addstr("This is an interactive bomb defusal manual ")
    stdscr.addstr("for Keep Talking and Nobody Explodes.")

    # Display control help using list
    stdscr.move(3, 0)
    control_pairs = [
        ("ESC", "Quit the program."),
        ("UP, DOWN", "Navigate the module list."),
        ("[type]", "Type module name into text prompt."),
        ("TAB", "Autocomplete module name."),
        ("ENTER", "Select module to run.")
        ]
    stdscr.addstr("Controls:\n")
    for i, pair in enumerate(control_pairs):
        stdscr.move(3+1 + i, 0)
        stdscr.addstr("- ".rjust(6))
        stdscr.addstr(pair[0].ljust(10), curses.color_pair(3))
        stdscr.addstr(": " + pair[1], curses.color_pair(0))
    
    # Display modules using list
    stdscr.move(10, 0)
    stdscr.addstr("Available Modules:")
    module_positions = []
    for i, name in enumerate(MODULE_NAMES):
        stdscr.move(10+1 + i, 0)
        stdscr.addstr((str(i) + ") ").rjust(6))
        stdscr.addstr(name, curses.color_pair(6))
        module_positions.append(stdscr.getyx())

    # Setup user input box
    stdscr.move(10 + len(MODULE_NAMES) + 3, 0)
    stdscr.addstr(">>> ", curses.color_pair(2))
    
    # Event loop
    selectindex = None
    inputstring = ""
    inputstring_color = curses.color_pair(0)
    valid_inputstring = False
    while True:
        # Handle user input
        c = stdscr.getch()
        #print(c)
        if c == 27:     # Esc
            break
        elif c == 10:   # Enter
            if valid_inputstring:
                return dummy
        elif c in (258, 259):  # Down, Up
            if selectindex is None:
                selectindex = 0
            else:
                if c == 258:
                    selectindex += 1
                else:
                    selectindex -= 1
            selectindex = selectindex % len(module_positions)
            inputstring = MODULE_NAMES[selectindex]
        elif c == 9:    # Tab
            pass
        elif c == 21:   # Ctrl-U
            inputstring = ""
        elif c == 8:    # Backspace
            inputstring = inputstring[:-1]
        elif 32 <= c <= 126:  # Printable
            inputstring += str(chr(c))
        valid_inputstring = inputstring in MODULE_NAMES
        # Update select arrow on module list
        for i, pos in enumerate(module_positions):
            stdscr.move(pos[0], pos[1])
            stdscr.clrtoeol()
            if i == selectindex:
                stdscr.addstr("  <--", curses.color_pair(2))
        # Update user input box
        stdscr.move(10 + len(MODULE_NAMES) + 3, 4)
        stdscr.clrtoeol()
        inputstring_color = curses.color_pair(0)
        if valid_inputstring:
            inputstring_color = curses.color_pair(6)
        stdscr.addstr(inputstring, inputstring_color)

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
