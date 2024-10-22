# Input a string from the user
input_string = input("Enter a string: ")

# Initialize substrings for odd and even indexed characters
odd_substring = ""
even_substring = ""

# Generate the substrings based on indices
for i in range(len(input_string)):
    if i % 2 == 0:
        even_substring += input_string[i]
    else:
        odd_substring += input_string[i]

# Merge the substrings
merged_string = even_substring + odd_substring

# Reverse the merged string
reversed_string = merged_string[::-1]

# Output the reversed merged string
print(f"The reversed merged string is: '{reversed_string}'")


"""
Python program to input a string and then generate two substrings.
First substring contains all the odd elements, second substring contains all even elements.
Then we have to merge the two strings and print them in reverse order
"""

'''
Breakdown of the Code:

input_string = input("Enter a string: ")
Prompts the user to enter a string and stores it in input_string.

odd_substring = ""
even_substring = ""
Initializes two empty strings to store characters from odd and even indices.

for i in range(len(input_string)):
    if i % 2 == 0:
        even_substring += input_string[i]
    else:
        odd_substring += input_string[i]
Iterates over each index in input_string. 
Uses the modulus operator to determine if the index is even or odd, and appends the character to the corresponding substring.

merged_string = even_substring + odd_substring
Concatenates even_substring and odd_substring into merged_string.

reversed_string = merged_string[::-1]
Uses slicing to reverse merged_string.

print(f"The reversed merged string is: '{reversed_string}'")
Prints the final reversed merged string.
'''