class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

emp1 = Employee("accountant", "finance", "60,000")
emp1.showDetails()

eng1 = Engineer("yatharth", 20)
eng1.showDetails()



'''
Define an Employee class with attributes role, department and salary. This class also has a showDetails() method
Create an Engineer class that inherits properties from Employee and has additional attributes: name and age
'''


"""
This code defines two classes: Employee and Engineer, showcasing inheritance and the use of super() for accessing the parent class's methods. 
Let's break it down:

Defining the Employee class:
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)
The Employee class has attributes role, dept, and salary.
It also has a method showDetails() to display these attributes.

Defining the Engineer class (subclass of Employee):
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")
The Engineer class inherits from the Employee class.
It adds attributes name and age.
In the constructor, it initializes the role, dept, and salary attributes using super() to call the parent class's constructor.

Creating instances of Employee and Engineer classes:
emp1 = Employee("accountant", "finance", "60,000")
emp1.showDetails()

eng1 = Engineer("yatharth", 20)
eng1.showDetails()

emp1 is an instance of the Employee class, initialized with role, department, and salary.
eng1 is an instance of the Engineer class, initialized with name and age.
Both instances call the showDetails() method to display their attributes.

Summary:
The Employee class serves as a base class with attributes and a method to display details.
The Engineer class inherits from Employee and adds attributes specific to engineers.
The Engineer class uses super() to initialize attributes inherited from Employee.
Instances of both classes demonstrate the use of inheritance and attribute initialization through constructors.
"""