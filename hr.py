class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("pathak", [98, 99, 97])
s1.get_avg()

s1.name = "yatharth"
s1.get_avg()
s1.hello()



'''
Static methods:- Methods that don't use the self parameter (work at class level)

class Student:
    @staticmethod    #decorator
    def college():
    print("ABC College")

Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, thout permanently modifying it
'''


"""
break down of Python code step by step:-

Class Definition and Initializer Method:
class Student:: Defines a new class named Student.
def __init__(self, name, marks):: Defines the initializer method, also known as the constructor, which is called when a new instance of Student is created.
self.name = name: Initializes the instance attribute name with the value provided during instantiation.
self.marks = marks: Initializes the instance attribute marks with the value provided during instantiation.

Static Method:
@staticmethod: This decorator indicates that hello is a static method, which means it does not operate on an instance of the class.
def hello():: Defines the static method hello.
print("hello"): This line prints the string "hello" when the hello method is called.

Instance Method to Calculate Average Marks:
def get_avg(self):: Defines an instance method get_avg.
sum = 0: Initializes a variable sum to 0.
for val in self.marks:: Iterates over the elements in the marks list.
sum += val: Adds each mark to sum.
print("hi", self.name, "your avg score is:", sum / 3): Prints the average score, which is the sum of the marks divided by 3.

Creating an Instance:
s1 = Student("pathak", [98, 99, 97])
This line creates an instance of the Student class named s1 with the name "pathak" and marks [98, 99, 97].
The __init__ method is called, setting s1.name to "pathak" and s1.marks to [98, 99, 97].

Calling get_avg Method:
s1.get_avg()
This line calls the get_avg method on the s1 instance.
It calculates the average of the marks and prints: hi pathak your avg score is: 98.0.

Modifying the name Attribute:
s1.name = "yatharth"
This line changes the name attribute of the s1 instance from "pathak" to "yatharth".

Calling get_avg Method Again:
s1.get_avg()
This line calls the get_avg method on the s1 instance again.
It calculates the average of the marks and prints: hi yatharth your avg score is: 98.0.

Calling the Static Method hello:
s1.hello()
This line calls the static method hello on the s1 instance.
It prints: hello.

Summary
Class Definition: The Student class is defined with an initializer method, a static method, and an instance method.
Instance Attributes: name and marks are initialized in the __init__ method.
Static Method: hello is a static method that prints "hello".
Instance Method: get_avg calculates and prints the average of the marks.
Instance Creation: An instance s1 is created with initial values for name and `
"""