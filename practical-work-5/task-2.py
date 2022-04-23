import turtle
import sys

turtle.color('blue', "green")


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

#   `b` value is size incrementer
b = 10

#   Loop to draw all squares
while True:
    draw_square(a)
    diff = a + 10
    prepare_next(diff)
    a = a + b
    if a >= 200:
        print("Size is reached a limit")
        break

#
#   Wait to see results
#
input('Press something :)')
