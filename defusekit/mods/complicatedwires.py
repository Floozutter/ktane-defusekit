NAME = "complicated-wires"

import curses
from defusekit import wards

from defusekit.kittypes import Window


def get_instruction(red: bool, blue: bool, star: bool, led: bool) -> str:
    binstr = "".join(["1" if b else "0" for b in (red, blue, star, led)])
    wirestate = int(binstr, 2)
    C = "Cut the wire"
    D = "Do not cut the wire"
    S = "Cut the wire if serial number's last digit is even"
    P = "Cut the wire if the bomb has a parallel port"
    B = "Cut the wire if the bomb has 2 or more batteries"
    INSTRUCTIONS = {
        0b0000 : C,
        0b0001 : D,
        0b0010 : C,
        0b0011 : B,
        0b0100 : S,
        0b0101 : P,
        0b0110 : D,
        0b0111 : P,
        0b1000 : S,
        0b1001 : B,
        0b1010 : C,
        0b1011 : B,
        0b1100 : S,
        0b1101 : S,
        0b1110 : P,
        0b1111 : D
        }
    return INSTRUCTIONS[wirestate]
        

def main(scr: Window):
    wards.setup(scr)
    wards.print_modulename(scr, NAME)
    wards.print_controls(scr, (
        ("ESC", "Quit the module."),
        ("Q/W/E/R", "Toggle wire options."),
        ("TAB", "Reset all wire options to NO.")
    ))

    scr.addstr("Wire Settings:", curses.color_pair(0))
    setting_keys = ("Q", "W", "E", "R")
    setting_labels = (
        "Has Red coloring",
        "Has Blue coloring",
        "Has Star symbol",
        "Has LED lit"
        )
    setting_states = [False, False, False, False]
    setting_yxs = []
    for i in range(4):
        scr.addstr("\n")
        scr.addstr((setting_keys[i]+" - ").rjust(6))
        scr.addstr(setting_labels[i].ljust(18), curses.color_pair(0))
        scr.addstr(": ", curses.color_pair(0))
        setting_yxs.append(scr.getyx())
    scr.addstr("\n\n")

    scr.addstr("Instruction: ")
    instruction_yx = scr.getyx()
    while True:
        # Show setting states
        for i in range(4):
            scr.move(setting_yxs[i][0], setting_yxs[i][1])
            scr.clrtoeol()
            if setting_states[i]:
                scr.addstr("YES", curses.color_pair(2))
            else:
                scr.addstr("NO", curses.color_pair(1))
        # Show instruction
        scr.move(instruction_yx[0], instruction_yx[1])
        scr.clrtoeol()
        scr.addstr(get_instruction(
            setting_states[0],
            setting_states[1],
            setting_states[2],
            setting_states[3]
            ))
        # Get input
        c = scr.getch()
        if c == 27:   # Esc
            return
        elif c == 9:  # Tab
            setting_states = [False, False, False, False]
        elif c in (81, 113):  # Q
            setting_states[0] = not setting_states[0]
        elif c in (87, 119):  # W
            setting_states[1] = not setting_states[1]
        elif c in (69, 101):  # E
            setting_states[2] = not setting_states[2]
        elif c in (82, 114):  # R
            setting_states[3] = not setting_states[3]
