# N-Body Simulation
# CSE1010 Homework 5, Spring 2019
# Alex Tomczuk
# March 15, 2019
# TA: Yijue Wang
# Lab section: 002
# Instructor: Raafat Elfouly

import math, random, time, turtle

# global constants:
NBodies = 5
G = 5
SpaceRadius = 250
MinMass = 5
MaxMass = 100
MaxVelocity = 100
BodyColor = 'black'
TraceColor = 'green'

Turtles = [] # helps draw graphics
Masses = [] # masses of all bodies
Xs = [] # x coordinate for each body
Ys = [] #  y coordinate for each body
Vxs = [] # x component of body velocity
Vys = [] # y component of body velocity

OffScreen = [] # list of bodies that left viewing area - program stops when all bodies left area
WinX2 = 0 # x value for determining if body left viewing area
WinY2 = 0 # y value for determining if body left viewing area

def newTurtle():
    t = turtle.Turtle() # 1. create new turtle and store in var (t) -- this var (t) is local to newTurtle
    Turtles.append(t) # 2. append this turtle the the Turtles list var
    t.speed(0) # 3. turtle return speed = 0 and pensize = 5
    t.pensize(5)
    return t # 4. return turtle value found in the variable it is stored in (x)

def printBodyInfo(n):
    print('Body', n, 'mass =', Masses[n], ', x =', Xs[n], ', y =',
          Ys[n], ', vx =', Vxs[n], ', vy =', Vys[n])

def initBody(t):
    mass = random.randint(MinMass, MaxMass) # 1. generate random mass in min-max range and append value to Masses list
    Masses.append(mass) 
    t.turtlesize(mass*0.03, mass*0.03) # 2. set turtle size
    t.shape('circle') # 3. set turtle shape to circle

    x = random.randint(-SpaceRadius, SpaceRadius) # 4. generate random x-location for turtle in space radius range and append to Xs list
    Xs.append(x)
    y = random.randint(-SpaceRadius, SpaceRadius) # 5. same thing for y-location
    Ys.append(y)

    vx = random.randint(-MaxVelocity, MaxVelocity) / 100 # 6. generate random x velocity in velocity range and add to Vxs list
    Vxs.append(vx)
    vy = random.randint(-MaxVelocity, MaxVelocity) / 100 # 7. same thing for y velocity
    Vys.append(vy)

    OffScreen.append(False) # 8. append value 'false' to OffScreen list

    t.penup() # 9. call 'penup' on turtle to go to x and y locations then call 'pendown'
    t.goto(x,y)
    t.pendown()

def setup():
    turtle.tracer(0,0) # 1. stop turtle animations from showing up until 'update' function is called - speeds up display output
    for x in range(NBodies): # 2. create for loop that iterates over number of bodies
        t = newTurtle() # 3. call newTurtle function and store value in new var
        initBody(t) # 4. call initBody function
        printBodyInfo(x) # 5. call printBodyInfo function
    turtle.update()
    
def moveBody(n):
    xNew = Xs[n] + Vxs[n] # 1. create equations for bodies in motion and replace values in Xs and Ys lists
    Xs[n] = xNew
    yNew = Ys[n] + Vys[n]
    Ys[n] = yNew

    t = Turtles[n] # 2. move the body

    t.hideturtle()
    t.color(TraceColor)
    t.goto(xNew,yNew) 
    t.color(BodyColor) 
    t.showturtle()

    if xNew < -WinX2 or xNew > WinX2 or yNew < -WinY2 or yNew > WinY2: # checks if value moved off screen
        OffScreen[n] = True

def moveBodies():
    for n in range(NBodies):
        t = Turtles[n]
        if t is not None:
            moveBody(n)
    
def calculateForce(n1, n2):
    m1 = Masses[n1]
    m2 = Masses[n2]
    x1 = Xs[n1]
    x2 = Xs[n2]
    y1 = Ys[n1]
    y2 = Ys[n2]

    dx = x2 - x1 # difference between x values
    dy = y2 - y1 

    r = math.sqrt((dx**2)+(dy**2)) # calculates distance between bodies

    f = G*((m1*m2)/(r**2)) # calculates the force

    a = math.atan2(dy , dx) # angle force

    fx = f * math.cos(a) # x direction force
    fy = f * math.sin(a)

    return fx, fy


def accelerateBody(body):
    for n in range(NBodies):
        if n != body: # calculate force 
            a, b = calculateForce(body, n)

            xA = a / Masses[body] # x acceleration
            yA = b / Masses[body] # y 

            xSum = xA + Vxs[body] # adding acceleration and velocity
            ySum = yA + Vys[body]

            Vxs[body] = xSum # replacing sum back in lists
            Vys[body] = ySum

def accelerateBodies():
    for n in range(NBodies):
        t = Turtles[n]
        if t is not None:
            accelerateBody(n)

def main():
    print('N-Body simulation starting')
    screen = turtle.Screen()
    screen.title('N-Body Simulator') # title of turtle graphics window
    global WinX2, WinY2
    WinX2 = screen.window_width() / 2
    WinY2 = screen.window_height() / 2
    setup() 
    while not all(OffScreen): # moves the body until all are off screen
        moveBodies()
        accelerateBodies()
        turtle.update()
    print('Program finished')
    screen.mainloop() # keeps the turtle graphics window on screen until manually closed

if __name__ == '__main__':
    main()
