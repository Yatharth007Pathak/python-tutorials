class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.name = brand

class Fortuner(ToyotaCar):
    def __init__(self, brand, type):
        super().__init__(brand)  # Call the initializer of the superclass
        self.type = type

car1 = Fortuner("Toyota", "diesel")

print(car1.name)  # Prints: Toyota
print(car1.type)  # Prints: diesel
car1.start()      # Prints: car started...



# SinglMulti-level inheritance


'''
Let's break down the given Python code, focusing on class inheritance, instance attributes, and the use of static methods.

Base Class Car:
class Car:: Defines a base class named Car.
@staticmethod: Decorator to define a static method.
def start():: Defines a static method start that prints "car started...".
def stop():: Defines a static method stop that prints "car stopped...".
Static methods do not require an instance to be called and do not have access to the instance (self) or class (cls) attributes.

Intermediate Class ToyotaCar:
class ToyotaCar(Car):: Defines a class ToyotaCar that inherits from the base class Car.
def __init__(self, brand):: Defines the initializer method (constructor) which takes brand as a parameter.
self.name = brand: Initializes the instance attribute name with the value provided during instantiation.

Derived Class Fortuner:
class Fortuner(ToyotaCar):: Defines a class Fortuner that inherits from the class ToyotaCar.
def __init__(self, type):: Defines the initializer method (constructor) which takes type as a parameter.
self.type = type: Initializes the instance attribute type with the value provided during instantiation.
Note: This definition does not call the initializer of the superclass ToyotaCar, so the name attribute from ToyotaCar is not initialized.

Creating an Instance:
car1 = Fortuner("diesel"): Creates an instance of the Fortuner class named car1 with the type attribute set to "diesel".

Accessing Attributes and Methods:
print(car1.type): Prints the type attribute of car1, which is "diesel".
car1.start(): Calls the start static method from the Car class. It prints "car started...".

Detailed Breakdown
Let's walk through the code step by step:

Class Definitions:
Car: The base class with static methods start and stop.
ToyotaCar: The intermediate class that inherits from Car and has an initializer to set the name attribute.
Fortuner: The derived class that inherits from ToyotaCar and has an initializer to set the type attribute.

Instance Creation:
car1: An instance of Fortuner with the type attribute set to "diesel". 
However, the name attribute from ToyotaCar is not initialized because the initializer of ToyotaCar is not called.

Method and Attribute Access:
car1.type: Accesses the type attribute of car1, prints "diesel".
car1.start(): Calls the static method start of the base class Car, prints "car started...".
'''