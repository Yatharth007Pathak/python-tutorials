# Input a string from the user
input_string = input("Enter a string: ")

# Input the start and end indices for slicing
start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))

# Initialize an empty string to hold the substring
substring = ""

# Generate the substring manually
for i in range(start, end):
    substring += input_string[i]

# Output the substring
print(f"The substring from index {start} to {end} is: '{substring}'")


# Python program that takes a string as input and generates substrings using slicing 

"""
 let's break down each line of the provided Python code:

input_string = input("Enter a string: ")
Purpose: This line prompts the user to enter a string and stores the input in the variable input_string.

start = int(input("Enter the start index: "))
end = int(input("Enter the end index: "))
Purpose: These lines prompt the user to enter the start and end indices for the substring. 
The input() function gets the user input as a string, and int() converts it to an integer. The values are stored in start and end.

substring = ""
Purpose: This line initializes an empty string substring which will be used to build the substring by concatenating characters.

for i in range(start, end):
    substring += input_string[i]
Purpose: This for loop iterates over the range of indices from start to end (excluding end). 
For each index i, it accesses the character at input_string[i] and appends it to the substring.

print(f"The substring from index {start} to {end} is: '{substring}'")
Purpose: This line prints the final result. It uses an f-string to format the output, 
displaying the generated substring along with the indices used.

Summary
User Input: Collects the string and indices from the user.
Initialization: Prepares an empty string to store the result.
Substring Generation: Manually creates the substring by iterating through the specified indices.
Output: Displays the resulting substring.
"""