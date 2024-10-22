class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("yatharth")
print(s1)

del s1
print(s1)

# output:- NameError: name 's1' is not defined



'''
del keyword:- Used to delete object properties or object itself.

del s1.name               deletes attributes
del s1                    deletes complete object
'''