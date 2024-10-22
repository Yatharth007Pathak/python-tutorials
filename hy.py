class Account:
    def __init__(self, acc_no, acc_pword):
        self.acc_no = acc_no
        self.__acc_pword = acc_pword

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.__acc_pword)



'''
Private(like) attributes and methods
Conceptual implementations in python
Private attributes and methods are meant to be used only within the class and are not accessible from outside the class
'''

"""
Let's break down the given Python code, focusing on the use of private attributes and how they affect access to the instance's data.

Class Definition and Initializer Method:
class Account:: Defines a new class named Account.
def __init__(self, acc_no, acc_pword):: Defines the initializer method (constructor) which is called when a new instance of Account is created.
self.acc_no = acc_no: Initializes the instance attribute acc_no with the value provided during instantiation.
self.__acc_pword = acc_pword: Initializes the private instance attribute __acc_pword with the value provided during instantiation.
The double underscore __ prefix makes __acc_pword a private attribute, meaning it cannot be accessed directly from outside the class.

Creating an Instance:
acc1 = Account("12345", "abcde")
This line creates an instance of the Account class named acc1 with account number "12345" and password "abcde".

Accessing Attributes:
print(acc1.acc_no): Prints the value of the public attribute acc1.acc_no, which is "12345".
print(acc1.__acc_pword): Tries to print the value of the private attribute acc1.__acc_pword. This will result in an AttributeError because __acc_pword is a private attribute and cannot be accessed directly from outside the class.

Detailed Breakdown

Class Definition:
The Account class is defined with an initializer method that sets both public (acc_no) and private (__acc_pword) attributes.

Instance Creation:
An instance acc1 of the Account class is created with the account number "12345" and the private password "abcde".

Accessing Attributes:
print(acc1.acc_no) prints the account number: "12345".
print(acc1.__acc_pword) tries to access the private attribute and results in an error.
"""