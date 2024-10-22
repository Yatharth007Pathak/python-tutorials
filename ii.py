class Person:
    name = "yatharth"  # Class attribute

    def changeName(self, name):
        Person.name = name  # Modify the class attribute

p1 = Person()  # Create an instance of Person
p1.changeName("pathak")  # Change the class attribute 'name' to 'pathak'

print(p1.name)  # Access and print the class attribute via the instance
print(Person.name)  # Access and print the class attribute via the class



'''
class method:- A class method is bound to the class and receives the classs as an implicit first argument.
Note- static method can't access or modify class state and generally for utility.

class Student:
    @classmethod             #decorator
    def college(cls):
        pass
'''


'''
Let's break down the provided code, focusing on class attributes and instance methods in Python.

Class and Instance Definition
class Person:: Defines a class named Person.
name = "yatharth": A class attribute name with the value "yatharth". This attribute is shared among all instances of the class.

Instance Method changeName:
def changeName(self, name):: Defines an instance method changeName that takes self (the instance itself) and name as parameters.
Person.name = name: Modifies the class attribute name of the Person class to the new value provided.

Creating an Instance:
p1 = Person(): Creates an instance of the Person class named p1.

Modifying the Class Attribute via an Instance Method:
p1.changeName("pathak"): Calls the changeName method on the instance p1, changing the class attribute name to "pathak".

Accessing the Class Attribute via an Instance and the Class:
print(p1.name): Prints the value of the class attribute name accessed through the instance p1, which is "pathak".
print(Person.name): Prints the value of the class attribute name accessed directly through the class Person, which is also "pathak".

Detailed Breakdown

Class Definition:
Person: A class with a class attribute name set to "yatharth".

Instance Method:
changeName: An instance method that changes the class attribute name.

Instance Creation:
p1: An instance of the Person class.

Modifying the Class Attribute:
p1.changeName("pathak"): Calls the changeName method on p1, setting Person.name to "pathak".

Accessing the Class Attribute:
p1.name: Accesses the modified class attribute name, which is now "pathak".
Person.name: Accesses the class attribute name directly from the class, which is also "pathak".

Summary
Class Attribute: name is a class attribute, meaning it is shared among all instances of the Person class.
Instance Method: The changeName method changes the class attribute name.
Class Attribute Modification: Modifying the class attribute via an instance method affects all instances of the class.
Accessing Class Attributes: Class attributes can be accessed via an instance or directly through the class.
'''