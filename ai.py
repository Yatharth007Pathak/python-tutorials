# Numeric Types
integer = 10
floating_point = 3.14
complex_number = 1 + 2j

print("Integer:", integer)
print("Floating Point:", floating_point)
print("Complex Number:", complex_number)

# Sequence Types
string = "Hello, World!"
list_example = [1, 2, 3, "apple"]
tuple_example = (1, 2, 3, "apple")
range_example = range(5)

print("String:", string)
print("List:", list_example)
print("Tuple:", tuple_example)
print("Range:", list(range_example))  # converting range to list for printing

# Mapping Type
dictionary = {"name": "Alice", "age": 30}

print("Dictionary:", dictionary)

# Set Types
set_example = {1, 2, 3, "apple"}
frozen_set_example = frozenset([1, 2, 3, "apple"])

print("Set:", set_example)
print("Frozen Set:", frozen_set_example)

# Boolean Type
boolean_true = True
boolean_false = False

print("Boolean True:", boolean_true)
print("Boolean False:", boolean_false)

# Binary Types
bytes_example = b'hello'
bytearray_example = bytearray(b'hello')
memoryview_example = memoryview(b'hello')

print("Bytes:", bytes_example)
print("Byte Array:", bytearray_example)
print("Memory View:", memoryview_example)

# None Type
none_type = None

print("None Type:", none_type)



'''
Python has a variety of built-in data types, each designed to handle specific kinds of data. 
Here's an overview of the main data types in Python:

Numeric Types
Integer (int): Represents whole numbers, e.g., 3, -42, 2024.
Floating Point (float): Represents real numbers with a decimal point, e.g., 3.14, -2.718, 0.0.
Complex (complex): Represents complex numbers with a real and imaginary part, e.g., 3+4j, -1-1j.

Sequence Types
String (str): Represents a sequence of characters, e.g., "hello", 'Python'.
List (list): An ordered, mutable collection of items, e.g., [1, 2, 3], ["apple", "banana", "cherry"].
Tuple (tuple): An ordered, immutable collection of items, e.g., (1, 2, 3), ("apple", "banana", "cherry").
Range (range): Represents an immutable sequence of numbers, commonly used in loops, e.g., range(5), range(1, 10, 2).

Mapping Type
Dictionary (dict): A collection of key-value pairs, e.g., {"name": "Alice", "age": 30}, {"apple": 1, "banana": 2}.

Set Types
Set (set): An unordered collection of unique items, e.g., {1, 2, 3}, {"apple", "banana", "cherry"}.
Frozen Set (frozenset): An immutable version of a set, e.g., frozenset([1, 2, 3]), frozenset(["apple", "banana", "cherry"]).

Boolean Type
Boolean (bool): Represents True or False.

Binary Types
Bytes (bytes): An immutable sequence of bytes, e.g., b'hello'.
Byte Array (bytearray): A mutable sequence of bytes, e.g., bytearray(b'hello'), bytearray([0, 1, 2]).
Memory View (memoryview): A memory view object exposes the buffer-protocol, e.g., memoryview(b'hello').

None Type
NoneType: Represents the absence of a value, e.g., None.
'''