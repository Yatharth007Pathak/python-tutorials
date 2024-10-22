class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())

    # credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    # print the balance method
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12345)

print(acc1.balance)
print(acc1.account_no)

acc1.debit(2000)
acc1.credit(500)



'''
Create a bank account with 2 attributes- balance and account no.
Create methods for debit, credit and printing the balance 
'''

"""
 Let's break down the given Python code step by step, focusing on the class definition, instance attributes, and methods.

Class Definition and Initializer Method:
class Account:: Defines a new class named Account.
def __init__(self, bal, acc):: Defines the initializer method, also known as the constructor, which is called when a new instance of Account is created.
self.balance = bal: Initializes the instance attribute balance with the value provided during instantiation.
self.account_no = acc: Initializes the instance attribute account_no with the value provided during instantiation.

Instance Method debit:
def debit(self, amount):: Defines an instance method debit.
self.balance -= amount: Decreases the balance by the specified amount.
print("Rs.", amount, "was debited"): Prints a message indicating the amount debited.
print("total balance =", self.get_balance()): Prints the current balance by calling the get_balance method.

Instance Method credit:
def credit(self, amount):: Defines an instance method credit.
self.balance += amount: Increases the balance by the specified amount.
print("Rs.", amount, "was credited"): Prints a message indicating the amount credited.
print("total balance =", self.get_balance()): Prints the current balance by calling the get_balance method.

Instance Method get_balance:
def get_balance(self):: Defines an instance method get_balance.
return self.balance: Returns the current balance.

Creating an Instance and Accessing Attributes:
acc1 = Account(10000, 12345): Creates an instance of the Account class named acc1 with a balance of 10000 and account number 12345.
print(acc1.balance): Prints the balance of acc1, which is 10000.
print(acc1.account_no): Prints the account number of acc1, which is 12345.

Calling the debit and credit Methods:
acc1.debit(2000): Calls the debit method on acc1 with an amount of 2000.
Decreases the balance by 2000.
Prints "Rs. 2000 was debited".
Prints the new balance, which is 8000.
acc1.credit(500): Calls the credit method on acc1 with an amount of 500.
Increases the balance by 500.
Prints "Rs. 500 was credited".
Prints the new balance, which is 8500.

Summary
Class Definition: The Account class is defined with an initializer method, three instance methods 
(debit, credit, and get_balance), and two instance attributes (balance and account_no).
Instance Methods:
debit decreases the balance and prints the updated balance.
credit increases the balance and prints the updated balance.
get_balance returns the current balance.
Instance Creation and Attribute Access: An instance acc1 is created and its attributes are accessed and printed.
Method Calls: The debit and credit methods are called to modify the balance and print the updated balance.
"""