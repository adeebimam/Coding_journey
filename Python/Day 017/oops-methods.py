"""
Methods is what the object does. It basically acts the the function
for a class that can be performed by the object
"""

class user:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow (self, user):
        self.following += 1
        user.followers += 1

user_1 = user(1, "Adeeb")
user_2 = user (2, "Imam")

user_1.follow(user_2)

print(f"The name of the user is {user_1.user_name} and the user_id is {user_1.user_id}")
print(f"The name of the user is {user_2.user_name} and the user_id is {user_2.user_id}")
print(f"{user_1.user_name} has {user_1.followers} followers and {user_1.following} following")
print(f"{user_2.user_name} has {user_2.followers} followers and {user_2.following} following")

