student = {"name": "John", "age": 21, "courses": ["Math", "Science"]}

# Access the value associated with a key
print(student["name"])  # Output: John
print(student["courses"])  # Output: ['Math', 'Science']
# print(student["name2"]) will give error


# Using the get method
print(student.get("age"))  # Output: 21
print(student.get("address", "Not Found"))  # Output: Not Found
# print(student.get("name2")) will not give error



# Accessing Dictionary Elements:- We can access elements in a dictionary using keys.