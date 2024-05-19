"""
This program introduces us to a new concept known as lists. 

Lists are fundamental for storing and manipulating ordered collections of data in programs.

In this program we will add a bunch of name to a list and then random pick a name that is going to
pay for the bill

Done By Adeeb Imam
Date 19th May 2024
"""

import random

names = []

while True:
  name = input("Enter a name (or press Enter to finish): ")

  if not name:  # Check if user pressed Enter (empty input)
    break

  names.append(name)  # Add the entered name to the list

if not names:
  print("No names entered. Nobody pays!")
else:
  # Select a random index from the list
  random_index = random.randint(0, len(names) - 1)

  # Get the name at the random index
  payer_name = names[random_index]

  # Announce the result
  print(f"{payer_name} pays for the food bill!")

