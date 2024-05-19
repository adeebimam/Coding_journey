'''
This program is a pizza builder and makes different
size pizza

Done By Adeeb Imam 19th May 2024
'''

# Greeting the user at the start of the program
print("Welcome to our pizza making place")

total_price = 0

# Ask the user to input the size of pizza needed
pizza_size = input("Please let us know of the size of the pizza S,M and L: ")
pizza_size = pizza_size.lower()

if pizza_size == "s":

    total_price = 15
    add_pepperoni_small = input("Would you like to add some pepperoni in your pizza? ")
    add_pepperoni_small = add_pepperoni_small.lower()

    if add_pepperoni_small == "y":
        total_price = total_price + 2

elif pizza_size == "m":
    total_price = 20
else:
    total_price = 25

if pizza_size != "s":

    add_pepperoni = input("Would you like to add some pepperoni in your pizza? ")
    add_pepperoni = add_pepperoni.lower()

    if add_pepperoni == "y":
        total_price = total_price + 3

add_cheese = input("Would you like to add some cheese in your pizza? ")
add_cheese = add_cheese.lower()

if add_cheese == "y":
    total_price = total_price + 1

print(f"The pizza you have order is {pizza_size.upper()} and the cost is ${total_price} ")