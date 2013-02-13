#All the tools for the program
import time
import random

def inputint(string):
    print(string)
    while True:
        try:
            x = int(input())
            if x < 1:
                x = int("fail")
            return x
        except ValueError:
            print("Please pick a positive integer")

def inputfloat(string):
    print(string)
    while True:
        try:
            x = float(input())
            if x < 1:
                x = float("fail")
            return x
        except ValueError:
            print("Please pick a decimal number.")

def inputyesno(string):
    print(string)
    while True:
        n = input("")
        if "yes" in n or "Yes" in n or "yeah" in n or "Yeah" in n :
            return True
        elif "no" in n or "No" in n:
            return False
        else:
            print("Is that a 'yes' or a 'no'?")

    
def inputmulti(string, options):
    #So multi is kinda of awesome. It checks if multi, or multi-multi then handles it (multi=true is multi-multi)
    #if multi it returns the first, if multimulti it returns the first of the i'th list
    j = 0
    i = 0
    l = 0
    m = 0
    k = "singing"
    try:
        l = len(options[0][1][1])
        multi = True
    except IndexError:
        multi = False
    if multi:
        j = len(options)
        while True:
            k = input(string)
            i = 0
            while i < j:
                l = 0
                m = len(options[i])
                while l < m:
                    if options[i][l] in k:
                        return options[i][0]
                    l += 1
                i += 1
            print("That's not one of the availible options.")
    if not multi:
        j = len(options)
        while True:
            k = input(string)
            i = 0
            while i < j:
                if options[i] in k:
                    return options[i]
                i += 1
            print("That's not one of the availible options.")

def fib(n, list):

    if not list:
        if n == 1:
            return 0.
        if n == 2:
            return 1
        i=2
        sum = 1
        prev = 0
        while i < n:
            sum = sum + prev
            prev = sum - prev
            i += 1
        print(sum)
        time.sleep(2)
    if list:
        if n == 1:
            print(0)
        i=2
        sum = 1
        prev = 0
        print(0)
        print(1)
        while i < n:
            sum = sum + prev
            prev = sum - prev
            print(sum)
            i += 1
        time.sleep(2)

def howlong(start):
    long = time.time() - start
    if long < 60:
        length = str(round(long,2)) + " seconds.\n\n"
    elif (long < 3600) and (long > 60):
        secs = long % 60
        length = str( int((long - secs) / 60)) + " minutes and " + str(int(round(secs,0))) + " seconds.\n\n"
    else:
        length = "a damn long time.\n\n"
    print("This program has been running for", length)
    print("\n" * 20)
    time.sleep(2)

def PerHandler(x, y, list):
    i = 2
    j = 1
    if list:
        print("Your list:")
        print("1. " + "1".rjust(12))
        start= time.time()
        while j < x:
            if time.time() - start > y:
                print("Sorry, this function ran out of time.")
                break
            if isPerfect(i):
                j += 1
                print((str(j) + ".").rjust(3), str(i).rjust(12))
            i += 1
        return 0
    if not list:
        if x == 1:
            print("It's perfect!")
            return 0
        else:
            if isPerfect(x):
                print("It's perfect!")
                return 0
            else:
                print("It's not perfect.")
                return 0

def isPerfect(n):
    if n == 1:
        return True
    if n % 2 == 1:
        return False
    i = 1
    sum = 0
    while i < n:
        if n % i == 0:
            sum += i
        i += 1
    if sum == n:
        return True
    return False

def matrix(t):
    a = " "
    b = ['@', '!', '/', '}', '*', '&', '^', '#', '>', '<' , '?', '|' , 'X' , '(', ')', '.']
    start = time.time()
    disp = ""
    while time.time() - start < t:
        time.sleep(.01)
        disp = ""
        while len(disp) < 70:
            i = random.randint(1, 12)
            j = random.randint(0, 15)
            disp += a * i + b[j]
        print(disp)

def fact(n, list):
    i = 1
    f = 1
    if list:
        if n == 0:
            print(1)
        if n == 1:
            print("1\n1")
        while i < n + 1:
            f *= i
            i += 1
            if n < 26:
                print((str(i - 1) + ".").rjust(3), str(f).rjust(27))
            else:
                print(f)
    else:
        if n == 0:
            print(1)
        if n == 1:
            print(1)
        while i < n + 1:
            f *= i
            i += 1
        print(f)  

def HapHandler(x, y, list):
    secs= time.time()
    haps = 0
    hapsl = []
    i = 0
    if list:
        while haps < x:
            if time.time()-secs > y:
                print("Sorry, this function ran out of time.")
                break
            if happy2(i) == "Yay! Happy":
                haps += 1
                print((str(haps) + ".").rjust(4), str(i).rjust(12))
            i += 1
        i = 0    
    else:
        print(happy2(x))

