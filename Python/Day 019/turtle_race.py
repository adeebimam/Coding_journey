# Import necessary modules
from turtle import Turtle, Screen  # For turtle graphics
from random import Random  # For generating random values

# Define colors for the turtles and initialize lists
color = ["violet", "indigo", "green", "blue", "orange", "red"]  # List of turtle colors
all_turtles = []  # List to store all turtle objects
position_y = [0, 60, -60, 120, -120]  # Y-axis positions for starting turtles

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)  # Set up the screen width and height

# Prompt the user to place a bet on a turtle color
user_bet = screen.textinput(title="Who is going to win?", 
                            prompt="Who is going to win the race? Enter a color. You can choose from violet, indigo, green, blue, orange ")
print(user_bet)  # Print the user's bet to the console

is_race_on = False  # Boolean to check if the race should start

# Check if the user has placed a bet
if user_bet:
    is_race_on = True  # Start the race only if a bet is placed

# Create turtle objects, assign colors, and position them
for turtle_index in range(0, 5):  # Loop through 5 turtles
    new_turtle = Turtle(shape="turtle")  # Create a turtle object
    new_turtle.color(color[turtle_index])  # Assign a unique color to each turtle
    new_turtle.penup()  # Lift the pen to avoid drawing a line during movement
    new_turtle.goto(x=-230, y=position_y[turtle_index])  # Position the turtle at the starting line
    all_turtles.append(new_turtle)  # Add the turtle to the list

# Start the race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle crosses the finish line
        if turtle.xcor() > 230:  # Finish line is at x = 230
            winning_color = turtle.pencolor()  # Get the winning turtle's color
            # Check if the user's bet matches the winning color
            if winning_color == user_bet:
                print(f"Congratulations you have won the game, your color was {user_bet} ")
            else:
                print(f"You have lost the game and the color that won is {winning_color} ")
            is_race_on = False  # End the race
        # Move the turtle forward by a random distance
        distance = Random().randint(0, 10)  # Generate a random distance between 0 and 10
        turtle.forward(distance)  # Move the turtle forward

# Close the screen when clicked
screen.exitonclick()
