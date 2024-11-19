def full_adder(A, B, Cin):
    # XOR for Sum
    Sum = A ^ B ^ Cin
    # Carry = AB + BCin + ACin
    Carry = (A & B) | (B & Cin) | (A & Cin)
    return Sum, Carry

# Example usage
A = int(input("Enter first binary digit (0 or 1): "))
B = int(input("Enter second binary digit (0 or 1): "))
Cin = int(input("Enter carry input (0 or 1): "))

if A in (0, 1) and B in (0, 1) and Cin in (0, 1):
    Sum, Carry = full_adder(A, B, Cin)
    print(f"Full Adder Results: Sum = {Sum}, Carry = {Carry}")
else:
    print("Invalid input! Please enter binary digits only (0 or 1).")

# A full adder adds three binary digits: two inputs and one carry from a previous addition. It provides two outputs: Sum and Carry.

'''
Here is a line-by-line breakdown of the provided Python code:

def full_adder(A, B, Cin):
Defines a function named full_adder that takes three arguments: 
A, B, and Cin, which represent two binary digits and a carry input, respectively.

Sum = A ^ B ^ Cin
Performs the XOR operation between A, B, and Cin. The result of this operation will give the sum bit of the full adder. 
If an odd number of inputs are 1, the result will be 1; otherwise, it will be 0.

Carry = (A & B) | (B & Cin) | (A & Cin)
Calculates the carry bit using the logic for a full adder. The carry is set to 1 if any two or more of the inputs (A, B, Cin) are 1. 
This is represented by the OR of the AND operations between each pair of inputs.

return Sum, Carry
Returns the Sum and Carry values, which represent the sum and carry bits from the full adder.

A = int(input("Enter first binary digit (0 or 1): "))
Prompts the user to input the first binary digit, converts it to an integer, and stores it in variable A.

B = int(input("Enter second binary digit (0 or 1): "))
Prompts the user to input the second binary digit, converts it to an integer, and stores it in variable B.

Cin = int(input("Enter carry input (0 or 1): "))
Prompts the user to input the carry input, converts it to an integer, and stores it in variable Cin.

if A in (0, 1) and B in (0, 1) and Cin in (0, 1):
Checks if A, B, and Cin are all valid binary digits (either 0 or 1). If all inputs are valid, the code inside the if block is executed.

Sum, Carry = full_adder(A, B, Cin)
Calls the full_adder function with A, B, and Cin as arguments, and stores the returned values in variables Sum and Carry.

print(f"Full Adder Results: Sum = {Sum}, Carry = {Carry}")
Prints the results of the full adder, displaying the Sum and Carry values returned by the function.

else:
If any of the inputs (A, B, or Cin) are not valid binary digits, the else block will execute.

print("Invalid input! Please enter binary digits only (0 or 1).")
Prints a message informing the user that the input was invalid and that only binary digits (0 or 1) should be entered.
'''