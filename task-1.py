
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
    forward(int(diff + (newSz - sz)) / 2)
    pendown()


#
#   Prepare parameters
#

#   Size of square
sz = int(input("a = "))
#   Size multiplier
szMultiplier = 30

#   Amount of squares
squareCount = 2

#   Loop to draw all squares
for i in range(squareCount):
    drawSquare(sz)

    newSz = sz - szMultiplier
    diff = (newSz - sz) / 2
    prepareNext(diff)
    sz = newSz
