class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def bark(self):  # Method
        print(f"{self.name} is barking!")

# Creating an object of the class
dog1 = Dog("Buddy", 3)
dog1.bark()  # Output: Buddy is barking!



# Classes and Objects