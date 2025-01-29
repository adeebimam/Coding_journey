"""
A simple interactive program that moves a turtle forward when the "space" key is pressed:

Screen Methods: listen() activates key listening, and onkey() binds the key to the movement function.
Demonstrates basic event handling and user interaction.

AI 27/01/2025
"""

# Import necessary modules
from turtle import Turtle, Screen  # Import Turtle for drawing and Screen for the window

# Create a turtle object named 'addi'
addi = Turtle()  # This turtle will be used for drawing and movement

# Create a screen object to control the display and user interactions
screen = Screen()

# Define a function to move the turtle forward
def turtle_mov():
    addi.forward(50)  # Move the turtle forward by 50 units

# Set up the screen to listen for keyboard events
screen.listen()  # Activates the screen to listen for user input

# Bind the "space" key to the turtle_mov function
screen.onkey(key="space", fun=turtle_mov)  
# When the "space" key is pressed, the turtle_mov function will execute

# Close the screen when the user clicks on it
screen.exitonclick()
