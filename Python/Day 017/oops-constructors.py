"""
The constructor allows the object to have pre-filled or pre-required
values when an object is created. This helps us to remove redundancy 
and make our code less error-prone
"""

class User:
    def __init__(self, name, number):   #This is the structure to a constructor
        self.name = name #This information is required from the user
        self.number = number #This information is required from the user
        self.followers = 0 #This information is not required from the user


user_1 = User("Adeeb", 21)
print(user_1.name)
print(user_1.number)

user_2 = User("Imam", 12)
print(user_2.name)
print(user_2.number)

print(f"The user {user_1.name} has {user_1.followers} followers")
print(f"The user {user_2.name} has the number {user_2.number}.")
