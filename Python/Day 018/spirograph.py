from turtle import Turtle, Screen, colormode
from random import Random

addi_color = colormode(255)
addi_turtle = Turtle()
addi_turtle.shape("arrow")
addi_turtle.pensize(2)
addi_turtle.speed("fastest")

def random_color():
    r = Random().randint(0, 255)
    g = Random().randint(0, 255)
    b = Random().randint(0, 255)
    random_color =  (r, g, b)
    return random_color


def draw_a_spirograph(size_of_gap):
    counts = int(3600/size_of_gap)
    for i in range(counts):
        addi_turtle.color(random_color())
        addi_turtle.circle(100)
        current_heading = addi_turtle.heading()
        addi_turtle.setheading(current_heading + 10)

count = input("Enter the size of the gap: ")
draw_a_spirograph(int(count))


screen = Screen()
screen.exitonclick()