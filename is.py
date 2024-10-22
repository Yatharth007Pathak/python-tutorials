class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(5, 6)
num1.showNumber()

num2 = Complex(1, 3)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()



'''
Let's break down the code step by step. 
This version of the Complex class includes support for both addition and subtraction using operator overloading.

Class Definition
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
Class Name: Complex.
Constructor Method (__init__): Initializes an instance of the Complex class.
Parameters: self, real, img.
self refers to the instance of the class.
real and img are the real and imaginary parts of the complex number, respectively.
These parameters are assigned to the instance variables self.real and self.img.

Method to Display the Complex Number
    def showNumber(self):
        print(self.real, "i +", self.img, "j")
Method Name: showNumber.
Parameter: self.
This method prints the complex number in the form of real i + img j.

Method to Add Two Complex Numbers
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
Method Name: __add__.
Parameters: self, num2.
This method overloads the + operator to add two complex numbers.

Addition:
newReal is the sum of the real parts: self.real + num2.real.
newImg is the sum of the imaginary parts: self.img + num2.img.
Returns: A new Complex object with newReal and newImg.

Method to Subtract Two Complex Numbers
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
Method Name: __sub__.
Parameters: self, num2.
This method overloads the - operator to subtract one complex number from another.

Subtraction:
newReal is the difference of the real parts: self.real - num2.real.
newImg is the difference of the imaginary parts: self.img - num2.img.
Returns: A new Complex object with newReal and newImg.

Creating and Displaying Complex Numbers

num1 = Complex(5, 6)
num1.showNumber()
Creating num1:
num1 is an instance of the Complex class with real part 5 and imaginary part 6.
num1.showNumber() prints: 5 i + 6 j.

num2 = Complex(1, 3)
num2.showNumber()
Creating num2:
num2 is an instance of the Complex class with real part 1 and imaginary part 3.
num2.showNumber() prints: 1 i + 3 j.

Adding Two Complex Numbers and Displaying the Result
num3 = num1 + num2
num3.showNumber()
Adding num1 and num2:
The __add__ method is called: num1.__add__(num2).
num3 is a new Complex object, resulting from the addition of num1 and num2.
The real part of num3 is 5 + 1 = 6.
The imaginary part of num3 is 6 + 3 = 9.
num3.showNumber() prints: 6 i + 9 j.

Subtracting Two Complex Numbers and Displaying the Result
num3 = num1 - num2
num3.showNumber()
Subtracting num1 and num2:
The __sub__ method is called: num1.__sub__(num2).
num3 is a new Complex object, resulting from the subtraction of num2 from num1.
The real part of num3 is 5 - 1 = 4.
The imaginary part of num3 is 6 - 3 = 3.
num3.showNumber() prints: 4 i + 3 j.

Summary
The Complex class models a complex number with real and imaginary parts.
It has methods to display the number and to add or subtract two complex numbers using operator overloading.
The code creates two complex numbers, displays them, adds them, displays the result, subtracts them, and then displays the result.
'''