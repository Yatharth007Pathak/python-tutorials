class Person:
    name = "yatharth"  # Class attribute

    @classmethod
    def changeName(cls, name):
        cls.name = name  # Modify the class attribute

p1 = Person()  # Create an instance of Person
p1.changeName("pathak")  # Change the class attribute 'name' to 'pathak'

print(p1.name)  # Access and print the class attribute via the instance
print(Person.name)  # Access and print the class attribute via the class



'''
Let's break down the provided code, focusing on the use of class methods and class attributes in Python.

Class Definition and Attribute:
class Person:: Defines a class named Person.
name = "yatharth": A class attribute name with the value "yatharth". This attribute is shared among all instances of the class.

Class Method changeName:
@classmethod: A decorator that defines a method as a class method. Class methods take cls as their first parameter, which refers to the class itself.
def changeName(cls, name):: Defines a class method changeName that takes cls (the class itself) and name as parameters.
cls.name = name: Modifies the class attribute name of the cls (which refers to the Person class) to the new value provided.

Creating an Instance:
p1 = Person(): Creates an instance of the Person class named p1.

Modifying the Class Attribute via a Class Method:
p1.changeName("pathak"): Calls the changeName class method on the instance p1, changing the class attribute name to "pathak". Note that class methods can be called on an instance, and they still modify the class attributes.

Accessing the Class Attribute via an Instance and the Class:
print(p1.name): Prints the value of the class attribute name accessed through the instance p1, which is "pathak".
print(Person.name): Prints the value of the class attribute name accessed directly through the class Person, which is also "pathak".

Detailed Breakdown

Class Definition:
Person: A class with a class attribute name set to "yatharth".

Class Method:
changeName: A class method that changes the class attribute name using cls.

Instance Creation:
p1: An instance of the Person class.

Modifying the Class Attribute:
p1.changeName("pathak"): Calls the changeName class method on p1, setting cls.name (which is Person.name) to "pathak".

Accessing the Class Attribute:
p1.name: Accesses the modified class attribute name, which is now "pathak".
Person.name: Accesses the class attribute name directly from the class, which is also "pathak".

Summary
Class Attribute: name is a class attribute, meaning it is shared among all instances of the Person class.
Class Method: The changeName class method changes the class attribute name using cls.name.
Class Attribute Modification: Modifying the class attribute via a class method affects all instances of the class.
Accessing Class Attributes: Class attributes can be accessed via an instance or directly through the class.
'''