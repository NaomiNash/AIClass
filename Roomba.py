#!/usr/bin/env python3

''' Roomba.py - Naomi Nash - Saint Leo University -
        24 Jan 2022 - Simulate a vacuum robot on a
        one dimensioinal carpet '''

import random

# -------------------------------------------------
def createCarpet(mySize=10, maxDirty=10) :
    ''' Returns a list of length mySize containing
        random ints from zero to maxDirty '''
    retVal = list()
    for i in range(0, mySize) :
        retVal.append(random.randint(1,maxDirty))
    return retVal

# -------------------------------------------------
def randomStartPosition(myCarpet) :
    ''' Returns a random position on the carpet, in
        0...len(myCarpet)-1 '''
    return random.randint(0,len(myCarpet)-1)

# -------------------------------------------------
def reportCarpet(myCarpet, myPosition=None) :
    ''' Print the carpet and mark the potion of the
        vacuum robot with an asterisk if one is
        specified '''
    print('+'+'+----'*len(myCarpet)+'++')
    
    print('|', end='')
    for i in range(0,len(myCarpet)) :
        if (i == myPosition) :
            print(F"|*{myCarpet[i]:^3}", end='')
        else :
            print(F"|{myCarpet[i]:^4}", end='')
    print('||')

    print('+'+'+----'*len(myCarpet)+'++')

# -------------------------------------------------
def canGoRight(myCarpet, myPosition) :
    ''' Return True if an agent at myPosition can
        go right and still remain on the carpet '''
    return myPosition < (len(myCarpet) -1)

# -------------------------------------------------
def canGoLeft(myCarpet, myPosition) :
    ''' Return True if an agent at myPosition can
        go left and still remain on the carpet '''
    return myPosition > 0
    
# -------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------
if __name__ == '__main__' :
    carpet = createCarpet()
    vacuumPosition = randomStartPosition(carpet)
    reportCarpet(carpet, vacuumPosition)
    print('vacuumPosition == ', vacuumPosition)
    
# -------------------------------------------------
