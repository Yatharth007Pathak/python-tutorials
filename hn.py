class Student:
    college_name = "ABC College"
    name = "yatharth"                           # class attr

    def __init__(self, name, marks):
        self.name = name                        # object attr
        self.marks = marks
        print("adding new student in database..")

s1 = Student("pathak", 98)
print(s1.name)

print(s1.college_name)



'''
class and instance attributes ( Class.attr, obj.attr)
Precedence of object attribute is greater than class attribute
'''



"""
break down the code step by step, highlighting the roles of class attributes and instance (object) attributes.

Class Definition and Class Attributes:
class Student:: Defines a new class named Student.
college_name = "ABC College": A class attribute shared by all instances of the Student class. 
This attribute is associated with the class itself, not with any particular instance.
name = "yatharth": Another class attribute shared by all instances. 
It will be overshadowed by the instance attribute name when an instance is created.

Initializer Method:
def __init__(self, name, marks):: Defines the initializer method that is called when a new instance of Student is created.
self.name = name: Initializes the instance attribute name with the value provided during the instantiation. This attribute is specific to each instance.
self.marks = marks: Initializes the instance attribute marks with the value provided during the instantiation.
print("adding new student in database.."): Prints a message indicating a new student is being added to the database.

Creating an Instance:
s1 = Student("pathak", 98)
This line creates an instance of the Student class with the name "pathak" and marks 98.
The __init__ method is called, setting the instance's name attribute to "pathak" and marks attribute to 98. 
It also prints the message "adding new student in database..".

Accessing Instance Attribute:
print(s1.name)
This line prints the name attribute of the s1 instance.
It outputs: pathak.

Accessing Class Attribute:
print(s1.college_name)
This line prints the college_name class attribute.
It outputs: ABC College.

Summary
Class Attributes: college_name and name are class attributes. They are shared across all instances of the Student class. 
The class attribute name is overshadowed by the instance attribute name once the instance is created.
Instance Attributes: name and marks are instance-specific attributes. These are set through the __init__ method when an instance is created.
Instance Creation: When s1 is created as an instance of Student, 
it sets the name to "pathak" and marks to 98, and prints a message about adding a new student.

In this code:

The class Student is defined with class attributes college_name and name.
The __init__ method initializes instance-specific attributes name and marks, and prints a message.
An instance s1 is created, demonstrating the initialization and accessing of both instance and class attributes.
"""