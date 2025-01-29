"""
In this program, we will draw a dashed line using turtle graphics.
Different methods will be used in order to draw the dashed line.
Difficulty: Easy

AI 23/01/2025
"""

from turtle import Turtle as t, Screen

addi_turtle = t()
addi_turtle.shape("turtle")

for i in range(10):
    addi_turtle.color("blue")
    addi_turtle.forward(10)
    addi_turtle.penup()
    addi_turtle.forward(10)
    addi_turtle.pendown()




screen = Screen()
screen.exitonclick()