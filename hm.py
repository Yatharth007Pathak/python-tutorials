class Student:
    def __init__(self, name, marks):                                 # parameterized constructors
        self.name = name
        self.marks = marks
        print("adding new student in database..")

s1 = Student("yatharth", 97)
print(s1.name, s1.marks)

s2 = Student("pathak", 98)
print(s2.name, s2.marks)


'''
break down the Python code step by step, focusing on the use of parameterized constructors and instance attributes.

Class Definition:
class Student:
This line defines a new class named Student.

Parameterized Constructor:
def __init__(self, name, marks):: Defines the initializer method, also known as the constructor, which is called when a new instance of Student is created.
self.name = name: Initializes the instance attribute name with the value provided during the instantiation.
self.marks = marks: Initializes the instance attribute marks with the value provided during the instantiation.
print("adding new student in database.."): Prints a message indicating a new student is being added to the database.

Creating the First Instance (s1):
s1 = Student("yatharth", 97)
This line creates an instance of the Student class with the name "yatharth" and marks 97.
The __init__ method is called, setting the instance's name attribute to "yatharth" and marks attribute to 97. 
It also prints the message "adding new student in database..".

Printing Attributes of the First Instance:
print(s1.name, s1.marks)
This line prints the name and marks attributes of the s1 instance.
It outputs: yatharth 97.

Creating the Second Instance (s2):
s2 = Student("pathak", 98)
This line creates another instance of the Student class with the name "pathak" and marks 98.
The __init__ method is called, setting the instance's name attribute to "pathak" and marks attribute to 98. 
It also prints the message "adding new student in database..".

Printing Attributes of the Second Instance:
print(s2.name, s2.marks)
This line prints the name and marks attributes of the s2 instance.
It outputs: pathak 98.

Summary
Class Definition: The Student class is defined with an initializer method.
Parameterized Constructor: The __init__ method takes two parameters (name and marks) and initializes the instance attributes accordingly.
Instance Creation: Two instances of the Student class (s1 and s2) are created with different names and marks.
Instance Attributes: Each instance has its own name and marks attributes, which are printed to the console.

In this code:

The Student class is defined with a parameterized constructor.
The __init__ method initializes the name and marks attributes and prints a message when a new student is added.
Two instances (s1 and s2) are created, demonstrating the initialization and accessing of instance attributes.
'''