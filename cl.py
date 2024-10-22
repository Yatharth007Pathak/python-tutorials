numbers = [1, 2, 3, 4, 5]

# Find the index of an element at first occurrence
index_of_3 = numbers.index(3)
print(index_of_3)  # Output: 2

# Count total occurrences of an element
count_of_3 = numbers.count(3)
print(count_of_3)  # Output: 1

# Sort the list in descending order
numbers.sort(reverse = True)
print(numbers)  # Output: [5, 4, 3, 2, 1]

# Sort the list in ascending order
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Reverse the list
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

# Copy the list
numbers_copy = numbers.copy()
print(numbers_copy)  # Output: [5, 4, 3, 2, 1]

# Removes first occurence of element
numbers.remove(1)
print(numbers)   # Output: [5, 4, 3, 2]

# Removes element at index
numbers.pop(1)
print(numbers)   # Output: [5, 3, 2]

# Clear all elements from the list
numbers.clear()
print(numbers)  # Output: []



# Python provides several methods to work with lists.