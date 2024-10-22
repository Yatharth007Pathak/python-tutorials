class Student:
    college_name = "ABC College"
    name = "yatharth"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("pathak", 98)
s1.welcome()
print(s1.get_marks())



'''
Methods are functions that belong to objects

creating class ->
class Student:
    def __int__(self, name):
        self.name = name

    def hello(self):
        print("hello", self.name)


creating object ->
s1 = Student("yatharth")
'''


"""
 break down of Python code step by step.

Class Definition and Class Attributes:
class Student:: Defines a new class named Student.
college_name = "ABC College": A class attribute shared by all instances of the Student class.
name = "yatharth": Another class attribute shared by all instances. 
This will be overshadowed by the instance attribute name when an instance is created.

Initializer Method:
__init__ is the initializer method that gets called when a new instance of Student is created.
self.name = name: Initializes the instance attribute name with the value provided during the instantiation.
self.marks = marks: Initializes the instance attribute marks with the value provided during the instantiation.

Instance Method welcome:
def welcome(self): defines an instance method named welcome.
print("welcome student", self.name): Prints a welcome message including the instance's name.

Instance Method get_marks:
def get_marks(self): defines an instance method named get_marks.
return self.marks: Returns the marks attribute of the instance.

Creating an Instance:
s1 = Student("pathak", 98)
This line creates an instance of the Student class with the name "pathak" and marks 98.
name attribute is set to "pathak" and marks attribute is set to 98 for this instance.

Calling the welcome Method:
s1.welcome()
This line calls the welcome method on the s1 instance.
It prints: "welcome student pathak".

Calling the get_marks Method:
print(s1.get_marks())
This line calls the get_marks method on the s1 instance.
It prints the returned value from get_marks(), which is 98.

Summary
Class Attributes: college_name and name are shared across all instances of the Student class. 
These are not specific to any particular instance.
Instance Attributes: name and marks are specific to each instance. When an instance is created, 
these attributes are set through the __init__ method.
Instance Methods: welcome and get_marks are methods that operate on individual instances of the Student class. 
They use the instance-specific attributes (self.name and self.marks).
"""