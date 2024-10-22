class Account:
    def __init__(self, acc_no, acc_pword):
        self.acc_no = acc_no
        self.__acc_pword = acc_pword

    def reset_pword(self):
        print(self.__acc_pword)

acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pword())


'''
Let's break down the updated code, focusing on how the class handles private attributes and the method used to access them.

Class Definition and Initializer Method:
class Account:: Defines a new class named Account.
def __init__(self, acc_no, acc_pword):: Defines the initializer method (constructor) which is called when a new instance of Account is created.
self.acc_no = acc_no: Initializes the instance attribute acc_no with the value provided during instantiation.
self.__acc_pword = acc_pword: Initializes the private instance attribute __acc_pword with the value provided during instantiation.
The double underscore __ prefix makes __acc_pword a private attribute, meaning it cannot be accessed directly from outside the class.

Instance Method reset_pword:
def reset_pword(self):: Defines an instance method reset_pword.
print(self.__acc_pword): This line prints the value of the private attribute __acc_pword. 
This allows controlled access to the private attribute within the class.

Creating an Instance and Accessing Attributes:
acc1 = Account("12345", "abcde"): Creates an instance of the Account class named acc1 with account number "12345" and password "abcde".
print(acc1.acc_no): Prints the value of the public attribute acc1.acc_no, which is "12345".
print(acc1.reset_pword()): Calls the reset_pword method on acc1, which prints the value of the private attribute __acc_pword and returns None.

Detailed Breakdown

Class Definition:
The Account class is defined with an initializer method that sets both public (acc_no) and private (__acc_pword) attributes.
An instance method reset_pword is defined to print the private attribute __acc_pword.

Instance Creation:
An instance acc1 of the Account class is created with the account number "12345" and the private password "abcde".

Accessing Attributes:
print(acc1.acc_no) prints the account number: "12345".
print(acc1.reset_pword()):
Calls the reset_pword method, which prints the private password: "abcde".
Since reset_pword does not return a value (it implicitly returns None), print(acc1.reset_pword()) prints: None.
'''