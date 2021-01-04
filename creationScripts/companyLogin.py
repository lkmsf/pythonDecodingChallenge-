#!/usr/bin/env python

import time 
import random 

PSWD = "@38lx^2c$5ta" 

def main():
    tries = 4
    while True: 
        user = input("login: ")
        if user == "admin": 
            break 
        print("No user by that name. Try again")
        tries -= 1
        printWarning(tries)
        if not tries: 
            return 

    while True: 
        user = input("password: ")
        if user == PSWD: 
            break 
        print("Wrong password")
        tries -= 1
        printWarning(tries)
        if not tries: 
            return 

    print("Welcome admin")
    printHack()     

    printMsg("\n\n Self Destructing") 
    return 

def printWarning(n): 
    if n == 3: 
        print("You have 3 tries before you're locked out")
    if n == 1: 
        print("One more try")
    if n == 0: 
        print("Locked out")

def printHack(): 
    print("Starting hack in", end = "")
    printDots(3, 0.25)
    for i in range(3, 0, -1): 
        print(i, " ", end = "", flush = True )
        time.sleep(0.6)
    printDots(3, 0.25)
    print()
    
    printMsg("Connecting to mainframe")
    printMsg("Downloading package")
    printMsg("Running virus")
    printMsg("Successfully deployed virus")
    printMsg("All assets deposited in offshore account") 

    printMsg("Changing directory")
    printMsg("Searching around for files")
    printRandom()


def printRandom(): 
    randomChars = "@*$&%@#(*%@(*!#$<>?:{}|{}{|}adsdgakdgjalkgfjakhjwietuirencmv,bKJDNGKSJHGUIEWWOIQ?" 
    for _ in range(random.randrange(20, 200)): 
        line = ""
        for _ in range(random.randrange(40, 100)): 
            line += randomChars[random.randrange(len(randomChars))]
        time.sleep(random.randrange(5) / 50)
        print(line)


def printMsg(s): 
    print(s, end = "")
    numDots = random.randrange(1, 4)
    for _ in range(numDots): 
        printDots(random.randrange(1, 6), random.randrange(5) / 10)
    print() 


def printDots(n, t): 
    for _ in range(n):
        time.sleep(t)
        print(".", end = "", flush = True)
    time.sleep(t)

if __name__ == "__main__":
    main()
