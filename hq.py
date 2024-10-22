class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)

s1 = Student("pathak", [98, 99, 97])
s1.get_avg()

s1.name = "yatharth"
s1.get_avg()



# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average


'''
break down the given Python code step by step.

Class Definition and Initialization
Class Definition:
class Student:
This line defines a new class named Student.

Initializer Method:
def __init__(self, name, marks):
    self.name = name
    self.marks = marks
This method is called when an instance of the Student class is created. It initializes the name and marks attributes for the instance.

Method Definition
Average Calculation Method:
def get_avg(self):
    sum = 0
    for val in self.marks:
        sum += val
    print("hi", self.name, "your avg score is:", sum/3)
This method calculates the average of the marks and prints a message with the student's name and average score.
sum = 0: Initializes a variable to hold the sum of the marks.
for val in self.marks:: Iterates through the marks.
sum += val: Adds each mark to the sum.
print(...): Prints the average score.
Creating an Instance and Using the Method

Creating an Instance:
s1 = Student("pathak", [98, 99, 97])
This line creates an instance of the Student class with the name "pathak" and marks [98, 99, 97].

Calling the Method:
s1.get_avg()
This line calls the get_avg method on the s1 instance, which prints the average score.

Modifying the Name Attribute:
s1.name = "yatharth"
This line changes the name attribute of the s1 instance from "pathak" to "yatharth".

Calling the Method Again:
s1.get_avg()
This line calls the get_avg method again, which now prints the average score with the updated name.
'''