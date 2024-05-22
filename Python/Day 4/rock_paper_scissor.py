"""
This program is a rock, paper, and scissors game where the
user chooses rock, paper or scissor and the computer also chooses
(randomly) and according the laws of the game the winner is announced

Done By Adeeb Imam
Date 22nd May 2024
"""

import random

#Assign the shapes of rock, paper, and scissor

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#Greeting for the user at the start of the program
("Welcome to the Rock, paper, and scissor game!")

#ask the user for the input to start the game
user_select = input("\nPlease choose from one of the following 0 for rock, 1 for paper and 2 for scissor: ")
user_select = int(user_select)

if user_select == 0:
    print(f"You choose rock\n{rock}")
elif user_select == 1:
    print(f"You choose paper\n{paper}")
else:
    print(f"You choose scissor\n{scissor}")

#Generating a random response from the computer
computer_select = random.randint(0,2)

if computer_select == 0:
    print(f"Computer choose rock\n{rock}")
elif computer_select == 1:
    print(f"Computer choose paper\n{paper}")
else:
    print(f"Computer choose scissor\n{scissor}")

#applying the laws of the game to declare the winner

if user_select == computer_select:
    print("It is a tie")
elif (user_select == 0 and computer_select == 1) or (user_select == 1 and computer_select == 2) or (user_select == 2 and computer_select == 0):
    print("Computer wins!")
else:
    print("You Win!")   