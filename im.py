class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy  # Initialize Physics marks
        self.chem = chem  # Initialize Chemistry marks
        self.math = math  # Initialize Mathematics marks
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"  # Calculate and store percentage

stu1 = Student(98, 97, 99)  # Create an instance of Student with specific marks
print(stu1.percentage)  # Print the percentage of the student


# We use @property decorator on any method in the class to use themethod as a property.


'''
Let's break down the provided code that defines a Student class, initializes it with marks in three subjects, and calculates the percentage.

Class Definition and Initialization:
class Student:: Defines a class named Student.
def __init__(self, phy, chem, math):: Defines the initializer (constructor) method which initializes 
the instance attributes phy, chem, math, and percentage.

Instance Attributes:
self.phy = phy: Initializes the instance attribute phy with the value passed during the creation of the Student object.
self.chem = chem: Initializes the instance attribute chem similarly.
self.math = math: Initializes the instance attribute math similarly.

Percentage Calculation:
self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
self.percentage: Initializes the instance attribute percentage.
(self.phy + self.chem + self.math) / 3: Calculates the average of the three marks.
str(...) + "%": Converts the average to a string and appends a "%" sign to denote it as a percentage.
Creating an Instance and Printing Percentage

Creating an Instance:
stu1 = Student(98, 97, 99): Creates an instance of the Student class named stu1, with marks 98 in Physics, 
97 in Chemistry, and 99 in Mathematics.

Printing the Percentage:
print(stu1.percentage): Prints the percentage attribute of the stu1 instance, which is the calculated average in percentage form.

Detailed Breakdown

Class Definition:
Student: A class to represent a student with marks in Physics, Chemistry, and Mathematics, and to calculate the average percentage.

Initializer Method:
__init__(self, phy, chem, math): The constructor method to initialize the instance with marks and calculate the percentage.

Instance Attributes Initialization:
phy, chem, math: Attributes to store the marks in Physics, Chemistry, and Mathematics, respectively.
percentage: Attribute to store the calculated percentage.

Percentage Calculation:
The average of the three marks is calculated and stored as a string with a "%" sign appended.

Creating an Instance:
An instance stu1 is created with specific marks.

Printing the Percentage:
The percentage of stu1 is printed.

Summary
Class Student: Defines a student with marks in three subjects and calculates the percentage.
Initializer Method: Initializes marks and calculates the percentage.
Instance Attributes: Stores marks and the calculated percentage.
Instance Creation: Creates an instance with specific marks.
Output: Prints the calculated percentage.
'''