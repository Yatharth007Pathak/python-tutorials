def reverse_substring_in_string(input_string, substring_to_reverse):
    # Check if the substring is in the input string
    if substring_to_reverse in input_string:
        # Reverse the substring
        reversed_substring = substring_to_reverse[::-1]
        # Replace the original substring with the reversed substring
        modified_string = input_string.replace(substring_to_reverse, reversed_substring, 1)
        return modified_string
    else:
        return "Substring not found in the input string."

# Example usage
input_string = input("Enter a string: ")
substring_to_reverse = input("Enter the substring to reverse: ")

result = reverse_substring_in_string(input_string, substring_to_reverse)
print("Modified string:", result)



'''
Python program that reads a string containing multiple words, finds a specified word or substring within the string, 
reverses that substring, and then replaces the original substring with the reversed one in the input string.
'''

"""
let's break down each line of the function reverse_substring_in_string and the example usage:

def reverse_substring_in_string(input_string, substring_to_reverse):
This line defines a function named reverse_substring_in_string that takes two parameters: input_string and substring_to_reverse.

    if substring_to_reverse in input_string:
This line checks if substring_to_reverse is present in input_string. If it is, the code inside the if block will execute.

        reversed_substring = substring_to_reverse[::-1]
This line reverses substring_to_reverse using slicing. [::-1] is a slicing operation that returns a reversed copy of the string.

        modified_string = input_string.replace(substring_to_reverse, reversed_substring, 1)
This line replaces the first occurrence (1) of substring_to_reverse in input_string with reversed_substring. 
The result is stored in modified_string.

        return modified_string
This line returns modified_string.

    else:
This line begins the else block, which executes if substring_to_reverse is not found in input_string.

        return "Substring not found in the input string."
This line returns the message "Substring not found in the input string." if the else block is executed.

input_string = input("Enter a string: ")
This line prompts the user to enter a string and stores the input in the variable input_string.

substring_to_reverse = input("Enter the substring to reverse: ")
This line prompts the user to enter the substring they want to reverse and stores the input in the variable substring_to_reverse.

result = reverse_substring_in_string(input_string, substring_to_reverse)
This line calls the function reverse_substring_in_string with input_string and substring_to_reverse as arguments, 
and stores the result in the variable result.

print("Modified string:", result)
This line prints the message "Modified string:" followed by the value of result.
"""