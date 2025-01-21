"""
An attribute is a variable associated witht he object, it is like
creating a variable but associtating it with the object. This is
what the object has
"""
#creating a class
class User:
    pass       

#creating an object
user_1 = User()
user_1.name = "adeeb" #Creating a name variable only and only for user 1
user_1.age = 21 #Creating a age variable only and only for user 1

user_2 = User()

user_2.number = 1122

"""
Now the user 1 only has the varibales for name and age, and only 
user 2 has the varibales for number
"""

print (user_1.name)
print (user_1.age)
print (user_2.number)