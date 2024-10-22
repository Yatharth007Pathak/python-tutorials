# Sample list
numbers = [5, 2, 9, 1, 5, 6]

# Sorting the list in ascending order with default parameters
numbers.sort()  # No key function, no reverse
print("Sorted in ascending order:", numbers)

# Sample list
words = ['banana', 'apple', 'cherry', 'date']

# Sorting the list in ascending order with a custom key function (length of the string)
words.sort(key=len)  # Sort by length of each word
print("Sorted by length:", words)

# Sample list
numbers_desc = [5, 2, 9, 1, 5, 6]

# Sorting the list in descending order
numbers_desc.sort(reverse=True)  # No key function, reverse order
print("Sorted in descending order:", numbers_desc)

# Sample list
words_desc = ['banana', 'apple', 'cherry', 'date']

# Sorting the list in descending order with a custom key function (length of the string)
words_desc.sort(key=len, reverse=True)  # Sort by length of each word, in reverse order
print("Sorted by length in descending order:", words_desc)

# Python code to implement sort method with all of its parameters


'''
The sort method in Python's list class can be used to sort lists in place. It accepts several parameters:

key: A function to be called on each list element before making comparisons.
reverse: A boolean value indicating whether the list should be sorted in descending order.
'''