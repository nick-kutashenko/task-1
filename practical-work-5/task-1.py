import turtle
import sys


#
#   Draw one square with size equals parameter `size`
#
def draw_square(size):
    if size <= 0:
        print("FATAL ERROR: The square size must be greater than zero")
        sys.exit(-1)
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
#   Program start is here
#

#   Request `a` value, as initial square size
a = int(input('a = '))

#   Request `b` value, as size incrementer
b = int(input('b = '))

#   Amount of squares
squareCount = 4

#   Set turtle colors
turtle.color('blue', "green")

#   Loop to draw all squares
for _ in range(squareCount):
    draw_square(a)
    diff = a + 10
    prepare_next(diff)
    a += b

#
#   Wait to see results
#
input('Press something :)')
