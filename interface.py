#This will be the interface for Live Run 2!
import tools
import time
import SonarGame

def greet():
    print("---------------------")
    print("This is Live Run 2.0!")
    print("---------------------")
    time.sleep(2)



def stmn(start):
    while True:
        #Input loop
        ext = False
        print("\n\n\n\nPlease choose between one of the following categories:")
        print("1) Sequence Calculators")
        print("2) Misc Calculators")
        print("3) Games")
        print("-" * 80, end = "")
        print("\n" * 18)
            
        op1 = ["1", "one", "One", "equence"]
        op2 = ["2", "two", "Two", "isc"]
        op3 = ["3", "three", "Game", "game"]
        opEx = ["exit", "Exit", "close", "Close"]
        opHL = ["ow long"]
        ops = [op1, op2, op3, opEx, opHL]
        
        n = tools.inputmulti(">>> ", ops)
        
        if n == "1":
            print("\n" * 30)
            ext = subMenuOne()
            if ext:
                return True
        elif n == "2":
            print("\n" * 30)
            ext = subMenuTwo()
            if ext:
                return True
        elif n == "3":
            print("\n" * 30)
            ext = subMenuThree()
            if ext:
                return True
        elif n == "ow long":
            tools.howlong(start)
        elif n == "exit":
            return True
        else:
            print("Oops, that's not supposed to happen")
            time.sleep(5)

def subMenuOne():
    while True:
        ex = False
        x = 1
        print("\n\nWhich calculator would you like?")
        print("1) Fibonacci")
        print("2) Happy Numbers")
        print("3) Factorial")
        print("4) Perfect number")
        print("Or would you like to return back to the root menu?")
        print("-" * 80, end = "")
        print("\n" * 16)
        
        op1 = ["1", "ibon"]
        op2 = ["2", "appy"]
        op3 = ["3", "Fact", "fact"]
        op4 = ["4", "erf"]
        opBK = ["eturn", "Back", "back", "oot", "enu"]
        opEX = ["xit", "Close", "close"]
        ops = [op1, op2, op3, op4, opBK, opEX]
        
        n = tools.inputmulti(">>> ", ops)
        
        if n == "1":
            print("\n" * 30)
            x =tools.inputint("Which number are you interested in?")
            list = tools.inputyesno("Would you like the numbers that come before that as well?")
            if ex == "cancel": break
            tools.fib(x, list)
            break
            
        elif n == "2":
            print("\n" * 30)
            n = tools.inputmulti("Are you looking to create a list or to check a number?", ["list", "check", "cancel"])
            y = 0 #dummy value in case of not list
            if n == "list":
                list = True
                x = tools.inputint("How many numbers do you want in the list?")
            elif n == "cancel": break
            else:
                list = False
                x = tools.inputint("Which number do you want to check?")
            if list:
                y = tools.inputint("These lists can take an extreme amount of time.\nPlease set a limit in seconds.")
            tools.HapHandler(x, y, list)
            break

        elif n == "3":
            print("\n" * 30)
            x = tools.inputint("What number do you want the factorial of?")
            list = tools.inputyesno("Do you want the numbers that come before it?")
            tools.fact(x, list)
            break
    
        elif n == "4":
            print("\n" * 30)
            n = tools.inputmulti("Are you looking to create a list or to check a number?", ["list", "check", "cancel"])
            y = 0 #dummy value in case of not list
            if n == "list":
                list = True
                x = tools.inputint("How many numbers do you want in the list?")
            elif n == "cancel": break
            else:
                list = False
                x = tools.inputint("Which number do you want to check?")
            if list:
                y = tools.inputint("These lists can take an extreme amount of time.\nPlease set a limit in seconds.")
            tools.PerHandler(x, y, list)
            break
            
        elif n == "eturn":
            ex = False
            break
        
        elif n == "xit":
            ex = True
            break
        else:
            print("That command was not recognized.\n\n")
    return ex

def subMenuTwo():
    while True:
        ex = False
        x = 1
        print("\n\nWhich calculator would you like?")
        print("1) Half Life")
        print("2) Variance")
        print("3) BMI")
        print("Or would you like to return back to the root menu?")
        print("-" * 80, end = "")
        print("\n" * 17)
        
        op1 = ["1", "one", "half", "Half"]
        op2 = ["2", "two", "aria"]
        op3 = ["3", "three", "BMI", "bmi" "Bmi"]
        opBK = ["eturn", "Back", "back", "oot", "enu"]
        opEX = ["xit", "Close", "close"]
        ops = [op1, op2, op3, opBK, opEX]
        n = tools.inputmulti(">>> ", ops)


        if n == "1":
            print("\n" * 30)
            ex = tools.Halflife()
            break
            
        if n == "2":
            print("\n" * 30)
            ex = tools.Variance()
            break

        if n == "3":
            print("\n" * 30)
            ex = tools.BMI()
            break
            
        elif n == "eturn" :
            break
        elif n == "xit":
            ex = True
            break
            
        else:
            print("That's not supposed to happen...")
    return ex

def subMenuThree():
    ex = False
    print("\n\nWhich game would you like to play?")
    print("1) Sonar")
    print("2) Matrix Mode")
    print("Or would you like to return back to the root menu?")
    print("-" * 80, end = "")
    print("\n" * 19)

    op1 = ["1", "onar", "one", "irst"]
    op2 = ["2", "atrix", "two", "econd"]
    opBK = ["eturn", "Back", "back", "root", "Root", "enu"]
    opEX = ["xit", "lose"]
    ops = [op1, op2, opBK, opEX]
    n = tools.inputmulti(">>> ", ops)

    if n == "1":
        SonarGame.Sonar()

    elif n == "2":
        t = tools.inputint("How long do you want the Matrix to last?")
        tools.matrix(t)

    elif n == "eturn":
        s = "Do nothing"

    elif n == "xit":
        ex = True
            
    else:
        print("That's not supposed to happen...")

    return ex
