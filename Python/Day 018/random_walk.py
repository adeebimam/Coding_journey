from turtle import Turtle, Screen, colormode
from random import Random

addi_color = colormode(255)

addi_turtle = Turtle()
addi_turtle.shape("turtle")
addi_turtle.pensize(5)
addi_turtle.speed("fastest")

def random_color():
    r = Random().randint(0, 255)
    g = Random().randint(0, 255)
    b = Random().randint(0, 255)
    random_color =  (r, g, b)
    return random_color

directions = [0, 90, 180, 270]

for _ in range(5000):
    addi_turtle.forward(10)
    addi_turtle.setheading(Random().choice(directions))
    addi_turtle.color(random_color())

screen = Screen()
screen.exitonclick()