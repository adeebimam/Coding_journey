"""
This Python project uses the turtle graphics module to create a simple drawing.
A turtle named 'tom' is created, customized to look like a green turtle,
and then instructed to draw a square. The program also sets up a screen that
waits for a mouse click to close, allowing the user to view the drawing.

In this project we also deal with the concept of Object-Oriented Programming.

Done By Adeeb Imam
Date 29th June 2024

"""
from turtle import Turtle, Screen

tom = Turtle()

tom.shape("turtle")
tom.color("green")
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(90)
tom.forward(100)


my_screen = Screen()
my_screen.exitonclick()

