def cla_adder(A, B, Cin):
    """
    Carry Look-Ahead Adder for two binary numbers of the same length.
    
    :param A: Binary string of the first number
    :param B: Binary string of the second number
    :param Cin: Initial carry-in (0 or 1)
    :return: Binary sum and carry-out
    """
    # Ensure both binary numbers are the same length
    n = max(len(A), len(B))
    A = A.zfill(n)
    B = B.zfill(n)

    # Initialize variables
    Sum = ''
    carry = [0] * (n + 1)
    carry[0] = Cin  # Initial carry-in

    # Generate and Propagate arrays
    G = [int(A[i]) & int(B[i]) for i in range(n)]  # Generate: G[i] = A[i] & B[i]
    P = [int(A[i]) | int(B[i]) for i in range(n)]  # Propagate: P[i] = A[i] | B[i]

    # Compute carry bits using CLA logic
    for i in range(1, n + 1):
        carry[i] = G[i - 1] | (P[i - 1] & carry[i - 1])

    # Compute the sum bits
    for i in range(n):
        Sum += str(int(A[i]) ^ int(B[i]) ^ carry[i])

    # Final carry-out
    Cout = carry[n]
    
    return Sum, Cout

# Example usage
A = input("Enter the first binary number: ")
B = input("Enter the second binary number: ")
Cin = int(input("Enter the initial carry-in (0 or 1): "))

# Validate input
if all(bit in '01' for bit in A) and all(bit in '01' for bit in B) and Cin in (0, 1):
    result, Cout = cla_adder(A, B, Cin)
    print(f"The CLA sum of {A} and {B} with Cin={Cin} is: {result}, Carry-out: {Cout}")
else:
    print("Invalid input! Please enter valid binary numbers and carry-in.")

'''
A Carry Look-Ahead (CLA) Adder is a type of binary adder that improves speed by calculating carries in advance, based on the inputs. 
It uses Generate (G) and Propagate (P) signals to determine the carry for each bit position.
'''

'''
Here is a line-by-line breakdown of the Python code for a Carry Look-Ahead Adder (CLA) that adds two binary numbers:

def cla_adder(A, B, Cin):
Defines the function cla_adder which takes three parameters: A (the first binary number), B (the second binary number), 
and Cin (the initial carry-in).

"""Carry Look-Ahead Adder for two binary numbers of the same length.
This is a docstring explaining the purpose of the function, 
which is to add two binary numbers of the same length using the Carry Look-Ahead Adder (CLA) method.

:param A: Binary string of the first number
Describes the parameter A as a binary string representing the first number.

:param B: Binary string of the second number
Describes the parameter B as a binary string representing the second number.

:param Cin: Initial carry-in (0 or 1)
Describes the parameter Cin as the initial carry-in, which can be either 0 or 1.

:return: Binary sum and carry-out
Specifies that the function returns the binary sum and the carry-out of the addition.

n = max(len(A), len(B))
Finds the maximum length of the two binary numbers (A and B) to ensure they are both the same length. The result is stored in variable n.

A = A.zfill(n)
Pads A with leading zeros to ensure it has a length of n.

B = B.zfill(n)
Pads B with leading zeros to ensure it has a length of n.

Sum = ''
Initializes an empty string Sum to store the final binary sum.

carry = [0] * (n + 1)
Initializes a list carry of size n+1 to store the carry bits. The list is initially filled with zeros.

carry[0] = Cin
Sets the first element of the carry list to the initial carry-in value (Cin).

G = [int(A[i]) & int(B[i]) for i in range(n)]
Creates a list G (for generate) where each element is the result of a bitwise AND operation between the corresponding bits of A and B. 
G[i] represents the generate carry for each bit.

P = [int(A[i]) | int(B[i]) for i in range(n)]
Creates a list P (for propagate) where each element is the result of a bitwise OR operation between the corresponding bits of A and B. 
P[i] represents the propagate carry for each bit.

for i in range(1, n + 1):
Starts a loop to compute the carry bits from i = 1 to n (inclusive). 
The loop will compute the carry for each bit position using the CLA logic.

carry[i] = G[i - 1] | (P[i - 1] & carry[i - 1])
The carry for bit position i is calculated using the CLA logic: 
the carry is 1 if there is a generate carry (G[i - 1]), or if the propagate carry (P[i - 1]) and the previous carry (carry[i - 1]) are both 1.

for i in range(n):
Starts a loop to compute the sum bits from i = 0 to n - 1.

Sum += str(int(A[i]) ^ int(B[i]) ^ carry[i])
The sum for each bit position is calculated using the XOR operation between the corresponding bits of A, B, and the carry for that bit. 
The result is appended to the Sum string.

Cout = carry[n]
The final carry-out (Cout) is the last carry bit, which is stored in carry[n].

return Sum, Cout
The function returns the binary sum (Sum) and the final carry-out (Cout).

A = input("Enter the first binary number: ")
Prompts the user to input the first binary number and stores it in the variable A.

B = input("Enter the second binary number: ")
Prompts the user to input the second binary number and stores it in the variable B.

Cin = int(input("Enter the initial carry-in (0 or 1): "))
Prompts the user to input the initial carry-in (either 0 or 1) and stores it in the variable Cin.

if all(bit in '01' for bit in A) and all(bit in '01' for bit in B) and Cin in (0, 1):
Validates the input to ensure both A and B consist only of '0' or '1' characters, and Cin is either 0 or 1.

result, Cout = cla_adder(A, B, Cin)
Calls the cla_adder function with A, B, and Cin as arguments, and stores the result in result and the carry-out in Cout.

print(f"The CLA sum of {A} and {B} with Cin={Cin} is: {result}, Carry-out: {Cout}")
Prints the CLA sum and the carry-out in a readable format.

else:
If the input is invalid (not binary or incorrect carry-in), the code enters this block.

print("Invalid input! Please enter valid binary numbers and carry-in.")
Prints an error message if the input is invalid.
'''