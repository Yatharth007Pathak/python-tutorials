class Car:
    def __init__(self):
        self.acltr = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acltr = True
        print("car started...")

car1 = Car()
car1.start()



# Abstraction:- hiding the implementation details of a class and  showing only the necessary features of an object to the user

'''
Let's break down the given Python code step by step, focusing on the class definition, instance attributes, and methods.

Class Definition and Initializer Method:
class Car:: Defines a new class named Car.
def __init__(self):: Defines the initializer method, also known as the constructor, which is called when a new instance of Car is created.
self.acltr = False: Initializes the instance attribute acltr (accelerator) to False.
self.brk = False: Initializes the instance attribute brk (brake) to False.
self.clutch = False: Initializes the instance attribute clutch to False.

Instance Method to Start the Car:
def start(self):: Defines an instance method start.
self.clutch = True: Sets the instance attribute clutch to True.
self.acltr = True: Sets the instance attribute acltr to True.
print("car started..."): Prints the message "car started..." to indicate the car has started.

Creating an Instance:
car1 = Car()
This line creates an instance of the Car class named car1.
The __init__ method is called, initializing car1.acltr to False, car1.brk to False, and car1.clutch to False.

Calling the start Method:
car1.start()
This line calls the start method on the car1 instance.
It sets car1.clutch to True and car1.acltr to True.
It prints: car started....

Summary
Class Definition: The Car class is defined with an initializer method and an instance method.
Instance Attributes: acltr, brk, and clutch are initialized in the __init__ method.
Instance Method: start sets clutch and acltr to True and prints a message.
Instance Creation: An instance car1 is created with initial values for acltr, brk, and clutch.
Method Call: The start method is called, which modifies the instance attributes and prints a message.
'''