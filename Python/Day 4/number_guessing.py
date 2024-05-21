"""
In this program we ask the user to input a number within a certain range and
then check if the number entered matches with the number we have in the list

Done by Adeeb Imam
Date 21st May 2024
"""

#Greeting the user at the start of the program
print("Welcome to the Number guessing game") 

#Assigning the selected numbers
selected_num = [1,2,3,4,5]

#Asking the user to input a number
input_num = input("Please enter a number between 1-10: ")
input_num = int(input_num)

#Checking if the number in the input matches
if input_num in selected_num:
    print("You have guessed a number within the list")
else:
    print("Sorry the number entered is not in the list")