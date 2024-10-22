class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy  # Initialize Physics marks
        self.chem = chem  # Initialize Chemistry marks
        self.math = math  # Initialize Mathematics marks
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"  # Calculate and store initial percentage

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"  # Recalculate and store percentage

stu1 = Student(98, 97, 99)  # Create an instance of Student with specific marks
print(stu1.percentage)  # Print the initial percentage of the student

stu1.phy = 86  # Modify the Physics marks of the student
print(stu1.phy)  # Print the modified Physics marks

stu1.calcPercentage()  # Recalculate the percentage based on updated marks
print(stu1.percentage)  # Print the updated percentage of the student


'''
Let's break down the updated code, which includes a method to recalculate the percentage after modifying one of the instance attributes.

Class Definition and Initialization;
class Student:: Defines a class named Student.
def __init__(self, phy, chem, math):: Defines the initializer (constructor) method 
which initializes the instance attributes phy, chem, math, and percentage.

Instance Attributes Initialization:
self.phy = phy: Initializes the instance attribute phy with the value passed during the creation of the Student object.
self.chem = chem: Initializes the instance attribute chem similarly.
self.math = math: Initializes the instance attribute math similarly.
self.percentage: Calculates the initial percentage and stores it as a string with a "%" sign appended.

Recalculate Percentage Method:
def calcPercentage(self):: Defines an instance method to recalculate the percentage based on the current values of phy, chem, and math.
self.percentage: Recalculates and updates the percentage attribute.

Creating an Instance:
stu1 = Student(98, 97, 99): Creates an instance of the Student class named stu1, with marks 98 in Physics, 
97 in Chemistry, and 99 in Mathematics.

Printing Initial Percentage:
print(stu1.percentage): Prints the initial percentage attribute of the stu1 instance, which is the calculated average in percentage form.

Modifying Physics Marks:
stu1.phy = 86: Modifies the phy attribute of the stu1 instance to 86.

Printing Modified Physics Marks:
print(stu1.phy): Prints the modified phy attribute of the stu1 instance, which is now 86.
Recalculating and Printing Updated Percentage:

stu1.calcPercentage(): Calls the calcPercentage method to recalculate the percentage based on the updated marks.
print(stu1.percentage): Prints the updated percentage attribute of the stu1 instance, reflecting the new average.

Detailed Breakdown

Class Definition:
Student: A class to represent a student with marks in Physics, Chemistry, and Mathematics, and to calculate the average percentage.

Initializer Method:
__init__(self, phy, chem, math): The constructor method to initialize the instance with marks and calculate the initial percentage.

Instance Attributes Initialization:
phy, chem, math: Attributes to store the marks in Physics, Chemistry, and Mathematics, respectively.
percentage: Attribute to store the calculated initial percentage.

Recalculate Percentage Method:
calcPercentage(self): An instance method to recalculate the percentage based on the current marks.

Instance Creation:
stu1: An instance of the Student class with initial marks.

Initial Percentage:
print(stu1.percentage): Prints the initial percentage, which is based on the initial marks.

Modifying Marks:
stu1.phy = 86: Modifies the Physics marks of stu1.

Printing Modified Marks:
print(stu1.phy): Prints the modified Physics marks.

Recalculating Percentage:
stu1.calcPercentage(): Recalculates the percentage based on the updated marks.

Printing Updated Percentage:
print(stu1.percentage): Prints the updated percentage reflecting the new marks.

Summary
Class Student: Defines a student with marks in three subjects and calculates the percentage.
Initializer Method: Initializes marks and calculates the initial percentage.
Recalculate Percentage Method: Provides functionality to recalculate the percentage after modifying the marks.
Instance Creation and Attribute Modification: Demonstrates creating an instance, modifying attributes, and recalculating the percentage.
'''