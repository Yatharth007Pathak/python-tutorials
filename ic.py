class Person:
    __name = "yatharth"  # Private class-level attribute

    def __hello(self):
        print("hello person!")  # Private instance method

    def welcome(self):
        self.__hello()  # Public method calling the private method

p1 = Person()

print(p1.welcome())




'''
Let's break down the given Python code, focusing on how private attributes and methods work, and how they can be accessed within a class.

Class Definition:
class Person:: Defines a new class named Person.
__name = "yatharth": Defines a class-level private attribute __name. The double underscore __ prefix makes __name a private attribute.

Private Method:
def __hello(self):: Defines a private instance method __hello. The double underscore __ prefix makes __hello a private method.
print("hello person!"): This line prints "hello person!" when __hello is called.

Public Method:
def welcome(self):: Defines a public instance method welcome.
self.__hello(): This line calls the private method __hello from within the class. 
This is allowed because private members can be accessed within the class they are defined in.

Creating an Instance:
p1 = Person()
This line creates an instance of the Person class named p1.

Calling the Public Method:
p1.welcome(): Calls the welcome method on the instance p1.
Within welcome, the private method __hello is called, which prints "hello person!".
The welcome method does not return any value (implicitly returns None).
print(p1.welcome()): Prints the return value of p1.welcome(), which is None.

Detailed Breakdown

Let's walk through the code execution step by step:

Class Definition:
The Person class is defined with a private class-level attribute __name and a private instance method __hello.
A public instance method welcome is also defined, which calls the private method __hello.

Instance Creation:
An instance p1 of the Person class is created.

Calling the Public Method:
p1.welcome():
Calls the welcome method on p1.
Inside welcome, self.__hello() calls the private method __hello, which prints "hello person!".
Since welcome does not return a value, it implicitly returns None.
print(p1.welcome()):
Calls p1.welcome() again, which prints "hello person!" and then returns None.
The print function then prints this return value, which is None.

Summary
Private Members: The Person class has a private class-level attribute __name and a private method __hello.
Accessing Private Methods: The private method __hello can be accessed within the class via the public method welcome.
Instance Method Calls: p1.welcome() calls the private method __hello and prints a message, 
and since welcome returns None, print(p1.welcome()) prints None.
'''