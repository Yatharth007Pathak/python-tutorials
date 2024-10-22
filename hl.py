class Student:
    name = "yatharth"
    def __init__(self):                                              # default constructors
        print(self)
        print("adding new student in database..")

s1 = Student()
print(s1)

'''
Constructor:- All classes have a function called __init__(), which is always executed when the object is being initiated

creating class ->
class Student:
    def __init__(self, name):
        self.name = name

creating object ->
s1 = Student("yatharth")
print(s1.name)

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class

The data or variables stored inside the class or objects are called attributes
'''


"""
break down the given Python code step by step, focusing on the use of class attributes and default constructors.

Class Definition and Class Attribute:
class Student:: Defines a new class named Student.
name = "yatharth": A class attribute shared by all instances of the Student class. 
This attribute is associated with the class itself, not with any particular instance.

Default Constructor:
def __init__(self):: Defines the initializer method, also known as the constructor, 
which is called when a new instance of Student is created. Since it takes no parameters other than self, it is a default constructor.
print(self): Prints the self reference, which is the instance of the class being created.
print("adding new student in database.."): Prints a message indicating a new student is being added to the database.

Creating an Instance:
s1 = Student()
This line creates an instance of the Student class named s1.
The __init__ method is called automatically, which prints the instance reference and the message "adding new student in database..".

Printing the Instance:
print(s1)
This line prints the instance reference s1.
It outputs the memory address of the instance s1, which is the same as the one printed within the __init__ method.

Summary
Class Attribute: name is a class attribute shared across all instances of the Student class. 
It is not used within this example, but it's defined at the class level.
Default Constructor: The __init__ method takes no additional parameters 
and prints the instance reference (self) and a message when a new instance is created.
Instance Creation: An instance s1 is created, invoking the __init__ method and printing details.
Printing the Instance: The instance reference is printed twice: once within the constructor and once after the instance is created.
"""