def half_adder(A, B):
    # XOR operation for Sum
    Sum = A ^ B
    # AND operation for Carry
    Carry = A & B
    return Sum, Carry

# Example usage
A = int(input("Enter first binary digit (0 or 1): "))
B = int(input("Enter second binary digit (0 or 1): "))

if A in (0, 1) and B in (0, 1):
    Sum, Carry = half_adder(A, B)
    print(f"Half Adder Results: Sum = {Sum}, Carry = {Carry}")
else:
    print("Invalid input! Please enter binary digits only (0 or 1).")

# A half adder adds two binary digits and provides two outputs: Sum and Carry.

'''
Here is a breakdown of the Python code line by line:

def half_adder(A, B):
Defines a function named half_adder that takes two arguments A and B. 
These represent the two binary digits (0 or 1) that will be input by the user.

Sum = A ^ B
Performs the XOR (exclusive OR) operation between A and B. 
The XOR operation returns 1 if A and B are different, and 0 if they are the same. The result is stored in the variable Sum.

Carry = A & B
Performs the AND operation between A and B. The AND operation returns 1 only if both A and B are 1. The result is stored in the variable Carry.

return Sum, Carry
The function returns two values: Sum and Carry, which represent the sum and carry bits from the half-adder logic.

A = int(input("Enter first binary digit (0 or 1): "))
Prompts the user to input the first binary digit, converts it to an integer using int(), and stores it in variable A.

B = int(input("Enter second binary digit (0 or 1): "))
Prompts the user to input the second binary digit, converts it to an integer, and stores it in variable B.

if A in (0, 1) and B in (0, 1):
Checks if both A and B are valid binary digits, i.e., either 0 or 1. If both values are valid, the code inside the if block will be executed.

Sum, Carry = half_adder(A, B)
Calls the half_adder function with A and B as arguments, and stores the returned values in variables Sum and Carry.

print(f"Half Adder Results: Sum = {Sum}, Carry = {Carry}")
Prints the results of the half-adder, displaying the Sum and Carry values returned by the function.

else:
If the input values for A or B are not valid binary digits, the else block will execute.

print("Invalid input! Please enter binary digits only (0 or 1).")
Prints a message informing the user that the input was invalid and they should enter binary digits (0 or 1) only.
'''