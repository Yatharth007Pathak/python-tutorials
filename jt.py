# Read the input string
input_string = input("Enter a string: ")

# Read the substring to reverse
substring_to_reverse = input("Enter the substring to reverse: ")

# Check if the substring is in the input string
if substring_to_reverse in input_string:
    # Find the start index of the substring
    start_index = input_string.find(substring_to_reverse)
    
    # Find the end index of the substring
    end_index = start_index + len(substring_to_reverse)
    
    # Reverse the substring
    reversed_substring = substring_to_reverse[::-1]
    
    # Create the modified string by concatenating parts
    modified_string = input_string[:start_index] + reversed_substring + input_string[end_index:]
    
    # Print the modified string
    print("Modified string:", modified_string)
else:
    print("Substring not found in the input string.")

'''
Python program that reads a string containing multiple words, finds a specified word or substring within the string, 
reverses that substring, and then replaces the original substring with the reversed one in the input string.
'''

"""
Here is a line-by-line breakdown of the provided Python code:

input_string = input("Enter a string: ")
This line reads a string of multiple words from the user and stores it in the variable input_string.

substring_to_reverse = input("Enter the substring to reverse: ")
This line reads the substring that the user wants to reverse and stores it in the variable substring_to_reverse.

if substring_to_reverse in input_string:
This line checks if the substring specified by the user exists within the input_string. If it does, the code inside the if block will execute.

    start_index = input_string.find(substring_to_reverse)
This line finds the starting index of the substring within input_string using the find method and stores it in the variable start_index.

    end_index = start_index + len(substring_to_reverse)
This line calculates the ending index of the substring by adding the length of the substring 
to the start_index and stores it in the variable end_index.

    reversed_substring = substring_to_reverse[::-1]
This line reverses the substring using slicing ([::-1]) and stores the reversed substring in the variable reversed_substring.

    modified_string = input_string[:start_index] + reversed_substring + input_string[end_index:]
This line constructs the modified string by concatenating three parts:
input_string[:start_index]: The part of the string before the substring to be reversed.
reversed_substring: The reversed substring.
input_string[end_index:]: The part of the string after the substring to be reversed.

    print("Modified string:", modified_string)
This line prints the modified string with the reversed substring.

else:
    print("Substring not found in the input string.")
If the substring is not found in the input string, this else block is executed, and it prints a message indicating that the substring was not found.
"""