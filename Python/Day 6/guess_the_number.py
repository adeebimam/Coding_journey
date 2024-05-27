# Importing the random library to generate random numbers.
import random

# Initializing the maximum number of guesses allowed.
max_guess = 5 

# Generating a random number between 1 and 100 to be guessed.
guess_num = random.randint(1, 100)

# Greeting the user and introducing the game.
print("Welcome to the guessing game!")

# Initialize game status to not won and set the trial count to zero.
game_won = False
trial = 0

# Start a while loop that runs as long as the game has not been won.
while not game_won:
    # Prompt the user to enter a guess and convert the input to an integer.
    user_guess_num = int(input("Please enter the number: "))  
    
    # Check if the user's guess is equal to the randomly generated number.
    if user_guess_num == guess_num:
        # Inform the user of winning and update game status to won.
        print("You have won the game!")
        game_won = True
    else:
        # Inform the user that the guess was incorrect.
        print("Incorrect answer, please try again")
        
        # Increment the trial count because the guess was wrong.
        trial += 1
        
        # Check if the number of trials has reached the maximum allowed guesses.
        if trial >= max_guess:
            # Inform the user that they've run out of guesses and end the game.
            print("You've used all your guesses. Game over!")
            break  # Exit the loop since the game is over either by winning or exceeding trials.
