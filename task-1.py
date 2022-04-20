from time import sleep
from turtle import *

color('blue', "green")

#
#   Draw one square with size equals parameter `size`
#
def drawSquare(size):
    for _ in range(4):
        forward(size)
        right(90)

#
#   Move turtle to a position of a new square, parameter `margin`
#
def prepareNext(margin):
    penup()
    forward(margin)
    pendown()


#
#   Prepare parameters
#

#   Size of square
sz = int(input("a = "))
if sz < 30:
    print("ERROR: initial size of square should be greater than 30")
    sys.exit(-1)

#   Size decrement value
szDecrement = 30

#   Size of a gap between squares
gapSize = 10

#   Amount of squares
squareCount = 2

#   Loop to draw all squares
for i in range(squareCount):
    drawSquare(sz)

    diff = sz + gapSize
    prepareNext(diff)
    sz = sz - szDecrement

#
#   Wait for 3 seconds
#
sleep(30)

