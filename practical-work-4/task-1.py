import turtle
import sys

turtle.color('blue', "green")


#
#   Draw one square with size equals parameter `size`
#
def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)


#
#   Move turtle to a position of a new square, parameter `margin`
#
def prepare_next(margin):
    turtle.penup()
    turtle.forward(margin)
    turtle.pendown()


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
for _ in range(squareCount):
    draw_square(sz)

    diff = sz + gapSize
    prepare_next(diff)
    sz = sz - szDecrement

#
#   Wait to see results
#
input('Press something :)')
