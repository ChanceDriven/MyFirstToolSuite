#Live Run 2.0!
import interface
import tools
import time


start = time.time()

interface.greet()

while True:
    #startmenu will have an exit value, if false then re-call
    if interface.stmn(start):
        break
