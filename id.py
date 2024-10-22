class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
car1.start()

print(car2.name)
car2.stop()
print(car2.color)

# Single inheritance

'''
Inheritance:- When one class (child/derived) derives the properties and methods of another class (parent/base)

class Car:                                              parent
    ....

class ToyotaCar(Car):                                   child
    ....


types of inheritance:-
Single inheritance (single parent class, single child class)
Multi-level inheritance (single parent class, single child class, single grandchild class and so on classes may nbebe derived)
Multiple inheritance (a single child class can inherit properties from multiple parent classes)
 '''

"""
Let's break down the provided code, focusing on class inheritance, instance attributes, and the use of static methods.

Base Class Car:
class Car:: Defines a base class named Car.
color = "black": A class-level attribute color with the value "black".
@staticmethod: Decorator to define a static method.
def start():: Defines a static method start that prints "car started...".
def stop():: Defines a static method stop that prints "car stopped...".
Static methods do not require an instance to be called and do not have access to the instance (self) or class (cls) attributes.

Derived Class ToyotaCar:
class ToyotaCar(Car):: Defines a derived class ToyotaCar that inherits from the base class Car.
def __init__(self, name):: Defines the initializer method (constructor) which takes name as a parameter.
self.name = name: Initializes the instance attribute name with the value provided during instantiation.

Creating Instances:
car1 = ToyotaCar("fortuner"): Creates an instance of ToyotaCar with the name attribute set to "fortuner".
car2 = ToyotaCar("prius"): Creates another instance of ToyotaCar with the name attribute set to "prius".

Accessing Attributes and Methods:
print(car2.color)
print(car1.name): Prints the name attribute of car1, which is "fortuner".
car1.start(): Calls the start static method from the Car class. It prints "car started...".
print(car2.name): Prints the name attribute of car2, which is "prius".
car2.stop(): Calls the stop static method from the Car class. It prints "car stopped...".
print(car2.color): Prints the color attribute, inherited from the Car class. The color is "black".

Detailed Breakdown
Let's walk through the code step by step:

Class Definitions:
Car: The base class with a class-level attribute color and two static methods, start and stop.
ToyotaCar: The derived class inheriting from Car and adding an initializer to set the name attribute.

Instance Creation:
car1: An instance of ToyotaCar with the name "fortuner".
car2: Another instance of ToyotaCar with the name "prius".

Method and Attribute Access:
car1.name: Accesses the name attribute of car1, prints "fortuner".
car1.start(): Calls the static method start of the base class Car, prints "car started...".
car2.name: Accesses the name attribute of car2, prints "prius".
car2.stop(): Calls the static method stop of the base class Car, prints "car stopped...".
car2.color: Accesses the class-level attribute color from the base class Car, prints "black".

Summary
Inheritance: ToyotaCar inherits from Car, allowing it to access class-level attributes and static methods of the base class.
Instance Attributes: Each instance of ToyotaCar has a name attribute set during initialization.
Static Methods: The start and stop methods can be called on instances of ToyotaCar because they are inherited from the Car class.
Class-level Attributes: The color attribute is a class-level attribute in Car and is inherited by ToyotaCar.
"""