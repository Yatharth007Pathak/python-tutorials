phone_book = {1: "Alice", 2: "Bob", 3: "Charlie"}

# Get all keys
keys = phone_book.keys()
print(keys)  # Output: dict_keys([1, 2, 3])

# Get all values
values = phone_book.values()
print(values)  # Output: dict_values(['Alice', 'Bob', 'Charlie'])

# Get all key-value pairs as tuples
items = phone_book.items()
print(items)  # Output: dict_items([(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')])

# Get value according to key
print(phone_book.get(1))

# Update the dictionary with another dictionary
phone_book.update({4: "David", 5: "Eve"})
print(phone_book)  # Output: {1: 'Alice', 2: 'Bob', 3: 'Charlie', 4: 'David', 5: 'Eve'}

# Clear all items in the dictionary
phone_book.clear()
print(phone_book)  # Output: {}



# Dictionary Methods:- Dictionaries provide several useful methods