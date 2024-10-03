"""
In this program we explore some basic code of Object Oriented Programming Paradigm
and with the help of examples understand how it works

Taking the example from oops_basic.py to oops_basic_5.py, we will using car and car parts as an example to explain the concept of composition

(
    Composition is a design principle where a class is composed of one or more objects from other classes.
    It allows objects to contain other objects, forming a "has-a" relationship.
    It's different from inheritance (which represents "is-a" relationships) and promotes modular, reusable code.
)

Done by Adeeb Imam (2nd of Oct 2024)
"""

#Class Wheel
class Wheel:
    def __init__(self, wheel):
        self.wheel = wheel
    def start(self):
        return f"The vehicle has {self.wheel} wheels "

# Class Engine
class Engine:
    
    def __init__(self,horsepower):
        self.horsepower = horsepower
    def start(self):
        return "Engine starts with horspower: " + str(self.horsepower)

#Class Car
class Car:
    def __init__(self,make,model,horsepower,wheel):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheel = Wheel(wheel)
    
    def start(self):
        return f"{self.make} {self.model} is starting \n{self.engine.start()}\n{self.wheel.start()}"
    
car = Car("Toyota", "Corolla", 130, 4)

print(car.start())

