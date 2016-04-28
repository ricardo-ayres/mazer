#!/bin/env python2
import termios
import fcntl
import sys
import os
import mazer.py

def main():
    # Terminal Setup for getting keystrokes.
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    
    # Main program setup here.
    
    maze = maze()
    player = player()

    try:
        # main program loop.
        while 1:
            command = get_keypress()
            player.do(command)
            maze.print_view(player.position)
    finally:
        # Cleaning up before exiting.
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)



#### Entry Point ####
if __name__ == "__main__":
    main()
