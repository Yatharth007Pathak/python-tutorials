class Car:
    def __init__(self, type):
        self.type = type  # Initialize instance attribute 'type'

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  # Call the initializer of the superclass (Car)
        self.name = name  # Initialize instance attribute 'name'
        super().start()  # Call the static method 'start' from the superclass

car1 = ToyotaCar("prius", "electric")  # Create an instance of ToyotaCar
print(car1.type)  # Access and print the 'type' attribute


# Super method:- super() method is used to access methods of the parent class


'''
Let's break down the provided code, focusing on class inheritance, instance initialization, and the use of static methods in Python.

Class Definitions and Inheritance
Base Class Car:
class Car:: Defines a base class named Car.
def __init__(self, type):: Defines the initializer method (constructor) which takes type as a parameter and 
initializes the instance attribute type.
@staticmethod: Decorator to define a static method.
def start():: Defines a static method start that prints "car started...".
def stop():: Defines a static method stop that prints "car stopped...".
Static methods do not require an instance to be called and do not have access to the instance (self) or class (cls) attributes.

Derived Class ToyotaCar:
class ToyotaCar(Car):: Defines a class ToyotaCar that inherits from the base class Car.
def __init__(self, name, type):: Defines the initializer method (constructor) which takes name and type as parameters.
super().__init__(type): Calls the initializer of the superclass (Car) to initialize the type attribute.
self.name = name: Initializes the instance attribute name.
super().start(): Calls the start static method from the Car class, which prints "car started...".

Creating an Instance:
car1 = ToyotaCar("prius", "electric"): Creates an instance of the ToyotaCar class named car1 
with the name attribute set to "prius" and the type attribute set to "electric".

Accessing Attributes:
print(car1.type)
print(car1.type): Prints the value of the type attribute from the car1 instance, which is "electric".

Detailed Breakdown

Class Definitions:
Car: A base class with an initializer to set the type attribute and two static methods, start and stop.
ToyotaCar: A derived class that inherits from Car. It has its own initializer to set the name attribute and calls the start method from the Car class.

Instance Creation:
car1: An instance of ToyotaCar with the name "prius" and the type "electric". During the initialization of car1, the type attribute is set by calling the Car initializer through super(), and the start static method is called, which prints "car started...".

Attribute Access:
car1.type: Accesses the type attribute of car1, which is "electric".

Summary
Inheritance: ToyotaCar inherits from Car.
Instance Initialization: The ToyotaCar class calls the initializer of the Car class using super() to set the type attribute. 
It also initializes its own name attribute.
Static Methods: Static methods start and stop from the Car class can be called without needing an instance.
'''