def happy2(n):
    #This code is for calling
    happy = False

    m = n
    sum = 0
    counter = 0
    while True:
        a = str(m)
        i=0
        counter += 1
        if counter > 100000:
            break
        sum = 0
        while i < len(a):
            sum += int(a[i]) ** 2
            i += 1
        m = sum
        if sum == 1:
            happy = True
            break
        if sum == n:
            break

    if happy == False:
        return "a sad number"
    else:
        return "Yay! Happy"


def Halflife():
    units = input("What units will you be using?")
    if "exit" in units or "Exit" in units or "Close" in units or "close" in units:
        return True
    while True:
        n = input("Are you looking for....\n1) Remaining percent\n2) Half-life\n")
        if n == "1" or n == "Remaining percent" or n == "percent" or n == "Percent":
            percent = True
            break
        if n == "2" or n == "Half-life" or n == "half-life" or n == "half":
            percent = False
            break
        else:
            print("Sorry, that is not a valid response")
    if percent:
        while True:
            try:
                print("What is the half-life in " + units + "?\n")
                n = float(input(""))
                hl = n
                if n < 0:
                    n =float("Fail try")
                break
            except ValueError:
                print("Please use a positive decimal.")
        while True:
            try:
                print("How many " +units + " have elapsed?\n")
                n = float(input(""))
                te = n
                if n < 0:
                    n =float("Fail try")
                break
            except ValueError:
                print("Please use a positive decimal.")
        result = round(0.5 ** ( te / hl ) * 100, 2)
        result = str(result) 
        result = "There is " + result + "% remaining"

    if not percent:
        import math
        while True:
            try:
                n = float(input("What was the starting value?\n"))
                stval = n
                if n < 0:
                    n =float("Fail try")
                break
            except ValueError:
                print("Please use a positive decimal.")
        while True:
            try:
                n = float(input("What was the end value?\n"))
                endval = n
                if n < 0:
                    n =float("Fail try")
                break
            except ValueError:
                print("Please use a positive decimal.")
        while True:
            try:
                print("How many " + units + " have elapsed?\n")
                n = float(input(""))
                te = n
                if n < 0:
                    n =float("Fail try")
                break
            except ValueError:
                print("Please use a positive decimal.")
        result = round( 0 - (te * math.log10(.5)) / math.log10(stval / endval), 4)
        result = str(result)
        result = "The half-life is " + result + units
    return False
            
def Variance():
    string = "Would you like to enter the set as a list or one number at a time?"
    ops = [["list", "List", "array"], ["time", "one", "One"], ["exit", "close", "Exit", "Close"], ["Cancel", "cancel"]]
    print("You can cancel at any time")
    n = inputmulti(string, ops)
    if n == "exit":
        return True
    elif n == "list":
        while True:
            try:
                list = input("Please enter the list as an array [ 1, 2, 3]")
                if "cancel" in list or "Cancel" in list:
                    cancel = True
                    break
                i = 0
                if len(list) == 1: float("abc")
                while i < len(list):
                    float(list[i])
                    i += 1
            except ValueError:
                print("That is not a valid list, please try again")
    elif n == "time":
        print("Please enter 'end' once complete")
        list = []
        while True:
            try:
                k = input("")
                if k == "end" or k == "End":
                    break
                if "cancel" in k or "Cancel" in k:
                    return False
                list.append(float(k))
            except ValueError:
                print("That is not a valid decimal number")
        if len(list) == 1:
            print("More than one number is needed.")
            return False

    elif n == "Cancel":
        return False
    else:
        print("Sorry, that's not one of the options")
    l = len(list)
    i = 0
    sum = 0.0
    while i < l:
        sum += list[i]
        i += 1
    average = sum / l
    variance = 0.0
    i = 0
    while i < l:
        variance += ( (list[i] - average) ** 2) / l
        i += 1
    i
    print("Variance is equal to:           ", round(variance, 3))
    print("The standard of deviation is:   ", round(variance ** .5, 3))
    print("The average is:                 ", round(average, 3))
    print("There were", l, "numbers in the list.")
    time.sleep(2)        
    return False

def BMI():
    print("Would you like to enter your information as 'metric' or 'imperial'\n(also known as 'murican')?\n")
    print("\n" * 20)
    n = inputmulti(">>> ", [["etric", "Workaround"],["perial", "ican"]])
    if n == "etric" :
        metric = True
    if n == "perial":
        metric = False
 
    if metric:
        print("What is your height in meters (leave off the units)?", "\n"*21)
        h = inputfloat(">>> ")
        print("What is your weight in kilograms (leave off the units)?", "\n"*21)
        w = inputfloat(">>> ")
    if not metric:
        h1 = inputfloat("What is your height in feet (leave off the units and inches)?")
        h = inputfloat("And how many inches?")
        h = ( h + h1 * 12) / 39.37
        w = inputfloat("What is your weight in pounds(leave off the units)?")
        w = w / 2.20462
    print( "Your BMI is", round( w / (h ** 2), 1))
    time.sleep(2)
    return False
