"""
In this program we explore some basic code of Object Oriented Programming Paradigm
and with the help of examples understand how it works

Taking the example from oops_basic.py the car example continues and we explore more new topics

Done by Adeeb Imam (2nd of Oct 2024)
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__speed = 0  # Private attribute

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

car1 = Car("Toyota","corolla","2024")
car1.accelerate()
car1.accelerate()
car1.accelerate()
print(f"The speed of the {car1.make} is {car1.get_speed()}")




    