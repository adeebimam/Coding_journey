"""
This program has a certain number of pre-determined words that are not told to the user,
the user then tries to guess each letter of the word and then checks how close or far he/she is
to the actual word.

Done By Adeeb Imam
Date 27th May 2024
"""

import random

# Lists of words, categories, and hints
words = [
    "Paris", "London", "Tokyo", "Sydney", "Cairo",
    "Berlin", "Madrid", "Moscow", "Toronto", "Dubai",
    "Elephant", "Kangaroo", "Dolphin", "Giraffe", "Penguin",
    "Cheetah", "Koala", "Octopus", "Peacock", "Porcupine",
    "Bicycle", "Laptop", "Telescope", "Backpack", "Umbrella",
    "Microwave", "Piano", "Suitcase", "Camera", "Table",
    "Chair", "Window", "Refrigerator", "Television", "Clock",
    "Lamp", "Bottle", "Mirror", "Telephone", "Printer",
    "Notebook", "Scissors", "Calculator", "Headphones", "Keyboard",
    "Toaster", "Blender", "Helmet", "Flashlight", "Glasses"
]

categories = [
    "place", "place", "place", "place", "place",
    "place", "place", "place", "place", "place",
    "animal", "animal", "animal", "animal", "animal",
    "animal", "animal", "animal", "animal", "animal",
    "thing", "thing", "thing", "thing", "thing",
    "thing", "thing", "thing", "thing", "thing",
    "thing", "thing", "thing", "thing", "thing",
    "thing", "thing", "thing", "thing", "thing",
    "thing", "thing", "thing", "thing", "thing",
    "thing", "thing", "thing", "thing", "thing"
]

hints = [
    "Capital of France", "Capital of the United Kingdom", "Capital of Japan", "Famous for its Opera House", "Capital of Egypt",
    "Capital of Germany", "Capital of Spain", "Capital of Russia", "Largest city in Canada", "Famous city in UAE",
    "Large mammal with a trunk", "Marsupial native to Australia", "Intelligent marine mammal", "Tallest land animal", "Flightless bird living in the Antarctic",
    "Fastest land animal", "Tree-dwelling marsupial from Australia", "Eight-armed sea creature", "Bird known for its colorful feathers", "Rodent with sharp quills",
    "Two-wheeled mode of transportation", "Portable computer", "Instrument to observe distant objects", "Bag carried on the back", "Used for protection against rain",
    "Appliance to heat food quickly", "Keyboard musical instrument", "Used to carry clothes while traveling", "Device to take photographs", "Piece of furniture with a flat top",
    "Piece of furniture to sit on", "Transparent opening in a wall", "Appliance to keep food cold", "Device to watch shows and movies", "Device to tell time",
    "Device to provide light", "Container to hold liquids", "Reflective surface", "Device to make voice calls", "Device to print documents",
    "Book of blank pages for writing", "Tool for cutting", "Device to perform arithmetic operations", "Device to listen to audio", "Input device for typing",
    "Appliance to toast bread", "Appliance to mix ingredients", "Protective headgear", "Portable hand-held electric light", "Worn to correct vision"
]

# ASCII art for hangman
hangman_pics = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

# Randomly select a word and its corresponding category and hint
index = random.randint(0, len(words) - 1)
word_chosen = words[index]
category = categories[index]
hint = hints[index]

# Print welcome message and hints
print("Welcome to the word guessing game!")
print(f"Hint 1: The word is related to a {category}.")
print(f"Hint 2: {hint}")

# Initialize display with underscores
display = ["_"] * len(word_chosen)
print(" ".join(display))

lives = 6  # Set the number of lives
running = True

# Game loop
while running:
    print(f"You have {lives} lives remaining")
    print(hangman_pics[6 - lives])
    word_input = input("Please enter a letter: ").lower()

    # Check if the guessed letter is in the chosen word
    if word_input in word_chosen.lower():
        for position in range(len(word_chosen)):
            if word_chosen[position].lower() == word_input:
                display[position] = word_chosen[position]
    else:
        lives -= 1  # Reduce lives if the guess is incorrect
        if lives == 0:
            print(hangman_pics[6])
            print("You have lost the game. The word was:", word_chosen)
            break

    # Print the current state of the word
    print(" ".join(display))

    # Check if the player has won
    if "_" not in display:
        print("\nYou have won!")
        break
