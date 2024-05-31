"""
This program takes ask the user to input their fav things and then prints them out

Done By Adeeb Imam
Date 21st May 2024
"""

#Greeting the user at the start of the program
print("Welcome to the favorite things list")

#Asking the user to input their favorite things
fav_things_list = []

fav_thing1 = input("Enter your first favorite thing: ")
fav_thing2 = input("Enter your second favorite thing: ")
fav_thing3 = input("Enter your third favorite thing: ")

fav_things_list.append(fav_thing1)
fav_things_list.append(fav_thing2)
fav_things_list.append(fav_thing3)

print(f"Your fav things are \n{fav_things_list[0]}\n{fav_things_list[1]}\n{fav_things_list[2]}")