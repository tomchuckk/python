# Error Detection
# CSE1010 Homework 6, Spring 2019
# Alex Tomczuk
# April 07, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly

import math, random

def getChar():
    x = input('Enter a character: ')
    return x[0] # takes character(s) and returns the first character as string

def char2bin(char):
    x = bin(ord(str(char))) # converts number or character to ASCII value and then to binary representation
    y = x.replace('0b', "").zfill(8) # converts binary representation to 8-bit string
    z = list(map(int, y)) # splits string into a list of characters and converts string to integers
    return z

def bin2char(bitlist): 
    s = chr(int(''.join(str(i) for i in bitlist), 2)) # inverse of 'char2bin' function
    return s

def parityOf(bits, par): 
    x = bits.count(1)
    if (x%2 == 0 and par == 0) or (x%2 != 0 and par == 1): # returns 0 for even or odd parity that is undesired
        return int(0)
    else:
        return int(1)

def appendParity(bits, par):
    x = parityOf(bits, par) # call on 'parityOf' function and adds to the parity to the end of the list of bits
    bits.append(x)
    return bits

def addNoise(bits, error): # simulates interference with transmission which causes some bits to change
    y = 0
    x = []
    for n in range(len(bits)):
        if random.random() < error: # uses random chance to determine if a bit changes
            if bits[n] == 1:
                n1 = 0
            else:
                n1 = 1
            y += 1
        else:
            n1 = bits[n]
        x.append(n1)
    return(x, y) # returns the new bit list and the number of bits that changed

def checkParity(bits, par):
    x = parityOf(bits[:8], par)
    if x == bits[8]: # checks to see if the parity bit (9th bit) matches what it was supposed to be
        return True # returns true if no errors were found (parity bit matches what it should be)
    else:
        return False

def main(): # sequences all the functions together
    error = 0.1
    par = 0
    char = getChar()
    bits = char2bin(char)
    x = appendParity(bits, par)
    y,z = addNoise(bits, error)

    print('transmitted bits: ', x)
    print('number of flipped bits: ', z)
    print('received bits ', y)

    if checkParity == True:
        print('no errors detected')
    else:
        print('error detected')
    print('received character: ', bin2char(y[:8]))

    if __name__ == '__main__': # will automatically run file when loaded
        main()
    


