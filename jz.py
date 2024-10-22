# Input string from user
input_string = input("Enter a string: ")

# Initialize a list from the input string for easy manipulation
modified_list = list(input_string)

# Iterate through the string
i = 0
while i < len(modified_list) - 1:
    # Check if the current character is 'A'
    if modified_list[i] == 'A':
        # Swap the current character with the next one
        modified_list[i], modified_list[i + 1] = modified_list[i + 1], modified_list[i]
        # Move to the next pair of characters
        i += 2
    else:
        # Move to the next character
        i += 1

# Convert the list back to a string
result = ''.join(modified_list)

# Output the modified string
print("Modified string:", result)


'''
python program to input a string and replace two alphabets of a string where the first alphabet starts with A,
 we want to replace these two alphabets by swapping both alphabets
'''

'''
Code Breakdown:
input_string = input("Enter a string: ")
Purpose: This line prompts the user to enter a string and stores the input in the variable input_string.

modified_list = list(input_string)
Purpose: Converts the input string into a list of characters (modified_list). 
This makes it easier to swap characters since lists in Python are mutable (they can be changed in place).

i = 0
while i < len(modified_list) - 1:
Purpose: Initializes an index variable i to 0 and starts a while loop that will run as long as i is less than the length of modified_list minus 1. 
This is to ensure that there is always a next character to swap with.

    if modified_list[i] == 'A':
Purpose: Checks if the current character in the list is 'A'.

        modified_list[i], modified_list[i + 1] = modified_list[i + 1], modified_list[i]
Purpose: If the current character is 'A', this line swaps it with the next character in the list using tuple unpacking. 
The syntax a, b = b, a swaps the values of a and b.

        i += 2
Purpose: After a swap, the index i is incremented by 2 to skip over the next character which has already been swapped.

    else:
        i += 1
Purpose: If the current character is not 'A', just move to the next character by incrementing i by 1.

result = ''.join(modified_list)
Purpose: Joins the list of characters back into a single string result.

print("Modified string:", result)
Purpose: Prints the modified string after the swaps.
'''