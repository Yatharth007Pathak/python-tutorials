numbers = {1, 2, 3, 4, 5}

# Adding a single element
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Adding multiple elements
numbers.update([7, 8, 9])
print(numbers)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing an element (raises an error if the element is not found)
numbers.remove(9)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Removing an element (does not raise an error if the element is not found)
numbers.discard(10)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Removing and returning an arbitrary element
popped_element = numbers.pop()
print(popped_element)
print(numbers)

# Clearing all elements
numbers.clear()
print(numbers)  # Output: set()


# Modifying Sets:- We can add or remove elements from a set using various methods.