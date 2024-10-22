values = {9, 9.25, 9.0}
print(values)

'''
break down of above code:

Creating a Set:
values = {9, 9.25, 9.0}
Here, a set named values is being created.
In Python, sets are collections of unique elements.
The elements within the braces {} are the items to be included in the set.
The elements 9, 9.25, and 9.0 are all numeric values.

Understanding the Set:
Sets automatically remove duplicate elements.
In the set {9, 9.25, 9.0}, the element 9 and 9.0 are considered the same because 9.0 is just another representation of the integer 9.
Therefore, only one instance of 9 will be included in the set.

Printing the Set:
print(values)
The print function is used to display the contents of the set values.
When the set is printed, it will show the unique elements it contains.

Final Output:
When we run this code, we will see the following output:
{9, 9.25}
This output reflects that the set values only contains unique elements, 
hence 9 and 9.0 are considered the same, and only one instance is shown. The elements are displayed without duplicates.
'''

values_ = (9, "9.0")
print(values_)

'''
break down of above code:

Creating a Tuple:
values_ = (9, "9.0")
Here, a tuple named values_ is being created.
In Python, tuples are ordered collections of elements that are enclosed in parentheses ().
Tuples can contain elements of different data types.
The elements within the parentheses are 9 (an integer) and "9.0" (a string).

Printing the Tuple:
print(values_)
The print function is used to display the contents of the tuple values_.
When the tuple is printed, it will show all the elements it contains in the order they were defined.

Final Output:
When you run this code, you will see the following output:
(9, '9.0')
This output reflects the elements of the tuple values_:
The integer 9.
The string "9.0".
Tuples preserve the order of elements and can contain multiple data types, so both elements are printed as they are.
'''


values__ = {
    ("float", 9.0),
    ("int", 9)
}
print(values__)

'''
break down of above code:

Creating a Set of Tuples:
values__ = {
    ("float", 9.0),
    ("int", 9)
}
Here, a set named values__ is being created.
In Python, sets are collections of unique elements.
The elements of this set are tuples.
The first tuple is ("float", 9.0), which pairs the string "float" with the float 9.0.
The second tuple is ("int", 9), which pairs the string "int" with the integer 9.

Printing the Set:
print(values__)
The print function is used to display the contents of the set values__.
When the set is printed, it will show all the unique elements it contains.

Final Output:
When we run this code, we will see an output similar to the following:
{('float', 9.0), ('int', 9)}
This output reflects the elements of the set values__:
The tuple ('float', 9.0).
The tuple ('int', 9).


Sets in Python:
Sets automatically remove duplicate elements.
Sets are unordered, meaning the elements can appear in any order when printed.

Tuples in Sets:
The tuples in the set maintain their structure and order within the set.
The elements of the tuples can be of different data types.
Since both tuples ('float', 9.0) and ('int', 9) are unique and distinct, they are both included in the set and printed as part of the set.
'''

# Figure out a way to store 9 and 9.0 as separate values in the set