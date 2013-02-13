#This is my sonar game!!!
import time
import random
import sys

def generate_sea(height, width):
    waves = "~`"
    sea = ""
    i = 0
    while i < width / 10:
        sea += " " * 9 + str(i)
        i += 1
    sea += "\n" + " " * 3 + "0123456789" * int((width / 10)) + "\n"
    i = 0
    j = 0
    while i < height:
        if i < 10:
            sea += " "
        sea += str(i) + " "
        j = 0
        while j < width:
            r = random.randint(0, 1)
            sea += waves[r]
            j += 1
        sea += " " + str(i) + "\n"
        i += 1
    return sea

def chest_placer(height, width):
    chests = [0, 0, 0, 0, 0, 0]
    chests[0] = random.randint(0, width - 1)
    chests[1] = random.randint(0, height - 1)
    while True:
        chests[2] = random.randint(0, width - 1)
        chests[3] = random.randint(0, height - 1)
        if chests[0:2] != chests[2:4]:
            break
    while True:
        chests[4] = random.randint(0, width - 1)
        chests[5] = random.randint(0, height - 1)
        if chests[0:2] != chests[4:6] or chests[2:4] != chests[5:6]:
            break
    return chests

def distance(currentx, currenty, chest, lostchests):
    d = round(( (currentx - chest[(3 - lostchests) * 2]) ** 2 +  (currenty - chest[(3 - lostchests) * 2 + 1]) ** 2 ) ** .5, 0)
    return int(d)

def placesonar(sea, dist, sonarlist, height, width):
    clears = 1
    if dist == 0:
        clears = len(sonarlist) / 2
    i = 0
    l = len(sonarlist)
    while i < clears:
        x = sonarlist[l - i * 2 - 2]
        y = sonarlist[l - i * 2 - 1]
        position = (width + 4) * 2 + (width + 6) * y + x
        if y > 10:
            position += y - 10
        distplace = str(dist)
        if dist > 9 or dist == 0:
            distplace = 'O'
        sea = sea[:position] + distplace + sea[position + 1:]
        i += 1
    
    return sea

#Interface
def Sonar():
    intro = "Hello! So you want to play a game of Sonar..."
    i = 0
    while i < len(intro):
        print(intro[i], end = '')
        if i > 5:
            if intro[i] != " ":
                time.sleep(.07)
                sys.stdout.flush()
        i += 1
    sys.stdout.flush()
    
    print("")
    #This is the interface loop. This way the game can be start over
    while True:
        while True:
            try:
                n = int(input("How tall do you want the board to be?\n"))
                if n < 5:
                    n = int("Fail")
                if n > 20:
                    n = int("fail")
                if n % 5 != 0:
                    n = int("fail")
                break
            except ValueError:
                print("Please pick an integer between 5 and 20 that is divisble by 5")
    
        height = n
        print("\nAlright, the height is set to:", height, "\n")
    
        while True:
            try:
                n = int(input("How wide do you want the board to be?\n"))
                if n < 10:
                    n = int("Fail")
                if n > 50:
                    n = int("fail")
                if n % 10 != 0:
                    n = int("fail")
                break
            except ValueError:
                print("Please pick an integer between 10 and 50 that is divisble by 10")
        
        width = n
        print("\nAlright, the width is set to:", width, "\n")
        print("So the board will look like this: \n")
        sea = generate_sea(height, width)
        print(sea)
        
        while True:
            #So this is the game loop
            while True:
                #if they don't like the board size they may begin again
                n = input("Is this ok?\n")
                if n == "yes" or n == "Yes":
                    like = True
                    break
                if n == "no" or n == "No":
                    like = False
                    break
                else:
                    print("Sorry, I didn't get that...")
            if not like:
                break
    
            chest = chest_placer(height, width)
            print("There are 3 treasure chests buried on the bottom of the ocean floor!")
            print("You have 16 sonar units that you can place to find them!")
            print("To claim a chest you will have to place a sonar unit on top of it")
            print("Sadly, you can only search for one chest at a time :(\n\n\n")
    
            sonars = 16
            lostchests= 3
            placedsonars = []
            sonarlist = []
            while sonars > 0:
                #Sonar placement loop
                while True:
                    #x placement loop
                    try:
                        print("Pick the horizontal position of sonar #",17 - sonars, "!")
                        n = int(input(""))
                        if n < 0 or n > width - 1:
                            n = int ("fail loop")
                        break
                    except ValueError:
                        print("Please pick a number between 0 and", width)
                currentx = n
                while True:
                    #y placement loop
                    try:
                        print("Pick the vertical position of sonar #", 17 - sonars, "!")
                        n = int(input(""))
                        if n < 0 or n > height - 1:
                            n = int ("fail loop")
                        break
                    except ValueError:
                        print("Please pick a number between 0 and", height)
                currenty = n
                sonarlist.append(currentx)
                sonarlist.append(currenty)
                dist = distance(currentx, currenty, chest, lostchests)
                sea = placesonar(sea, dist, sonarlist, height, width)
                print(sea)
                sonars -= 1
                if dist == 0:
                    lostchests -= 1
                    if lostchests > 0:
                        print("Congratulations! You have found a chest.")
                        print("There are", lostchests, "left!")
                        print("You have", sonars, "sonar devices remaining. Goodluck\n\n")
                    else:
                        print("------------------------------")
                        print("You have found all the chests!")
                        print("WoooOOooOoOOoOOOOOOOoooOoOoo!!")
                        print("------------------------------")
                        print("You had", sonars, "sonars remaining! Good job!")
                        break
                if sonars == 0:
                    print("Awww man, you lost!\nYou had", lostchests, " chests remaining. :(")
            while True:
                n = input("Would you like to play again?\n")
                if n == "yes" or n == "Yes":
                    quit = False
                    print("/n/n/n/n/n/n/n/n/n/n/n/n/n/n/")
                    break
                if n == "no" or n == "No":
                    quit = True
                    break
            break
        if quit:
            break
