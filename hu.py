class Dog:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def bark(self):
        print(f"{self.__name} is barking!")

    def get_age(self):
        return self.__age

dog1 = Dog("Buddy", 3)
print(dog1.get_age())  # Output: 3



# Encapsulation:- Wrapping data and fuctions into a single unit (object)

"""
 Let's break down the given Python code step by step, focusing on encapsulation with private attributes, instance methods, and accessing these attributes through methods.

Class Definition and Initializer Method:
class Dog:: Defines a new class named Dog.
def __init__(self, name, age):: Defines the initializer method, also known as the constructor, which is called when a new instance of Dog is created.
self.__name = name: Initializes the private instance attribute __name with the value provided during instantiation.
self.__age = age: Initializes the private instance attribute __age with the value provided during instantiation.
The double underscore __ prefix makes these attributes private, meaning they cannot be accessed directly from outside the class.

Instance Method bark:
def bark(self):: Defines an instance method bark.
print(f"{self.__name} is barking!"): This line prints a message indicating that the dog (referenced by self.__name) is barking.
The method accesses the private attribute __name from within the class.

Instance Method get_age:
def get_age(self):: Defines an instance method get_age.
return self.__age: This line returns the value of the private attribute __age.
This method provides controlled access to the private attribute __age from outside the class.

Creating an Instance:
dog1 = Dog("Buddy", 3)
This line creates an instance of the Dog class named dog1 with the name "Buddy" and age 3.
The __init__ method is called, setting dog1.__name to "Buddy" and dog1.__age to 3.

Calling the get_age Method:
print(dog1.get_age())
This line calls the get_age method on the dog1 instance.
It returns the value of the private attribute __age, which is 3.
print(dog1.get_age()) prints: 3.

Summary
Class Definition: The Dog class is defined with an initializer method, two private attributes, and two instance methods.
Private Attributes: __name and __age are private attributes, 
prefixed with double underscores to indicate they should not be accessed directly from outside the class.
Instance Methods: bark prints a message using the private attribute __name, and get_age returns the value of the private attribute __age.
Instance Creation: An instance dog1 is created with initial values for __name and __age.
Method Call: The get_age method is called to access the private attribute __age.
"""