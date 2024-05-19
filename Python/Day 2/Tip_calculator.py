"""
This program calculates the tip that would be paid by each member of a group

done by Adeeb Imam on 19th May 2024
"""

# Creating a greeting for the program
print("Welcome to the tip calculator!\n")

# Asking the user to input the total price
total_price = float(input("Please enter the total price: "))

# Asking the user to input the tip percentage
tip_percentage = float(input("Please enter the tip you would like to give in %: "))

# Asking the user to input the number of people between which the price will be split
number_of_people = int(input("Please enter the number of people that the bill will be split between: "))

# Calculating the total price after adding the tip.
total_price_with_tip = total_price + (total_price * (tip_percentage / 100))

# Calculating the price that will be paid by each person
person_payment = total_price_with_tip / number_of_people

# Printing the payment each person will pay
print(f"Each person will pay ${person_payment:.2f}")
