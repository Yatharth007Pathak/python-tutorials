# Input a string from the user
input_string = input("Enter a string: ")

# Initialize an empty string to hold the reversed string
reversed_string = ""

# Calculate the length of the input string
length = 0
for char in input_string:
    length += 1

# Reverse the string using slicing technique
for i in range(length - 1, -1, -1):
    reversed_string += input_string[i]

# Output the reversed string
print(f"The reversed string is: '{reversed_string}'")



# To reverse a string using slicing in Python

"""
Breakdown of the Code:

input_string = input("Enter a string: ")
Prompts the user to enter a string and stores it in the variable input_string.

reversed_string = ""
Initializes an empty string reversed_string to build the reversed version of the input string.

length = 0
for char in input_string:
    length += 1
Determines the length of the input string by iterating over each character and counting them.

for i in range(length - 1, -1, -1):
    reversed_string += input_string[i]
Iterates from the last index (length - 1) to the first index (0) in reverse order. 
For each index i, appends the character at input_string[i] to reversed_string.

print(f"The reversed string is: '{reversed_string}'")
Prints the reversed string using an f-string to format the output.
"""