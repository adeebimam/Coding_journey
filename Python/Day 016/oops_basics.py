"""
In this program we explore some basic code of Object Oriented Programming Paradigm
and with the help of examples understand how it works

This program defines a car class that models basic car attributes (brand, color, model)
and has certain behaviours (describe, start) and allows us to create more obejcts and
interact with the car

Done by Adeeb Imam (2nd of Oct 2024)
"""

#Defining a simple class known as car 
    #(class = A blueprint for creating objects (a definition of data and functions))

class car:
    #We use an constructor to initialize attributes
        # (constructor = initializes an object's attributes when a new instance of a class is created)
    def __init__(self, brand, model, color) -> None:
        self.brand = brand  #instance attribute
        self.model = model  #instance attribute 
        self.color = color  #instance attribute
    # Method to describe the car
        #(Method = Functions defined inside a class that descitbe the behaviour of an object)
    def describe(self):
        print(f"This car is a {self.brand} and is the model {self.model} and has the color {self.color} ")
    
    def start(self):
        print(f"The {self.brand} {self.model} is strating")
    

car1 = car("Toyota","corolla","red")
car2 = car("Honda","civic","Blue")

car1.describe()
car1.color="green"
car2.describe()
car1.describe()

car2.start()




    