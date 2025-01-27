# Import necessary modules
from turtle import Turtle, Screen  # Import Turtle for drawing and Screen for the window

# Create a turtle object for drawing and movement
addi_turtle = Turtle()

# Create a screen object to handle display and user input
screen = Screen()

# Define functions for turtle movements and actions
def fd():
    addi_turtle.fd(10)  # Move the turtle forward by 10 units

def bk():
    addi_turtle.bk(10)  # Move the turtle backward by 10 units

def right():
    addi_turtle.right(10)  # Turn the turtle 10 degrees to the right

def left():
    addi_turtle.left(10)  # Turn the turtle 10 degrees to the left

def clear():
    addi_turtle.reset()  # Reset the turtle to its starting position and clear the screen

# Set up the screen to listen for keyboard events
screen.listen()  # Activate the screen to listen for user input

# Bind keyboard keys to the respective functions
screen.onkey(key="w", fun=fd)  # Press "w" to move forward
screen.onkey(key="s", fun=bk)  # Press "s" to move backward
screen.onkey(key="a", fun=right)  # Press "a" to turn right
screen.onkey(key="d", fun=left)  # Press "d" to turn left
screen.onkey(key="c", fun=clear)  # Press "c" to clear the screen and reset the turtle

# Close the screen when the user clicks on it
screen.exitonclick()
