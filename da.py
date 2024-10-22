student = {"name": "John", "age": 21, "courses": ["Math", "Science"]}

# Add a new key-value pair
student["address"] = "123 Main St"
print(student)  # Output: {'name': 'John', 'age': 21, 'courses': ['Math', 'Science'], 'address': '123 Main St'}

# Update an existing key-value pair
student["age"] = 22
print(student)  # Output: {'name': 'John', 'age': 22, 'courses': ['Math', 'Science'], 'address': '123 Main St'}

# Remove a key-value pair
del student["address"]
print(student)  # Output: {'name': 'John', 'age': 22, 'courses': ['Math', 'Science']}

# Remove and return a value
age = student.pop("age")
print(age)  # Output: 22
print(student)  # Output: {'name': 'John', 'courses': ['Math', 'Science']}



# Modifying Dictionaries:- We can add, update, or remove key-value pairs in a dictionary.