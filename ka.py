# Input list from user
input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

# Input the element to remove
value_to_remove = int(input("Enter the value to remove: "))

# Remove all occurrences of the value using list comprehension
result_list = [item for item in input_list if item != value_to_remove]

# Output the result
print("List after removing occurrences of", value_to_remove, ":", result_list)

# Python program to remove multiple occurrences of an element from a list

'''
Here's a step-by-step breakdown of the simplified code:

input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
Purpose: Prompts the user to enter a list of integers separated by spaces.
input(): Reads the input from the user as a single string.
.split(): Splits the string into a list of substrings (one for each number).
map(int, ...): Converts each substring to an integer.
list(...): Converts the result from map into a list of integers.
Result: input_list is now a list of integers provided by the user.

value_to_remove = int(input("Enter the value to remove: "))
Purpose: Prompts the user to enter the integer value that should be removed from the list.
input(): Reads the input as a string.
int(): Converts the string input to an integer.
Result: value_to_remove is the integer that will be removed from the list.

result_list = [item for item in input_list if item != value_to_remove]
Purpose: Creates a new list excluding all occurrences of value_to_remove.
List Comprehension: [item for item in input_list if item != value_to_remove]
item for item in input_list: Iterates over each item in input_list.
if item != value_to_remove: Includes the item in the new list only if it is not equal to value_to_remove.
Result: result_list is a list of integers from input_list with value_to_remove excluded.

print("List after removing occurrences of", value_to_remove, ":", result_list)
Purpose: Prints the modified list.
print(): Displays the message along with the value_to_remove and result_list.
Result: Provides the user with the updated list showing the list with the specified element removed.
'''