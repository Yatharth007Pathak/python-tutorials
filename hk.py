class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)


'''
Let's break down the given Python code step by step, focusing on the use of class attributes and creating an instance of the class.

Class Definition and Class Attributes:
class Car:: Defines a new class named Car.
color = "blue": A class attribute shared by all instances of the Car class. This attribute is associated with the class itself, not with any particular instance.
brand = "mercedes": Another class attribute shared by all instances of the Car class.

Creating an Instance:
car1 = Car()
This line creates an instance of the Car class named car1.
Since no __init__ method is defined, Python uses a default constructor which does nothing special other than create the instance.

Accessing Class Attributes:
print(car1.color): This line prints the color attribute of the car1 instance. 
Since color is a class attribute, it is accessed through the instance car1.
print(car1.brand): This line prints the brand attribute of the car1 instance. 
Similarly, since brand is a class attribute, it is accessed through the instance car1.

Summary
Class Definition: The Car class is defined with class attributes color and brand.
Class Attributes: color and brand are shared across all instances of the Car class. 
These attributes are associated with the class itself and can be accessed through any instance of the class.
Instance Creation: An instance car1 is created using the default constructor.
Accessing Class Attributes: The class attributes color and brand are accessed and printed through the car1 instance.
'''