class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86

print(stu1.phy)
print(stu1.percentage)


'''
This code introduces the @property decorator, which allows the percentage method to be accessed 
like an attribute rather than a method call. Let's break it down:

Class Definition and Initialization:
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
Defines a class named Student.
Initializes instance attributes phy, chem, and math with the given values.

percentage Method with @property:
@property
def percentage(self):
    return str((self.phy + self.chem + self.math) / 3) + "%"
Decorates the percentage method with @property, making it behave like an attribute rather than a method.
When stu1.percentage is accessed, this method is automatically called and the return value is provided.

Creating an Instance:
stu1 = Student(98, 97, 99)
Creates an instance of the Student class named stu1 with initial marks.

Accessing Percentage:
print(stu1.percentage)
Prints the percentage of stu1, which is automatically calculated based on the initial marks.

Modifying Physics Marks:
stu1.phy = 86
Modifies the phy attribute of the stu1 instance to 86.

Printing Modified Physics Marks:
print(stu1.phy)
Prints the modified phy attribute of the stu1 instance, which is now 86.

Accessing and Printing Updated Percentage:
print(stu1.percentage)
Prints the updated percentage of the stu1 instance. Since percentage is decorated with @property, 
accessing it automatically recalculates the percentage based on the modified marks.

Summary
@property: Decorator used to define a method that behaves like an attribute.
Usage: Enables accessing the percentage method as if it were an attribute, automatically recalculating it whenever it is accessed.
Benefits: Provides a cleaner and more intuitive way to access calculated attributes.
'''