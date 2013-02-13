#My version of the hangman generator

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
    
Continue = -1
GoodInput = -1


while Continue = -1
    while GoodInput = -1:
        
        
