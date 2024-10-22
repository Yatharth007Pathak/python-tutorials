class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius


c1 = Circle(21)
print(c1.area())
print(c1.perimeter())



'''
Define a Circle class to create a circle with radius r using the constructor
Define an area() method of the class which calculates the area of the circle
Define a perimeter() method of the class which calculates the perimeter of the circle
'''


"""
This code defines a Circle class that calculates the area and perimeter of a circle based on its radius. 
Let's break it down step by step:

Defining the Circle class:
class Circle:
    def __init__(self, radius):
        self.radius = radius
This class has a constructor __init__ which initializes the radius attribute of the circle object.

Defining the area method:
def area(self):
    return (22/7) * self.radius ** 2
This method calculates the area of the circle using the formula π * r^2, where r is the radius of the circle.

Defining the perimeter method:
def perimeter(self):
    return 2 * (22/7) * self.radius
This method calculates the perimeter (or circumference) of the circle using the formula 2 * π * r.

Creating an instance of the Circle class:
c1 = Circle(21)
This line creates a Circle object with a radius of 21 units.

Printing the area and perimeter of the circle:
print(c1.area())
print(c1.perimeter())
These lines call the area and perimeter methods of the c1 object respectively, and print their return values.

Summary:
The Circle class encapsulates the properties and behaviors related to circles.
It provides methods to calculate the area and perimeter of a circle based on its radius.
The __init__ method initializes the radius attribute when a Circle object is created.
The area method calculates the area using the radius attribute.
The perimeter method calculates the perimeter using the radius attribute.
The output of this code will print the area and perimeter of a circle with a radius of 21 units, calculated using the provided formulas.
"""