class Student:
    name = "yatharth"

s1 = Student()
print(s1.name)
print(s1)

s2 = Student()
print(s2.name)
print(s2)


'''
creating class ->
class Student:
    name = "yatharth"

creating object (instance) ->
s1 = Student()
print(s1.name)
'''


"""
Let's break down the given Python code step by step, focusing on the use of class attributes, creating instances, and understanding the output.

Class Definition and Class Attribute:
class Student:: Defines a new class named Student.
name = "yatharth": A class attribute shared by all instances of the Student class. 
This attribute is associated with the class itself, not with any particular instance.

Creating the First Instance (s1):
s1 = Student()
This line creates an instance of the Student class named s1.
Since no __init__ method is defined, Python uses a default constructor which does nothing special other than create the instance.

Printing the name Attribute and Instance Reference for s1:
print(s1.name): This line prints the name attribute of the s1 instance. Since name is a class attribute, 
it is accessed through the instance s1 and prints: yatharth.
print(s1): This line prints the reference to the s1 instance. 
It outputs the memory address of the s1 instance, e.g., <__main__.Student object at 0x7f9f9c7d8910>.

Creating the Second Instance (s2):
s2 = Student()
This line creates another instance of the Student class named s2.
Like s1, s2 is created using the default constructor.

Printing the name Attribute and Instance Reference for s2:
print(s2.name): This line prints the name attribute of the s2 instance. 
Since name is a class attribute, it is accessed through the instance s2 and prints: yatharth.
print(s2): This line prints the reference to the s2 instance. 
It outputs the memory address of the s2 instance, e.g., <__main__.Student object at 0x7f9f9c7d8b10>.

Summary
Class Attribute: name is a class attribute shared across all instances of the Student class. It is defined at the class level.
Instance Creation: Two instances, s1 and s2, are created using the default constructor.
Accessing Class Attribute: The class attribute name is accessed and printed through both instances s1 and s2.
Instance References: The memory addresses of the instances s1 and s2 are printed, showing that they are distinct objects.
"""