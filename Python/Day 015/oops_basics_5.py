"""
In this program we explore some basic code of Object Oriented Programming Paradigm
and with the help of examples understand how it works

Taking the example from oops_basic.py to oops_basic_3.py, we will using animal example to explain the concept of abstraction

(
    Abstraction is the concept of hiding complex implementation details and showing only the essential features of an object. 
    It helps reduce complexity and increase efficiency by exposing only relevant data and functionality.
)

Done by Adeeb Imam (2nd of Oct 2024)
"""

from abc import ABC, abstractmethod
import math

#Abstract Class
class Shapes(ABC):
    @abstractmethod
    def area(self):
        pass

#subclass for a square
class Square(Shapes):
    def __init__(self, side):
        self.side = side
        self.__name = "Square"
    def area(self):
        return self.side*self.side
    def name(self):
        return self.__name

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
        self.__name = "Circle"
    def area(self):
        return math.pi*self.radius*self.radius
    def name(self):
        return self.__name

    
object1 = Square(5)
object2 = Circle(6)

print(f"The area of {object1.name()} is {object1.area()}")
print(f"The area of {object2.name()} is {object2.area()}")
