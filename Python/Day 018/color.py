from turtle import Turtle as t, Screen, colormode
from random import Random

# List of colors

color = [(199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)]


addi_turtle = t()  # Create a turtle object
addi_turtle.shape("turtle")  # Set the turtle shape to turtle
addi_turtle.speed("fastest")  # Set the turtle speed to fastest
addi_color = colormode(255)

y_coordinate = [-300, -250, -200, -150, -100, -50, 0, 50, 100, 150]
addi_turtle.penup()

for y in y_coordinate:
    addi_turtle.goto(-300, y)
    for i in range(10):
        addi_turtle.color(Random().choice(color))
        addi_turtle.dot(20)
        addi_turtle.penup()
        addi_turtle.forward(50)
        addi_turtle.pendown()
        addi_turtle.penup()

addi_turtle.hideturtle()  # Hide the turtle
screen = Screen()  # Create a screen object
screen.exitonclick()  # Exit the screen on click
