marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

print(marks)



'''
Program to enter marks of # subjects from the user and store them in a dictionary. 
Start with an empty dictionary and add one by one. USe subject name as key and marks as value
'''