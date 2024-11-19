def multiplier_with_enable(A, B, Enable):
    """
    2-bit Multiplier with Enable: Multiplies two 2-bit binary numbers only if Enable is 1.
    
    :param A: First 2-bit binary input (string)
    :param B: Second 2-bit binary input (string)
    :param Enable: Enable signal (0 or 1)
    :return: The product (4-bit binary) or 0 if Enable = 0
    """
    # Ensure inputs are valid binary digits of length 2
    if len(A) != 2 or len(B) != 2 or not all(bit in '01' for bit in A) or not all(bit in '01' for bit in B):
        raise ValueError("A and B must be 2-bit binary numbers.")
    if Enable not in (0, 1):
        raise ValueError("Enable must be 0 or 1.")

    # If Enable is 0, return product as 0
    if Enable == 0:
        return '0000'

    # Convert binary strings A and B to integers
    int_A = int(A, 2)
    int_B = int(B, 2)

    # Multiply the numbers
    product = int_A * int_B

    # Convert the product to a 4-bit binary string
    return bin(product)[2:].zfill(4)

# Example usage
try:
    A = input("Enter the first 2-bit binary number (e.g., 01): ")
    B = input("Enter the second 2-bit binary number (e.g., 10): ")
    Enable = int(input("Enter the Enable signal (0 or 1): "))

    product = multiplier_with_enable(A, B, Enable)
    print(f"The product of {A} and {B} with Enable = {Enable} is: {product}")
except ValueError as e:
    print(e)

'''
A multiplier with enable in digital electronics multiplies two binary numbers, 
but the multiplication only occurs when an enable signal is set to 1. 
If the enable signal is 0, the output should be 0 regardless of the input numbers.
'''

'''
Here's a breakdown of the multiplier_with_enable function:

def multiplier_with_enable(A, B, Enable):
Defines the function multiplier_with_enable, which takes three parameters: A (the first binary number), B (the second binary number), a
nd Enable (a control signal to enable or disable the multiplication).

"""
The docstring explains that the function multiplies two 2-bit binary numbers only if the Enable signal is 1. If Enable is 0, it returns 0.

# Ensure inputs are valid binary digits of length 2
Comment indicating that the input validation step ensures both binary inputs are exactly 2 bits long and contain 
only valid binary digits ('0' or '1').

if len(A) != 2 or len(B) != 2 or not all(bit in '01' for bit in A) or not all(bit in '01' for bit in B):
Checks that both inputs A and B are 2 bits long and that each character in the strings is either '0' or '1'. 
If this condition fails, it raises a ValueError.

raise ValueError("A and B must be 2-bit binary numbers.")
If the validation fails, an error is raised to inform the user that both inputs must be 2-bit binary numbers.

if Enable not in (0, 1):
Ensures that the Enable input is either 0 or 1. If it's not, a ValueError is raised.

raise ValueError("Enable must be 0 or 1.")
If Enable is not 0 or 1, an error message is shown.

# If Enable is 0, return product as 0
Comment explaining that if Enable is 0, the function will return 0000 as the product (indicating multiplication is disabled).

if Enable == 0:
If Enable is 0, the function immediately returns the 4-bit binary string '0000', representing the zero product.

int_A = int(A, 2)
Converts the binary string A to its decimal (integer) equivalent using int(A, 2).

int_B = int(B, 2)
Converts the binary string B to its decimal (integer) equivalent in the same way.

product = int_A * int_B
Multiplies the two decimal integers int_A and int_B.

# Convert the product to a 4-bit binary string
Comment indicating that the product will be converted back to a 4-bit binary string.

return bin(product)[2:].zfill(4)
Converts the product to a binary string using bin(), which returns a string prefixed with '0b'. 
The [2:] slices off the '0b' prefix, and .zfill(4) pads the binary result to 4 bits if necessary.

Example Usage:

try:
Starts a try block to handle potential input errors.

A = input("Enter the first 2-bit binary number (e.g., 01): ")
Prompts the user to input the first 2-bit binary number.

B = input("Enter the second 2-bit binary number (e.g., 10): ")
Prompts the user to input the second 2-bit binary number.

Enable = int(input("Enter the Enable signal (0 or 1): "))
Prompts the user to input the Enable signal, which is either 0 or 1.

product = multiplier_with_enable(A, B, Enable)
Calls the multiplier_with_enable function with the user inputs and stores the result in product.

print(f"The product of {A} and {B} with Enable = {Enable} is: {product}")
Prints the result of the multiplication along with the Enable signal.

except ValueError as e:
Catches any ValueError exceptions (e.g., invalid input) and prints the error message.

print(e)
Prints the error message raised by the ValueError.
'''