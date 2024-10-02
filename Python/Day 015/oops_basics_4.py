"""
In this program we explore some basic code of Object Oriented Programming Paradigm
and with the help of examples understand how it works

Taking the example from oops_basic.py to oops_basic_3.py, we will using animal example to explain he concept of polymorphism

(
    Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
    It lets methods in different classes have the same name but behave differently based on the object calling the method.
)

Done by Adeeb Imam (2nd of Oct 2024)
"""

# Parent class
class Animal:
    def sound(self):
        return "Some sound"
    def appearance(self):
        return "Some physical attribute"

# Child classes
class Dog(Animal):
    def sound(self):
        return "Bark"
    def appearance(self):
        return "Is a dog and is very friendly"

class Cat(Animal):
    def sound(self):
        return "Meow"
    def appearance(self):
        return "Is a cat and is very small"
    
class Cow(Animal):
    def sound(self):
        return "Moo"
    def appearance(self):
        return "Is a cow and is very big"

# Function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.sound())

def animal_appearance(animal):
    print(animal.appearance())

# Creating instances of each class
dog = Dog()
cat = Cat()
cow = Cow()
# Polymorphism in action
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
animal_sound(cow)
print("\n")
animal_appearance(dog)
animal_appearance(cat)
animal_appearance(cow)
