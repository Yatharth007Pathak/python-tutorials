class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order("chips", 20)
odr2 = Order("tea", 10)

print(odr1 > odr2) # True



'''
Create a class called Order which stores item and its price
use dunder function __gt__() to convey that:
    order1 > order2 if price of order1 > price of order2
'''


"""
let's break down the provided code:

class Order:: This line defines a class named Order.

def __init__(self, item, price):: This is the constructor method for the Order class. 
It initializes instances of the class with two attributes: item and price.

self.item = item and self.price = price: These lines assign the values of item and price 
passed to the constructor to the respective attributes of the instance.

def __gt__(self, odr2):: This method is defining the behavior of the > operator (greater than) 
for instances of the Order class. It takes another Order instance (odr2) as input.

return self.price > odr2.price: This line compares the price attribute of the current instance 
(self) with the price attribute of the other instance (odr2). It returns True if the price of 
the current instance is greater than the price of the other instance; otherwise, it returns False.

odr1 = Order("chips", 20): This line creates an instance of the Order class named odr1 with the item "chips" and the price 20.

odr2 = Order("tea", 10): This line creates another instance of the Order class named odr2 with the item "tea" and the price 10.

print(odr1 > odr2): This line compares odr1 with odr2 using the > operator. 
It will call the __gt__ method of the odr1 instance, passing odr2 as an argument
"""