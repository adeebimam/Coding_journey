"""
In this program we play a game where the user would guess a random number
that is chosen by the computer and the game has 2 level of difficulty 
hard and easy, the hard level has only 5 lives and the easy level has 10 lives

Done By Adeeb Imam
Date 3rd June 2024
"""

import random

max_num = 100

def lives(diff):
    if diff == "hard":
        lives = 5
    elif diff == "easy":
        lives = 10
    return lives

print("\nGreetings welcome to the guess the number game!")

difficulty = input("Please input the difficulty level that you would like to play on: ").lower()

game_live = lives(difficulty)

random_num = random.randint(1,max_num)

while game_live != 0:
    print("\n")
    if game_live == 1:
        print(f"You have {game_live} life remaining")
    else:
        print(f"You have {game_live} lives remaining")

    num = int(input("Please select a number between 1-100: "))
    
    if num == random_num:
        print(f"congratulations you have won the game, with {game_live} remaining lives and the number was {random_num}")
        break

    elif num >= random_num:
        print("It is too high")
        game_live-=1
        
    
    elif num <= random_num:
        print("It is too low")
        game_live-=1
        
    

if game_live == 0:
    print(f"\nYou have lost the game, the number was {random_num}")
    








