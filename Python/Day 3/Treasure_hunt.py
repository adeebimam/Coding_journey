"""
This project simulates a treasure hunt game. The user is given a set of choices throughout the game,
and must select the correct options to proceed and ultimately win the game.

Done by: Adeeb Imam
Date: 18/05/2024
"""

# Print a welcome message to greet the player.
print("Welcome to the treasure hunt!")

# Ask the player for their name to personalize interactions.
name = input("Please enter your name: ")

# Ask the player to choose a direction to start the game.
move1 = input("Where would you like to move? (left or right): ")
move1 = move1.lower()  # Convert the input to lower case to standardize the comparison.

# Validate the first move choice.
if move1 != "right" and move1 != "left":
    print("Invalid choice, please try again!")
elif move1 == "right":
    print("Game over")  # End the game if the wrong choice is made.
else:
    print("Congratulations! You have now moved to level 2")  # Proceed to the next level for the correct choice.

    # Ask the player the next choice in level 2.
    move2 = input("Would you like to wait or swim? ")
    move2 = move2.lower()  # Normalize input.

    # Validate the second move choice.
    if move2 != "swim" and move2 != "wait":
        print("Invalid choice, please try again!")
    elif move2 == "swim":
        print("Game over!")  # End the game if the wrong choice is made.
    else:
        print("Congratulations! You have now moved to level 3")  # Proceed to the next level for the correct choice.

        # In level 3, ask the player to choose one of three doors.
        move3 = input("You have 3 doors in front of you now, which one would you take? RED, GREEN, and BLUE: ")
        move3 = move3.lower()  # Normalize input.

        # Validate the third move choice.
        if move3 != "red" and move3 != "blue" and move3 != "green":
            print("Invalid choice, please try again!")
        elif move3 == "red" or move3 == "blue":
            print("You have lost the game")  # End the game if a wrong door is chosen.
        else:
            print("You have won the game!")  # The player wins the game by choosing the correct door.
