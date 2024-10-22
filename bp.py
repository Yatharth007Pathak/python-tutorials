# Concatenation

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # Output: "Hello World"
print(result)

# Repetition

result = str1 * 3  # Output: "HelloHelloHello"
print(result)

# Indexing

first_char = str1[0]  # Output: 'H'
print(first_char)
last_char = str1[-1]  # Output: 'o'
print(last_char)

# Slicing

str3 = "Hello, World!"
substring = str3[0:5]  # Output: 'Hello'
print(substring)
substring = str3[7:]   # Output: 'World!'
print(substring)
substring = str3[:5]   # Output: 'Hello'
print(substring)
substring = str3[::2]  # Output: 'Hlo ol!'
print(substring)

# length of a string

length = len(str1)  # Output: 5
print(length)

# Converting the string to lowercase or uppercase.

lower_str = str1.lower()  # Output: 'hello'
print(lower_str)
upper_str = str1.upper()  # Output: 'HELLO'
print(upper_str)

# Removing leading and trailing whitespace.

str4 = "  Hello  "
stripped_str = str4.strip()  # Output: 'Hello'
print(stripped_str)

# Spliting the string into a list of substrings based on a delimiter.

word = str3.split(", ")  # Output: ['Hello', 'World!']
print(word)

# Joining a list of strings into a single string with a specified delimiter.

words = ['Hello', 'World']
result = " ".join(words)  # Output: 'Hello World'
print(result)

# Replacing occurrences of a substring with another substring.

new_str = str3.replace("World", "Python")  # Output: 'Hello, Python!'
print(new_str)

# Finding the first or last occurrence of a substring.

index = str3.find("World")  # Output: 7
print(index)
index = str3.rfind("o")     # Output: 8
print(index)

# Formatting of strings with placeholders.

name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)
# Output: "My name is Alice and I am 30 years old."

# Providing a more concise way to format strings.

formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)
# Output: "My name is Alice and I am 30 years old."

# Special characters can be included in strings using escape sequences.

new_line = "Hello\nWorld"               # New line
print(new_line)
tab = "Hello\tWorld"                    # Tab
print(tab)
quote = "She said, \"Hello!\""          # Double quote
print(quote)

# Multiline strings can be created using triple quotes.

multiline_str = """This is a
multiline string."""
print(multiline_str)

# Strings in Python are immutable, meaning that once a string is created, it cannot be changed. 
# Any operations that modify a string will return a new string.

str5 = str1.replace("H", "J")  # str1 is not changed
print(str1)  # Output: "Hello"
print(str5)  # Output: "Jello"


"""
String Operations

Concatenation
Strings can be concatenated using the + operator.

Repetition
Strings can be repeated using the * operator.

Indexing
We can access individual characters in a string using indexing. Python uses zero-based indexing.

Slicing
We can extract substrings using slicing.

Common String Methods

len()
Returns the length of the string.

lower() and upper()
Converts the string to lowercase or uppercase.

strip()
Removes leading and trailing whitespace.

split()
Splits the string into a list of substrings based on a delimiter.

join()
Joins a list of strings into a single string with a specified delimiter.

replace()
Replaces occurrences of a substring with another substring.

find() and rfind()
Finds the first or last occurrence of a substring.

String Formatting
Using format()
Allows formatting of strings with placeholders.

Using f-strings (Python 3.6+)
Provides a more concise way to format strings.

Escape Characters
Special characters can be included in strings using escape sequences.

Multiline Strings
Multiline strings can be created using triple quotes.

String Immutability
Strings in Python are immutable, meaning that once a string is created, it cannot be changed. 
Any operations that modify a string will return a new string.
"""