"""
In this program we explore some basic code of Object Oriented Programming Paradigm
and with the help of examples understand how it works

Taking the example from oops_basic.py and oops_basic_2.py the car example continues and we explore more new topics (inheritance)

(
    Inheritance allows one class (the child or derived class) to inherit the attributes and methods of another class 
    (the parent or base class). This promotes code reuse and creates a hierarchical relationship between classes.

)

Done by Adeeb Imam (2nd of Oct 2024)
"""

# Parent class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        return f"The {self.make} {self.model} is starting."

# Child class
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)  # Inherits attributes from Vehicle
        self.year = year
    
    def honk(self):
        return f"The {self.year} {self.make} {self.model} is honking."
    
# Child class

class MotorCycle(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model)
        self.year = year
        self.color = color

    def moving(self):
        return f"The {self.make} of {self.year} which is {self.color} is moving at high speed"

# Create an instance of Car
car1 = Car("Toyota", "Corolla", 2024)

# Using inherited and child class methods
print(car1.start())  # Inherited from Vehicle
print(car1.honk())   # Defined in Car

motorcycle1 = MotorCycle("Royal Enfield","Raptor","2024","black")
print(motorcycle1.start())
print(motorcycle1.moving())





    