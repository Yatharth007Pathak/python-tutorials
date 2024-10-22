class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

dog1 = Dog()
cat1 = Cat()

make_animal_speak(dog1)  # Output: Woof!
make_animal_speak(cat1)  # Output: Meow!



# Polymorphism



'''
This code demonstrates the concept of inheritance and polymorphism in object-oriented programming using Python. 
Here's a breakdown of each part of the code:

Defining the base class Animal:
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
The Animal class serves as a base class (or abstract class).
It contains a method speak that raises a NotImplementedError. 
This indicates that any subclass of Animal must provide an implementation for the speak method.

Defining the Dog class:
class Dog(Animal):
    def speak(self):
        return "Woof!"
The Dog class inherits from the Animal class.
It overrides the speak method to return the string "Woof!".

Defining the Cat class:
class Cat(Animal):
    def speak(self):
        return "Meow!"
The Cat class also inherits from the Animal class.
It overrides the speak method to return the string "Meow!".

Defining a function to make an animal speak:
def make_animal_speak(animal):
    print(animal.speak())
This function takes an object animal as a parameter.
It calls the speak method of the animal object and prints the result.

Creating instances of Dog and Cat:
dog1 = Dog()
cat1 = Cat()
dog1 is an instance of the Dog class.
cat1 is an instance of the Cat class.

Calling the function with different animal objects:
make_animal_speak(dog1)
make_animal_speak(cat1)
The make_animal_speak function is called with dog1 and cat1 as arguments.
When called with dog1, the function prints "Woof!".
When called with cat1, the function prints "Meow!".

Summary:
Inheritance: Dog and Cat classes inherit from the Animal class.
Polymorphism: Both Dog and Cat classes implement the speak method differently.
Abstraction: The Animal class provides an abstract method speak that must be implemented by any subclass.
Encapsulation: The speak method's implementation details are hidden within each subclass.
'''