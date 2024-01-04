#!/usr/bin/python
#-*-encoding:utf-8-*-

import random
import sys
import os

def printDocAndExit():
    print("Run ./roll_caracter.py [--output output_txt] [--age age] [-h] [--help]")
    print("--output: output path to save the caracter's data. Default: output.txt")
    print("--age: the caracter's age. Default: 20")
    print("-h --help: Print this documentation and exit.")

    sys.exit(-1)

def generate3d6():
    return sum([random.randint(1, 6) for x in range(3)])

def genererate2d6_6():
    return sum([random.randint(1, 6) for x in range(2)])+6

def improvement_check(old_value):
    d100 = random.randint(1, 100)
    d10  = 0
    if d100 >= old_value:
        d10 = random.randint(1, 10)
        if old_value + d10 > 99:
            d10 = 99 - old_value
        old_value += d10
    return (old_value, d100, d10)

if __name__ == '__main__':
    argv       = sys.argv[1:]
    outputFile = os.getcwd() + "/output.txt"
    age        = 20

    i = 0
    while i < len(argv):
        #Read input file names (beginning of the command)
        arg = argv[i]
        while i < len(argv):
            arg = argv[i]

            if arg == "-h" or arg == "--help":
                printDocAndExit()

            elif arg == "--output":
                if i < len(argv)-1:
                    outputFile = argv[i+1]
                    i+=1
                else:
                    print("Missing output file path value to the '--output' parameter")
                    sys.exit(-1)
            elif arg == "--age":
                if i < len(argv)-1:
                    age = int(argv[i+1])
                    if age < 15 or age > 89:
                        print("Age must be between 15 and 89... Exiting")
                        sys.exit(-1)
                    i+=1
                else:
                    print("Missing age value to the '--age' parameter")
                    sys.exit(-1)
            else:
                print("Unknown parameter {}".format(arg))
                printDocAndExit()
            i+=1

    print(f"Age: {age}")

    STR = 5*generate3d6()
    print(f"Rolling STR: {STR}")
    CON = 5*generate3d6()
    print(f"Rolling CON: {CON}")
    DEX = 5*generate3d6()
    print(f"Rolling DEX: {DEX}")
    APP = 5*generate3d6()
    print(f"Rolling APP: {APP}")
    POW = 5*generate3d6()
    print(f"Rolling POW: {POW}")
    LUCK = 5*generate3d6()
    print(f"Rolling LUCK: {LUCK}")

    SIZ = 5*genererate2d6_6()
    print(f"Rolling SIZ: {SIZ}")
    INT = 5*genererate2d6_6()
    print(f"Rolling INT: {INT}")
    EDU = [(5*genererate2d6_6(),)]
    print(f"Rolling EDU: {EDU[0][0]}")

    if age <= 19:
        LUCK = max(LUCK, 5*generate3d6())
        print("You would need to deduce 5 points from STR or SIZE.")
        EDU[-1] -= 5
        print(f"Reducing EDU by 5 points... EDU : {EDU[-1]}")

    elif age <= 39:
        EDU.append(improvement_check(EDU[-1][0]))
        print(f"Rolling improvement check on EDU : d100 = {EDU[-1][1]}{' --> d10 = ' + str(EDU[-1][-1]) if EDU[-1][-1] > 0 else ''}")

    elif age <= 49:
        print("You would need to deduce 5 points from STR, CON and DEX (distributed).")
        APP -= 5
        print(f"Reducing APP by 5 points... APP : {APP}")
        for i in range(2):
            EDU.append(improvement_check(EDU[-1][0]))
            print(f"Rolling improvement check on EDU : d100 = {EDU[-1][1]}{' --> d10 = ' + str(EDU[-1][-1]) if EDU[-1][-1] > 0 else ''}")

    elif age <= 59:
        print("You would need to deduce 10 points from STR, CON and DEX (distributed).")
        APP -= 10
        print(f"Reducing APP by 10 points... APP : {APP}")
        for i in range(3):
            EDU.append(improvement_check(EDU[-1][0]))
            print(f"Rolling improvement check on EDU : d100 = {EDU[-1][1]}{' --> d10 = ' + str(EDU[-1][-1]) if EDU[-1][-1] > 0 else ''}")

    elif age <= 69:
        print("You would need to deduce 20 points from STR, CON and DEX (distributed).")
        APP -= 15
        print(f"Reducing APP by 15 points... APP : {APP}")
        for i in range(4):
            EDU.append(improvement_check(EDU[-1][0]))
            print(f"Rolling improvement check on EDU : d100 = {EDU[-1][1]}{' --> d10 = ' + str(EDU[-1][-1]) if EDU[-1][-1] > 0 else ''}")

    elif age <= 79:
        print("You would need to deduce 40 points from STR, CON and DEX (distributed).")
        APP = max(APP, APP-20)
        print(f"Reducing APP by 20 points... APP : {APP}")
        for i in range(4):
            EDU.append(improvement_check(EDU[-1][0]))
            print(f"Rolling improvement check on EDU : d100 = {EDU[-1][1]}{' --> d10 = ' + str(EDU[-1][-1]) if EDU[-1][-1] > 0 else ''}")

    else:
        print("You would need to deduce 80 points from STR, CON and DEX (distributed).")
        APP = max(APP, APP-25)
        print(f"Reducing APP by 25 points... APP : {APP}")
        for i in range(4):
            EDU.append(improvement_check(EDU[-1][0]))
            print(f"Rolling improvement check on EDU : d100 = {EDU[-1][1]}{' --> d10 = ' + str(EDU[-1][-1]) if EDU[-1][-1] > 0 else ''}")

    SAN          = POW
    MAGIC_POINTS = int(POW/5)
    HP           = int((SIZ+CON)/10)

    print("Cannot determine MOV as maybe some values must be adjusted...")
    print("Same for combat value")

    with open(outputFile, "w") as f:
        f.write(f"age: {age}\n\n")
        f.write(f"STR: {STR}\n")
        f.write(f"CON: {CON}\n")
        f.write(f"DEX: {DEX}\n")
        f.write(f"APP: {APP}\n")
        f.write(f"POW: {POW}\n")
        f.write(f"SIZ: {SIZ}\n")
        f.write(f"INT: {INT}\n")
        f.write(f"EDU: {EDU[-1][0]}\n")
        f.write(f"LUCK: {LUCK}\n")

        for i in range(0, len(EDU)-1):
            f.write(f"Improvment check: EDU = {EDU[i][0]}, d100 = {EDU[i+1][1]} {' --> d10 = ' + str(EDU[i+1][-1]) if EDU[i+1][-1] > 0 else ''}\n")
