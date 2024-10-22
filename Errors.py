# Find all python error

import re
for i in dir(__builtins__):
    if re.match(r'^[A-Z]',i):
        print(i)

'''
Here's a line-by-line breakdown of this code, which uses regular expressions to filter and 
print certain elements from Python's built-in functions and classes:

1. import re
This imports the re module, which provides functions for working with regular expressions (regex).
Regular expressions are used for pattern matching within strings.

2. for i in dir(__builtins__):
This starts a for loop that iterates over all items in dir(__builtins__).
dir(__builtins__) returns a list of all built-in objects in Python 
(functions, classes, and variables that are available without needing to import any module).

3. if re.match(r'^[A-Z]',i):
This line checks whether the name i (from the built-in objects) starts with an uppercase letter.
re.match() tries to match the pattern ^[A-Z], which means "a string that starts with an uppercase letter".
^ indicates the start of a string.
[A-Z] is a character class that matches any single uppercase letter from A to Z.

4. print(i)
If the condition in the if statement is true (i.e., the built-in name starts with an uppercase letter), it prints the name i.
Explanation of What the Code Does:
The code loops through all the names of Python's built-in objects and checks if the name starts with an uppercase letter.
If the name starts with an uppercase letter, it's printed. 
Since class names typically begin with an uppercase letter in Python, this will filter out classes and some other built-in objects.
'''