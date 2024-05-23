"""
In this program we will learn a new topic known as "while loop" and based on our understanding
of this topic we will build a program that would select a random number and then ask the user 
to guess that number, the user will have only 5 attempts to guess the number

A while loop is a programming construct that repeatedly executes a block of code 
as long as a certain condition remains true.

Done By Adeeb Imam
Date 23rd May 2024

"""

#Importing and initialzing all the necessary variables for the program

import random

max_guess = 5 
guess_num = random.randint(1, 100)

print("Welcome to the guessing game!")

game_won = False
trial = 0

while not game_won:
    user_guess_num = int(input("Please enter the number: "))  # Prompt moved inside the loop
    
    if user_guess_num == guess_num:
        print("You have won the game!")
        game_won = True
    else:
        print("Incorrect answer, please try again")
        trial += 1
        if trial >= max_guess:
            print("You've used all your guesses. Game over!")
            break





