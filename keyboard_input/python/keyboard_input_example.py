import curses
import time

# Initialize the terminal
win = curses.initscr()

# Turn off line buffering
curses.cbreak()


# Make getch() non-blocking
win.nodelay(True)

while True:
    key = win.getch()
    if key != -1:
        print('Pressed key', key)
    time.sleep(0.01)
