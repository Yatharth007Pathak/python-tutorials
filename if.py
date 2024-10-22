class A:
    varA = "welcome to class A"  # Class-level attribute

class B:
    varB = "welcome to class B"  # Class-level attribute

class C(A, B):
    varC = "welcome to class C"  # Class-level attribute

c1 = C()

print(c1.varC)  # Accesses varC from class C, prints: welcome to class C
print(c1.varB)  # Accesses varB from class B, prints: welcome to class B
print(c1.varA)  # Accesses varA from class A, prints: welcome to class A


# Multiple inheritance


'''
Let's break down the provided code, focusing on class inheritance and attribute access in Python.

Class Definitions and Multiple Inheritance
Base Class A:
class A:: Defines a base class named A.
varA = "welcome to class A": A class-level attribute varA with the value "welcome to class A".

Base Class B:
class B:: Defines a base class named B.
varB = "welcome to class B": A class-level attribute varB with the value "welcome to class B".

Derived Class C:
class C(A, B):: Defines a derived class C that inherits from both base classes A and B. This is an example of multiple inheritance.
varC = "welcome to class C": A class-level attribute varC with the value "welcome to class C".

Creating an Instance:
c1 = C(): Creates an instance of the C class named c1.

Accessing Attributes:
print(c1.varC): Prints the value of varC from the C class, which is "welcome to class C".
print(c1.varB): Prints the value of varB from the B class, inherited by the C class, which is "welcome to class B".
print(c1.varA): Prints the value of varA from the A class, inherited by the C class, which is "welcome to class A".

Detailed Breakdown
Let's walk through the code step by step:

Class Definitions:
A: A base class with a class-level attribute varA.
B: Another base class with a class-level attribute varB.
C: A derived class that inherits from both A and B, and has its own class-level attribute varC.

Instance Creation:
c1: An instance of the C class. This instance has access to attributes from its own class (C) 
as well as the inherited attributes from classes A and B.

Attribute Access:
c1.varC: Accesses varC from the C class, prints "welcome to class C".
c1.varB: Accesses varB from the B class through inheritance, prints "welcome to class B".
c1.varA: Accesses varA from the A class through inheritance, prints "welcome to class A".

Summary
Multiple Inheritance: Class C inherits from both A and B. This means that instances of C have access to the attributes of both A and B.
Attribute Access: The instance c1 of class C can access its own attribute (varC) 
as well as the inherited attributes from A (varA) and B (varB).
'''