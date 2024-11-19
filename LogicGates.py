def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def not_gate(a):
    return 1 - a  # Inverts 0 to 1 and 1 to 0

def nand_gate(a, b):
    return 1 - (a & b)

def nor_gate(a, b):
    return 1 - (a | b)

def xor_gate(a, b):
    return a ^ b

def xnor_gate(a, b):
    return 1 - (a ^ b)

def get_input():
    # Getting binary inputs from the user (either 0 or 1)
    a = int(input("Enter the first input (0 or 1): "))
    b = int(input("Enter the second input (0 or 1): "))
    
    if a not in [0, 1] or b not in [0, 1]:
        print("Invalid input. Please enter 0 or 1.")
        return None, None
    return a, b

def logic_gates():
    a, b = get_input()
    if a is None or b is None:
        return
    
    print(f"\nLogic Gate Outputs for inputs {a} and {b}:")

    print(f"AND Gate: {and_gate(a, b)}")
    print(f"OR Gate: {or_gate(a, b)}")
    print(f"NOT Gate (for the first input): {not_gate(a)}")
    print(f"NOT Gate (for the second input): {not_gate(b)}")
    print(f"NAND Gate: {nand_gate(a, b)}")
    print(f"NOR Gate: {nor_gate(a, b)}")
    print(f"XOR Gate: {xor_gate(a, b)}")
    print(f"XNOR Gate: {xnor_gate(a, b)}")

# Call the function to display the results
logic_gates()

'''
How It Works:
Gate Functions:
AND Gate: Returns 1 if both inputs are 1, otherwise 0.
OR Gate: Returns 1 if at least one input is 1, otherwise 0.
NOT Gate: Inverts the input (i.e., 1 becomes 0 and 0 becomes 1).
NAND Gate: Returns the inverse of the AND gate.
NOR Gate: Returns the inverse of the OR gate.
XOR Gate: Returns 1 if the inputs are different, otherwise 0.
XNOR Gate: Returns the inverse of the XOR gate.
User Input: The program asks for two binary inputs (either 0 or 1).
If the inputs are valid, it proceeds to evaluate the outputs of the logic gates.
Output: The program outputs the result of each logic gate for the provided inputs.
'''

'''
This code defines a series of basic logic gates in Python, along with a function to get binary inputs 
and display the results of applying those inputs to each gate. Here's a breakdown of the code:

Functions:
and_gate(a, b): Returns the result of the AND operation (a & b).
or_gate(a, b): Returns the result of the OR operation (a | b).
not_gate(a): Returns the result of the NOT operation, flipping the binary value (1 - a), where a is either 0 or 1.
nand_gate(a, b): Returns the result of the NAND operation, which is the inverse of AND (1 - (a & b)).
nor_gate(a, b): Returns the result of the NOR operation, which is the inverse of OR (1 - (a | b)).
xor_gate(a, b): Returns the result of the XOR operation (a ^ b), which outputs 1 if a and b are different.
xnor_gate(a, b): Returns the result of the XNOR operation, which is the inverse of XOR (1 - (a ^ b)), and outputs 1 if a and b are the same.

User Input:
get_input():
This function gets two binary inputs (0 or 1) from the user. 
It checks if the inputs are valid; if not, it returns None for both inputs and prompts the user to enter correct values.

Main Function:
logic_gates():
This function calls get_input() to get two binary inputs and checks if they are valid.
If the inputs are valid, it applies these inputs to each logic gate and prints the results.
'''