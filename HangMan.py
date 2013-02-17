#My version of the hangman generator
import random

def noosegen(x):
    line1 = "______   \n"
    line2 = "|     |   \n"
    line3 = "|        \n"
    line4 = "|        \n"
    line5 = "|        \n"
    line6 = "|\n"
    line7 = "|------|\n"
    line8 = "|______|"
    

    if x > 0:
        line3 = line3[0:6] + "O" + line3[7:]
    if x > 1:
        line4 = line4[0:5] + "/" + line4[6:]
    if x > 2:
        line4 = line4[0:6] + "|" + line4[7:]
    if x > 3:
        line4 = line4[0:7] + "\\" + line4[8:]
    if x > 4:
        line5 = line5[0:5] + "/" + line5[6:]
    if x > 5:
        line5 = line5[0:7] + "\\" + line5[8:]

    lines = line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8

    print( lines )
    
def getclue(type):
    if not type == "own":
        file = open("C:/Clues.txt")
        cluelist = file.readlines()
        file.close
        size = len(cluelist)
        while True:         #continuously tries to grab a clue from file
            line = random.randint(0, size - 1)
            if type == "clean":
                if cluelist[line][0] == '@':
                    return cluelist[line][1:]
            else:
                if cluelist[line][0] == '#':
                    return cluelist[line][1:]
    print("What would you like to the clue to be?\n>>> ")
    while True:
        n = input()
        i =0
        badclue = False
        if len(n) < 5:
            print("Please choose a longer clue\n>>> ")
        else:
            while i < len(n):
                if not n[i].isalpha() or n[i] != " ":
                    print("Please use only letters and spaces")
                    badclue = True
                    break
                i += 1
            if not badclue:
                return n
            break

def getguess(letterlist):
    while True:
        k = input("\n>>> ")
        if (len(k) > 1) or (not k.isalpha()):
            print("Not a valid guess")
        elif k.upper() in letterlist:
            print("This has already been guessed")
        else:
            letterlist[ord(k.lower())-97] = k.upper()
            return k.lower()







while True:       # Game loop
    print("Welcome to HangMan!")
    print("Would you like to play a clean game,\ndirty one, or input your own clue?")
    win = False
    while True:             # First input loop
        n = input(">>> ")
        if "ean" in n:
            n = "clean"
            break
        elif "irty" in n:
            n = "dirty"
            break
        elif "lue" in n:
            n = "own"
            break
        else:
            print("That doesn't seem to be an option")
    clue = getclue(n)
    wrong = 0
    letterlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while wrong < 6:
        noosegen(wrong)
        print("\n")
        i = 0
        board = []
        while i < len(clue):
            if clue[i] == " ":
                board.append("  ")
            elif clue[i].upper() in letterlist:
                board.append(clue[i] + " ")
            else:
                board.append("_ ")
            i += 1
        i = 0
        while i < len(board):
            print(board[i], end = "")
            i += 1
        print("\n" * 2)
        if not "_ " in board:
            print("You won!" + "\n" * 5)
            win = True
            break
        guess = getguess(letterlist)
        print(letterlist)
        if not guess.upper() in clue.upper():
            wrong += 1

    if not win:        
        noosegen(6)
        print("You lost!" + "\n" * 5)
        
        
        
