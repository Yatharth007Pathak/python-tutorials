import string

def remove_punctuations(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the translate method to remove all punctuation
    return input_string.translate(translator)

# Prompt the user for input
user_input = input("Enter a string with punctuation: ")

# Remove punctuations from the input string
cleaned_string = remove_punctuations(user_input)

# Print the result
print("Original string:", user_input)
print("String without punctuation:", cleaned_string)

# Python program to input a string and remove all the punctuations from a string


"""
Let's break down the code step by step:

import string: This imports the string module, 
which contains constants and utilities related to string operations, including string.punctuation that lists all punctuation characters.

def remove_punctuations(input_string):: This defines a function named remove_punctuations that takes input_string as its parameter.
translator = str.maketrans('', '', string.punctuation):
str.maketrans('', '', string.punctuation): Creates a translation table.
The first two empty strings ('') specify that no characters are being mapped to new characters, and the third argument (string.punctuation) 
specifies the characters to be removed (i.e., all punctuation characters).
return input_string.translate(translator):
input_string.translate(translator): Applies the translation table to the input_string, effectively removing all punctuation characters.
The function returns the modified string with punctuation removed.

input("Enter a string with punctuation: "): Prompts the user to enter a string. The input is stored in the variable user_input.

cleaned_string = remove_punctuations(user_input):
Calls the remove_punctuations function with the user's input and stores the result in cleaned_string.

print("Original string:", user_input): Prints the original string entered by the user.
print("String without punctuation:", cleaned_string): Prints the string after punctuation has been removed.
"""