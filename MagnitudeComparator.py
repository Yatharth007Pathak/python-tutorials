def magnitude_comparator(A, B):
    """
    Compares two binary numbers and determines their relationship.
    
    :param A: Binary string of the first number
    :param B: Binary string of the second number
    :return: A tuple (A > B, A == B, A < B)
    """
    # Convert binary strings to integers
    int_A = int(A, 2)
    int_B = int(B, 2)

    # Compare the numbers
    greater = int_A > int_B
    equal = int_A == int_B
    less = int_A < int_B

    return greater, equal, less

# Example usage
A = input("Enter the first binary number: ")
B = input("Enter the second binary number: ")

# Validate input
if all(bit in '01' for bit in A) and all(bit in '01' for bit in B):
    greater, equal, less = magnitude_comparator(A, B)
    print(f"Comparison of {A} and {B}:")
    print(f"A > B: {greater}")
    print(f"A == B: {equal}")
    print(f"A < B: {less}")
else:
    print("Invalid input! Please enter valid binary numbers.")

'''
A Magnitude Comparator is a combinational circuit in digital electronics that compares 2 binary numbers 
and determines their relative magnitudes, i.e., whether one is greater than, less than, or equal to the other.
'''

'''
Here's a line-by-line breakdown of the Python code for a magnitude comparator that compares two binary numbers:

def magnitude_comparator(A, B):
Defines the function magnitude_comparator, which takes two parameters: A (the first binary number) and B (the second binary number).

"""
This is the start of the docstring that explains the function's purpose.

Compares two binary numbers and determines their relationship.
Describes that the function compares two binary numbers to determine their relationship (greater than, equal to, or less than).

:param A: Binary string of the first number
Describes parameter A as the binary string for the first number.

:param B: Binary string of the second number
Describes parameter B as the binary string for the second number.

:return: A tuple (A > B, A == B, A < B)
Specifies that the function returns a tuple with three boolean values: A > B, A == B, and A < B.

int_A = int(A, 2)
Converts the binary string A into its corresponding integer value (int_A) using the int function with base 2.

int_B = int(B, 2)
Converts the binary string B into its corresponding integer value (int_B) using the int function with base 2.

greater = int_A > int_B
Compares int_A and int_B to check if A is greater than B. The result (True or False) is stored in the greater variable.

equal = int_A == int_B
Compares int_A and int_B to check if they are equal. The result (True or False) is stored in the equal variable.

less = int_A < int_B
Compares int_A and int_B to check if A is less than B. The result (True or False) is stored in the less variable.

return greater, equal, less
Returns a tuple containing the three comparison results (greater, equal, less).

A = input("Enter the first binary number: ")
Prompts the user to input the first binary number and stores it in the variable A.

B = input("Enter the second binary number: ")
Prompts the user to input the second binary number and stores it in the variable B.

if all(bit in '01' for bit in A) and all(bit in '01' for bit in B):
Validates that all characters in A and B are either '0' or '1', ensuring that both inputs are valid binary strings.

greater, equal, less = magnitude_comparator(A, B)
Calls the magnitude_comparator function with A and B as arguments and stores the returned tuple in the variables greater, equal, and less.

print(f"Comparison of {A} and {B}:")
Prints a header for the comparison results.

print(f"A > B: {greater}")
Prints the result of the comparison A > B.

print(f"A == B: {equal}")
Prints the result of the comparison A == B.

print(f"A < B: {less}")
Prints the result of the comparison A < B.

else:
If the input is invalid (contains characters other than '0' or '1'), the code enters this block.

print("Invalid input! Please enter valid binary numbers.")
Prints an error message indicating that the input is invalid.
'''