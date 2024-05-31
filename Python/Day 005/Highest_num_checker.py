"""
In this program we check the highest number that has been inputed by the user
and then print that number out

Done by Adeeb Imam
Date 22nd May 2024
"""

#Greeting for the user at the start of the program
print("Welcome the highest number checker")

#Prompt to ask the user to enter the numbers
number = input("Please enter the numbers to check for the highest number, seprated by spaces: ").split() 

#changing the number from str to int
number = [int(num) for num in number]

#initalizing the hightest number variable
highest_number = 0 

#running through the loop to check for the highest possible number
for num in number:
    highest_number = 0 
    if num > highest_number:   #checking the highest possible number
        highest_number = num

print(f"The highest number that you have entered is: {highest_number}")