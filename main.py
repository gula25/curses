import curses

screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_WHITE)

for i in range(6):

    # Update the buffer, adding text at different locations
    screen.addstr(0, 0, "This string gets printed at position (0, 0)")
    screen.addstr(3, 1, "Try Russian text", curses.color_pair(1))  # Python 3 required for unicode
    screen.addstr(4, 4, str(i))
    screen.addch(5, 5, "Y")

    # Changes go in to the screen buffer and only get
    # displayed after calling `refresh()` to update
    screen.refresh()

    curses.napms(1000)

curses.nocbreak()
#stdscr.keypad(False)
curses.echo()

curses.endwin()