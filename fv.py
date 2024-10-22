def greet(*names):
    for name in names:
        print(f"Hello {name}!")

greet("Alice", "Bob", "Charlie")
# Output:
# Hello Alice!
# Hello Bob!
# Hello Charlie!

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York



# *args and **kwargs:- Functions can accept a variable number of arguments using *args and **kwargs: