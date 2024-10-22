# Input the main string and the substring to search
main_string = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

# Initialize variables
index = 0
occurrences = []

# Search for occurrences
while True:
    # Find the index of the substring starting from the current index
    index = main_string.find(substring, index)
    if index == -1:
        break
    occurrences.append(index)
    index += 1  # Move to the next character after the current found substring

# Print results
if occurrences:
    print("Occurrences found at indices:", occurrences)
else:
    print("Substring not found in the main string.")



# Python program to input a string and to search multiple occurrences of a substring in a given string

"""
let's break down each line of the simplified Python program:

main_string = input("Enter the main string: "): Prompts the user to enter the main string and stores it in the variable main_string.
substring = input("Enter the substring to search: "): Prompts the user to enter the substring to search for and stores it in the variable substring.

index = 0: Initializes the variable index to 0. This variable keeps track of the current position in main_string from where the search will start.
occurrences = []: Initializes an empty list occurrences to store the indices where the substring is found.

while True:: Starts an infinite loop that will continue until it is explicitly broken.
index = main_string.find(substring, index): Uses the find method to search for the substring in main_string starting from the current index.
        It updates index with the position where the substring is found, or -1 if the substring is not found.
if index == -1:: Checks if find returned -1, indicating that the substring is not found.
break: Exits the loop if the substring is not found.
occurrences.append(index): Adds the current index to the occurrences list.
index += 1: Increments index by 1 to move past the current found substring, ensuring that the search continues from the next position.

if occurrences:: Checks if the occurrences list is not empty (i.e., there are found indices).
print("Occurrences found at indices:", occurrences): Prints the indices where the substring was found.
else:: If occurrences is empty, this block is executed.
print("Substring not found in the main string."): Prints a message indicating that the substring was not found in the main string.
"""