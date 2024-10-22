from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog1 = Dog()
cat1 = Cat()

print(dog1.speak())  # Output: Woof!
print(cat1.speak())  # Output: Meow!

'''
Let's break down the given Python code step by step, focusing on the use of abstract classes, inheritance, and method overriding.

Importing the ABC and abstractmethod from the abc Module:
from abc import ABC, abstractmethod: Imports the ABC class and the abstractmethod decorator from the abc module.
ABC is the base class for defining abstract base classes in Python.
abstractmethod is a decorator used to define abstract methods.

Defining the Abstract Base Class Animal:
class Animal(ABC): Defines an abstract base class named Animal that inherits from ABC.
@abstractmethod: Decorator that indicates speak is an abstract method.
def speak(self):: Defines the abstract method speak. This method does not provide an implementation, just the signature.
pass: Indicates that this method does not contain any code.

Defining the Dog Class:
class Dog(Animal): Defines a class named Dog that inherits from the Animal class.
def speak(self):: Provides the implementation of the speak method for the Dog class.
return "Woof!": When speak is called on a Dog instance, it returns the string "Woof!".

Defining the Cat Class:
class Cat(Animal): Defines a class named Cat that inherits from the Animal class.
def speak(self):: Provides the implementation of the speak method for the Cat class.
return "Meow!": When speak is called on a Cat instance, it returns the string "Meow!".

Creating Instances and Calling the speak Method:
dog1 = Dog(): Creates an instance of the Dog class named dog1.
cat1 = Cat(): Creates an instance of the Cat class named cat1.
print(dog1.speak()): Calls the speak method on the dog1 instance and prints the result. It outputs: Woof!.
print(cat1.speak()): Calls the speak method on the cat1 instance and prints the result. It outputs: Meow!.

Summary
Abstract Base Class: Animal is an abstract base class with an abstract method speak. 
This means any subclass of Animal must implement the speak method.
Inheritance and Method Overriding: Dog and Cat are subclasses of Animal that provide specific implementations of the speak method.
Instance Creation and Method Calls: Instances of Dog and Cat are created, 
and their respective speak methods are called to produce the expected output.
'''