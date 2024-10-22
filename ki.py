import string

# Defining the Function to Remove Punctuation from a Single String
def remove_punctuations(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the translate method to remove all punctuation
    return input_string.translate(translator)

# Defining the Function to Remove Punctuation from a List of Strings
def remove_punctuations_from_list(string_list):
    # Apply the remove_punctuations function to each element in the list
    return [remove_punctuations(s) for s in string_list]

# Example list of strings with punctuation
string_list = ["Hello, world!", "Python is great.", "Let's code!"]

# Remove punctuations from each string in the list
cleaned_list = remove_punctuations_from_list(string_list)

# Print the result
print("Original list:", string_list)
print("List without punctuation:", cleaned_list)

# Python program to remove all punctuations from a list, where each element is a string

"""
breakdown of the code that removes all punctuations from each string in a list:

def remove_punctuations(input_string):: Defines a function named remove_punctuations that takes a single string (input_string) as input.
translator = str.maketrans('', '', string.punctuation):
str.maketrans('', '', string.punctuation): Creates a translation table. The first two arguments are empty strings, 
indicating no replacement characters are specified. The third argument (string.punctuation) lists the characters to be removed.
return input_string.translate(translator):
input_string.translate(translator): Uses the translation table to remove all punctuation from input_string.
The function returns the modified string with punctuation removed.

def remove_punctuations_from_list(string_list):: Defines a function that takes a list of strings (string_list) as input.
return [remove_punctuations(s) for s in string_list]:
Uses a list comprehension to apply the remove_punctuations function to each string (s) in string_list.
remove_punctuations(s): Calls the function to remove punctuation from each string.
Creates a new list with the cleaned strings and returns it.
"""