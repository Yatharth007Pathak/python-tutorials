# An empty set
empty_set = set()
print(empty_set)
# note:- empty_set = {} is syntax of empty dictionary

# A set of integers
numbers = {1, 2, 3, 4, 5}
print(numbers)
print(type(numbers))

# A set of strings
fruits = {"apple", "banana", "cherry"}
print(fruits)

# A set with mixed data types
mixed_set = {1, "hello", False, 3.14}
print(mixed_set)

# Creating a set from a list (to remove duplicates)
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(list_with_duplicates)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}



'''
Set in python

Sets in Python are an unordered collection of unique elements which are immutable.
Sets are mutable but the elements of set are immutable.
In a set, repeated elements are stored only once
They are useful for performing various mathematical operations like union, intersection, difference, and symmetric difference.
We can create a set by placing elements inside curly braces {}, separated by commas, or by using the set() function.

Advantages of Using Sets
Unordered: Elements are stored in an unordered way.
Unique Elements: Automatically removes duplicates.
Efficient: Provides efficient membership testing and set operations.

Sets are a powerful and flexible data structure, particularly useful for mathematical operations and ensuring unique elements in a collection
'''