"""
In this program we will create our own black jack game

Done By Adeeb Imam
Date 1st June 2024
"""
import random
import os

# List of possible card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to determine and print the winner
def winner(computer_sum, user_sum, computer_cards, user_cards):
    print(f"Your cards are {user_cards}, and your total score is {user_sum}") 
    print(f"Computer cards are {computer_cards}, and computer total score is {computer_sum}")  

    if computer_sum > 21:
        print("You have won the game")
    elif user_sum > 21:
        print("Computer has won the game")
    elif computer_sum < 21 and computer_sum > user_sum:
        print("Computer has won")
    elif computer_sum < 21 and computer_sum < user_sum:
        print("You have won")
    elif computer_sum == 21:
        print("Computer has won")
    elif computer_sum == user_sum:
        print("It is a draw")

# Function to select a random card from the deck
def card_selection():
    card = random.choice(cards)
    return card

# Function to calculate the sum of cards
def card_sum(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to check if the user wants to continue the game
def continue_game():
    continue_game = input("Would you like to continue the game (Y/N): ").lower()
    if continue_game == "y":
        clear_screen()
        return True
    elif continue_game == "n":
        clear_screen()
        return False

print("Greetings to the Black-Jack Game!")

running = True

# Initial prompt to start the game
game_start = input("Would you like to play a game? (Y/N): ").lower()

while running:
    if game_start == "y":
        user_cards = []
        computer_cards = []

        # Dealing initial cards to computer and user
        computer_card1 = card_selection()
        computer_cards.append(computer_card1)

        computer_card2 = card_selection()
        computer_cards.append(computer_card2)

        user_card1 = card_selection()
        user_cards.append(user_card1)

        user_card2 = card_selection()
        user_cards.append(user_card2)

        user_sum = card_sum(user_cards)
        computer_sum = card_sum(computer_cards)

        print(f"Your cards are: {user_cards}, your card score is {user_sum}")
        print(f"Computer card is: {computer_card1}")

        if user_sum < 21:
            add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_sum < 21 and add_card == "y":
                # User decides to take more cards
                while user_sum < 21 and add_card == "y":
                    new_card = card_selection()
                    user_cards.append(new_card)
                    user_sum = card_sum(user_cards)
                    print(f"Your cards are: {user_cards}, your card score is {user_sum}")
                    print(f"Computer card is: {computer_card1}")
                    if user_sum < 21:
                        add_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                if user_sum == 21 or user_sum > 21:
                    winner(computer_sum, user_sum, computer_cards, user_cards)
                    running = continue_game()

            elif user_sum < 21 and add_card == "n":
                # User decides to pass
                if computer_sum <= 17:
                    new_card_comp = card_selection()
                    computer_cards.append(new_card_comp)
                    computer_sum = card_sum(computer_cards)
                print(f"Your cards are: {user_cards}, your card score is {user_sum}")
                print(f"Computer cards are: {computer_cards}, computer card score is {computer_sum}")
                winner(computer_sum, user_sum, computer_cards, user_cards)
                running = continue_game()

        elif user_sum == 21 or user_sum > 21:
            # User already won or lost with initial cards
            winner(computer_sum, user_sum, computer_cards, user_cards)
            running = continue_game()
    
    else:
        running = False
