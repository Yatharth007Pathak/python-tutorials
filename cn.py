# An empty tuple
empty_tuple = ()
print(empty_tuple)

# A tuple of integers
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(type(numbers))

# A tuple of strings
fruits = ("apple", "banana", "cherry")
print(fruits)

# A tuple containing mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print(mixed_tuple)

# A nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)

# A tuple without parentheses (tuple packing)
packed_tuple = 1, 2, 3
print(packed_tuple)



'''
Tuples in python

In Python, a tuple is a built-in data type that allows us to create immutable sequence of values.
Tuples in Python are similar to lists but with one key difference: 
they are immutable, meaning that once a tuple is created, its elements cannot be changed
We can create a tuple by placing items inside parentheses (), separated by commas.

Advantages of Using Tuples
Immutability: Useful for fixed data that should not change.
Performance: Tuples are generally faster than lists for indexing and iteration.
Hashable: Tuples can be used as keys in dictionaries, whereas lists cannot.
'''