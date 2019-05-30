# Error Correction
# CSE1010 Homework 7, Spring 2019
# Alex Tomczuk
# April 18, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly

import errordetection


# Phase 1. Encoding

def string2bin(string): # takes string and converts into a list of bit lists
    return [errordetection.char2bin(a) for a in string] # calls 'char2bin' function in errordetection

def segmentString(string, fill): # takes string + fill character & returns list of 8-character string 
    if (len(string) % 8) != 0:
        newList = [string[(8*n):8+(8*n)] for n in range(int(len(string)/8)+1)]
    else:
        newList = [string[(8*n):8+(8*n)] for n in range(int(len(string)/8))]
    return [n.ljust(8, fill) for n in newList] # strings w/ less than 8-characters include fill characters

def printFrames(frames): # helps debug the 'string2frames' function
    frameN = 0
    for frame in frames: 
        charN = 0
        for bin in frame:
            char = errordetection.bin2char(bin)
            print(f"{charN:2}", bin, char)
            charN += 1
            frameN += 1
            print()

def string2frames(string, fill): # calls 'segmentString' function to create 8-character segments
    return [string2bin(n) for n in segmentString(string, fill)] # then returns frame by calling 'string2bin' function

def appendParityColumn(frame, parity): # takes frame (bit lists) & returns new frame w/ parity bit
    return [errordetection.appendParity(bits, parity) for bits in frame]

def transpose(lst): # rotates the list: rows --> columns & columns --> rows
    lst = list(map(list, zip(*lst)))
    return lst

def appendParityRow(frame, parity): # transposes 'appendParityColumn' so there is a row of parity bits
    return (transpose(appendParityColumn(transpose(frame), parity)))

def appendParityToFrame(frame, parity): # takes 8x8 frame & returns 9x9 frame (w/ parities)
    return appendParityRow((appendParityColumn(frame, parity)), parity)

def appendParityToFrames(frames, parity): # returns new lists of frames after adding parities
    return [appendParityToFrame(frame, parity) for frame in frames]


# Phase 2: Transmission

def transmitFrames(frames, error): # transmits frames, displays # flipped bits, & returns new frames
    newFrames = []
    totalBitsFlipped = 0
    for frame in frames:
        newFrame = []
        subTotalBitsFlipped = 0
        for row in frame:
            (newRow, bitsFlipped) = errordetection.addNoise(row, error)
            newFrame.append(newRow)
            subTotalBitsFlipped += bitsFlipped
        newFrames.append(newFrame)
        totalBitsFlipped += subTotalBitsFlipped
            
    print('Number of bits flipped: ', totalBitsFlipped)
    return newFrames


# Phase 3. Decoding

def splitFrame(frame): # splits 9x9 frame into payload, parity column, parity row
    payload = [row[0:8] for row in frame[0:8]]
    parityColumn = [row[8] for row in frame[0:8]]
    parityRow = [row for row in frame[8]]
    return(payload, parityColumn, parityRow)

def checkParityOfFrame(frame, parity): # identifies error by comparing transmitted & received frames
    (recBits, recCol, recRow) = splitFrame(frame)
    reCalcFrame = appendParityToFrame(recBits, parity)
    (reCalcBits, reCalcCol, reCalcRow) = splitFrame(reCalcFrame)
    rowList = [n for n in range(len(recCol)) if recCol[n] != reCalcCol[n]]
    colList = [n for n in range(len(recRow)) if recRow[n] != reCalcRow[n]]
    return(colList, rowList)

def repairFrame(frame, colList, rowList): # repairs frame [if needed] & returns repair status
    if (colList == []) and (rowList == []):
        return('NO ERRORS')
    elif (len(rowList) == 1) and (len(colList) == 2):
        frame[rowList[0]][colList[0]] = 1 - frame[rowList[0]][colList[0]]
        return('CORRECTED')
    elif ((rowList == []) and (len(colList) == 1)) or ((len(rowList) == 1) and (colList == [])):
        return('PARITY ERROR')
    else:
        return('NOT CORRECTED')

def repairFrames(frames, parity): # repairs list of frames & returns repair statuses for each
    returnValues = []
    for frame in frames:
        (colList, rowList) = checkParityOfFrame(frame, parity)
        returnValues.append(repairFrame(frame, colList, rowList))
    for n in range(len(returnValues)):
        if returnValues[n] == 'NO ERRORS':
            print('Frame', n, 'has no errors')
        elif returnValues[n] == 'CORRECTED':
            print('Frame', n, 'has been repaired')
        elif returnValues[n] == 'PARITY ERROR':
            pass
        else:
            print('Frame', n, 'could not be repaired')
    return returnValues

def stripFrames(frames): # creates new list of frames w/o the parities
    returnPayload = []
    for frame in frames:
        (payload, col, row) = splitFrame(frame)
        returnPayload.append(payload)
    return returnPayload

def bin2string(frame, fill): # takes a frame & returns the string (opposite of 'string2bin')
    stringList = [errordetection.bin2char(thing) for thing in frame]
    newStringList = []
    for n in range(len(stringList)):
        if stringList[n] != fill:
            newStringList.append(stringList[n])
    return ''.join(newStringList)

def frames2string(frames, fill): # takes a list of frames & returns the combined string
    listOfStrings = [bin2string(frame, fill) for frame in frames]
    return ''.join(listOfStrings)

def main(): # ties all the functions together
    errorProb = 0.01
    desiredParity = 0 # even
    fillChar = "~" # tilde

    string = input("Enter a string: ")
    frames = string2frames(string, "~")
    transmittedFrames = appendParityToFrames(frames, desiredParity)
    receivedFrames = transmitFrames(transmittedFrames, errorProb)
    repairStatuses = repairFrames(receivedFrames, desiredParity)
    strippedFrames = stripFrames(receivedFrames)
    string = frames2string(strippedFrames, fillChar)

    print(string)
    print(repairStatuses)

    if __name__ == '_main_': # will automatically run file in IDLE when loaded
        main()
