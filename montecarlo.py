# Monte Carlo Simulation
# CSE1010 Homework 4, Spring 2019
# Alex Tomczuk
# February 22, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly


import math
import random
import tkinter

FIELD_W = 600 # field width equal to canvas width
FIELD_H = 600 # field height equal to canvas height

POND_X = 300 # pond position in field (origin)
POND_Y = 300 # pond position in field (origin)
POND_R = 150 # pond radius

shotX = random.randint(0, FIELD_W)
shotY = random.randint(0, FIELD_H)

NUM_SHOTS = 1000 # number of shots fired


def drawCircle(canvas, x, y, r, outline='black', fill='white'):
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    canvas.create_oval(x1, y1, x2, y2, fill=fill, outline=outline)


def drawPond(canvas):
    drawCircle(canvas, POND_X, POND_Y, POND_R, outline='blue')


def hitPond(shotX, shotY):
    dist = math.sqrt(((shotX-POND_X)**2)+((shotY-POND_Y)**2))
    if dist <= POND_R:
        hitPond = True # hits pond if shot distance to pond center is less than pond radius
    else:
        hitPond = False 
    return hitPond


def plotShot(canvas, shotX, shotY):
    h = hitPond(shotX,shotY)
    if h:
        drawCircle(canvas, shotX, shotY, 5, outline='black', fill='blue') # hits pond
    else:
        drawCircle(canvas, shotX, shotY, 5, outline='black', fill='green') # lands outside of pond
    return h


def fireShot(canvas):
    shotX=random.randint(0, FIELD_W)
    shotY=random.randint(0, FIELD_H)	
    hit = plotShot(canvas, shotX, shotY) # need to assign to a variable and return
    return hit


def fireShots(canvas, NUM_SHOTS):
    splashes=0
    for i in range(NUM_SHOTS):
        x = fireShot(canvas) # need to assign to variable to have conditions
        if x == True:
            splashes = splashes + 1
        elif x == False:
            pass
    return splashes


def estimatePondArea(fireShots, NUM_SHOTS):
    fieldarea = FIELD_W * FIELD_H
    splashratio = fireShots / NUM_SHOTS
    pondarea = fieldarea * splashratio
    return pondarea
        

def initWindow(title, width, height):
    master = tkinter.Tk()
    master.title(title)
    canvas = tkinter.Canvas(master, width=width, height=height)
    canvas.pack()
    return canvas


def main():
    canvas = initWindow("Monte Carlo Simulation", FIELD_W, FIELD_H) 
    drawPond(canvas)
    numSplashes = fireShots(canvas, NUM_SHOTS)
    print("Number of shots:", NUM_SHOTS)
    print("Number of splashes:", numSplashes)
    estPondArea = estimatePondArea(numSplashes, NUM_SHOTS)
    estPondArea = round(estPondArea, 1)
    print("Estimated pond area:", estPondArea)
    actPondArea = round(math.pi * POND_R**2, 1)
    print("Actual pond area:", actPondArea)
    err = round(abs(actPondArea - estPondArea) / actPondArea * 100, 1)
    print("Error:", err, "%")
if __name__ == '__main__':
    main()
    tkinter.mainloop()
