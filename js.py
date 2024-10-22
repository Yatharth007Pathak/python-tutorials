# Input string from user
input_string = input("Enter a string with multiple words: ")

# Split the string into words
words = input_string.split()

# Iterate through each word
for word in words:
    print(f"Word: {word}")
    
    # Create an empty dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the word
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find and print duplicate characters
    duplicates = []
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
    
    # Print duplicates if any
    if duplicates:
        print(f"Duplicate characters: {' '.join(duplicates)}")
    else:
        print("No duplicate characters")
    
    print()  # Print a newline for better readability

# Python program that takes a string containing multiple words as input and prints duplicate characters for each word

"""
 Let's go through each line of the code and explain what it does:

input_string = input("Enter a string with multiple words: ")
This line prompts the user to enter a string with multiple words and stores the input in the variable input_string.

words = input_string.split()
This line splits the input string into a list of words. 
The split() method splits the string at each whitespace character and returns a list of words.

for word in words:
This line starts a for loop that iterates through each word in the list words.

    print(f"Word: {word}")
This line prints the current word being processed in the loop.

    char_count = {}
This line initializes an empty dictionary char_count that will be used to store the count of each character in the current word.

    for char in word:
This line starts a nested for loop that iterates through each character in the current word.

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
This if-else block checks if the character char is already in the dictionary char_count. 
If it is, it increments the count of that character by 1. If it is not, it adds the character to the dictionary with a count of 1.

    duplicates = []
This line initializes an empty list duplicates that will be used to store characters that appear more than once in the current word.

    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)
This loop iterates through each item in the dictionary char_count. 
For each character char and its count count, it checks if the count is greater than 1. If it is, it adds the character to the duplicates list.

    # Print duplicates if any
    if duplicates:
        print(f"Duplicate characters: {' '.join(duplicates)}")
    else:
        print("No duplicate characters")
This if-else block checks if there are any duplicate characters in the duplicates list. 
If there are, it prints them. If not, it prints "No duplicate characters".

    print()  # Print a newline for better readability
This line prints a newline for better readability, separating the output for each word.

The complete code together allows the user to input a string, processes each word to find duplicate characters, 
and prints the results in a readable format.
"""