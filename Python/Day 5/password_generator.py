"""
This program is a passowrd generator that creates a password by asking how many letters, symbols, and number they would like to have

Done By Adeeb Imam
Date 22nd May 2024
"""



# Importing the random module to generate random selections
import random

# List of possible letters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# List of possible numbers for the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# List of possible symbols for the password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcoming user to the password generator
print("Welcome to the PyPassword Generator!")

# Asking the user for the number of letters, symbols, and numbers they want in their password
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# List to store password components
password_list = []

# Adding random letters to the password list
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)  # Choose a random letter
    password_list.append(random_char)  # Add the letter to the password list

# Adding random symbols to the password list
for sym in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)  # Choose a random symbol
    password_list.append(random_sym)  # Add the symbol to the password list

# Adding random numbers to the password list
for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)  # Choose a random number
    password_list.append(random_num)  # Add the number to the password list

# Shuffling the generated password list to ensure randomness
random.shuffle(password_list)

# Convert list to string to form the final password
password = ""
for keyword in password_list:
    password += keyword  # Concatenate each character to form the password

# Output the generated password
print(password)
