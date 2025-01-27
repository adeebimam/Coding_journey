from turtle import Turtle as t, Screen
from random import Random

addi_turtle = t()
addi_turtle.shape("turtle")
addi_turtle.speed("fastest")
addi_turtle.pensize(5)
colors = ["dark red", "blue", "slate gray", "dark slate gray", "orange", "purple", "dark violet", "black", "brown",]

def draw_polygon(sides):
    angle = 360 / sides
    for i in range(sides):

        addi_turtle.forward(100)
        addi_turtle.right(angle)

for i in range(3, 11):
    addi_turtle.color(Random().choice(colors))
    draw_polygon(i)





screen = Screen()
screen.exitonclick()