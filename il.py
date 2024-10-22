class Person:
    name = "yatharth"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("pathak")

print(p1.name)
print(Person.name)


'''
Let's break down the updated code, focusing on the difference between class attributes and instance attributes in Python.

Class Definition and Attribute:
class Person:: Defines a class named Person.
name = "yatharth": A class attribute name with the value "yatharth". 
This attribute is shared among all instances of the class unless an instance attribute with the same name is set.

Instance Method changeName:
def changeName(self, name):: Defines an instance method changeName that takes self (the instance itself) and name as parameters.
self.name = name: Sets an instance attribute name to the value provided. 
This does not change the class attribute but creates a new attribute specific to the instance.

Creating an Instance:
p1 = Person(): Creates an instance of the Person class named p1.

Modifying the Instance Attribute via an Instance Method:
p1.changeName("pathak"): Calls the changeName method on the instance p1, setting an instance attribute name to "pathak".

Accessing the Attributes via an Instance and the Class:
print(p1.name): Prints the value of the instance attribute name for p1, which is "pathak".
print(Person.name): Prints the value of the class attribute name of the Person class, which remains "yatharth".

Detailed Breakdown

Class Definition:
Person: A class with a class attribute name set to "yatharth".

Instance Method:
changeName: An instance method that sets an instance attribute name.

Instance Creation:
p1: An instance of the Person class.

Modifying the Instance Attribute:
p1.changeName("pathak"): Calls the changeName method on p1, setting self.name (which is p1.name) to "pathak".

Accessing the Attributes:
p1.name: Accesses the instance attribute name, which is now "pathak".
Person.name: Accesses the class attribute name directly from the class, which remains "yatharth".

Summary
Class Attribute: name is a class attribute shared among all instances of the Person class unless overridden by an instance attribute.
Instance Attribute: An instance attribute name is created when self.name = name is executed in the changeName method.
Attribute Modification: Modifying an instance attribute does not affect the class attribute.
Accessing Attributes: Instance attributes take precedence over class attributes when accessed via an instance. 
Class attributes can be accessed directly from the class.
'''