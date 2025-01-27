from turtle import Turtle as t, Screen
from random import Random

addi_turtle = t()
addi_turtle.shape("turtle")

#triangle
for i in range(3):
    addi_turtle.forward(100)
    addi_turtle.right(120)

#square 
for i in range(4):
    addi_turtle.forward(100)
    addi_turtle.right(90)

#pentagon
for i in range(5):
    addi_turtle.forward(100)
    addi_turtle.right(72)

#hexagon
for i in range(6):
    addi_turtle.forward(100)
    addi_turtle.right(60)

#heptagon
for i in range(7):
    addi_turtle.forward(100)
    addi_turtle.right(51.43)

#octagon
for i in range(8):
    addi_turtle.forward(100)
    addi_turtle.right(45)

#nonagon
for i in range(9):
    addi_turtle.forward(100)
    addi_turtle.right(40)

#decagon
for i in range(10):
    addi_turtle.forward(100)
    addi_turtle.right(36)


screen = Screen()
screen.exitonclick()