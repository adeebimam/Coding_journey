'''
This program checks if the year entered is leap year or not

Done by Adeeb Imam on 19th May 2024
'''

#Greeting for the program
year = input("Greetings please enter the year you want to check for leap year: ")
year = int(year)

#check if the year given by the user is a leap year or not

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
