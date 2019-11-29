import curses
from .. import wards

def run(scr):
    wards.stdsetup(scr)
    scr.addstr("This is a dummy module!\n\n")
    scr.addstr("Press any key to exit.", curses.color_pair(3))
    scr.getch()
