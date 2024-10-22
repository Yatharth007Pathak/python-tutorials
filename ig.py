class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

print(dog1.speak())  # Output: Buddy says Woof!
print(cat1.speak())  # Output: Whiskers says Meow!

# Inheritance


'''
Let's break down the provided code, focusing on class inheritance, method overriding, and raising exceptions in Python.

Base Class Definition

Base Class Animal:
class Animal:: Defines a base class named Animal.
def __init__(self, name):: Defines the initializer method (constructor) which takes name as a parameter.
self.name = name: Initializes the instance attribute name with the value provided during instantiation.
def speak(self):: Defines a method speak that raises a NotImplementedError with the message "Subclass must implement abstract method".
NotImplementedError is used to indicate that subclasses must override this method.

Derived Classes
class Dog(Animal):: Defines a class Dog that inherits from the base class Animal.
def speak(self):: Overrides the speak method from the base class. This method returns a string with the dog's name followed by "says Woof!".
class Cat(Animal):: Defines a class Cat that inherits from the base class Animal.
def speak(self):: Overrides the speak method from the base class. This method returns a string with the cat's name followed by "says Meow!".

Creating Instances:
dog1 = Dog("Buddy"): Creates an instance of the Dog class named dog1 with the name attribute set to "Buddy".
cat1 = Cat("Whiskers"): Creates an instance of the Cat class named cat1 with the name attribute set to "Whiskers".

Calling Methods and Printing Results:
print(dog1.speak()): Calls the speak method on the dog1 instance. It returns and prints the string "Buddy says Woof!".
print(cat1.speak()): Calls the speak method on the cat1 instance. It returns and prints the string "Whiskers says Meow!".

Detailed Breakdown
Let's walk through the code step by step:

Class Definitions:
Animal: A base class with an initializer to set the name attribute and a speak method that raises a NotImplementedError.
Dog: A derived class that inherits from Animal and overrides the speak method to return a string specific to dogs.
Cat: A derived class that inherits from Animal and overrides the speak method to return a string specific to cats.

Instance Creation:
dog1: An instance of Dog with the name "Buddy".
cat1: An instance of Cat with the name "Whiskers".

Method Calls:
dog1.speak(): Calls the overridden speak method of the Dog class, which returns "Buddy says Woof!".
cat1.speak(): Calls the overridden speak method of the Cat class, which returns "Whiskers says Meow!".

Summary
Inheritance: Dog and Cat inherit from the Animal base class.
Method Overriding: Both Dog and Cat override the speak method from the Animal class to provide their own implementations.
Raising Exceptions: The speak method in the Animal class raises a NotImplementedError 
to ensure that subclasses provide an implementation for this method.
'''