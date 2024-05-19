'''
This is the program that calculates the love when
two names are given

done by Adeeb Imam on 18/05/2024
'''

#Greetings for the program
print("Welcome to the love calculator")

#Asking the user the input the names
name_1 = input("Please enter the first name: ")
name_2 = input("Please enter the second name: ")

#combining the names
combined_names = name_1 + name_2
lower_combined_names = combined_names.lower()

t = lower_combined_names.count("t")
u = lower_combined_names.count("u")
r = lower_combined_names.count("r")
e = lower_combined_names.count("e")

first_digit = t + r + u + e

l = lower_combined_names.count("l")
o = lower_combined_names.count("o")
v = lower_combined_names.count("v")
e = lower_combined_names.count("e")

second_digit = l + o + v + e

love_score = int(str(first_digit) + str(second_digit))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")




