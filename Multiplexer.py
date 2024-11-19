def multiplexer_4to1(S0, S1, I0, I1, I2, I3):
    """
    4-to-1 Multiplexer: Selects one of the four inputs based on the values of two select lines.
    
    :param S0: Select line 0 (binary, 0 or 1)
    :param S1: Select line 1 (binary, 0 or 1)
    :param I0, I1, I2, I3: Four input lines (binary values, 0 or 1)
    :return: The selected input based on the select lines S0 and S1.
    """
    # Ensure select lines and inputs are valid binary digits
    if S0 not in (0, 1) or S1 not in (0, 1):
        raise ValueError("Select lines S0 and S1 must be binary (0 or 1).")
    if not all(i in (0, 1) for i in [I0, I1, I2, I3]):
        raise ValueError("Input lines I0, I1, I2, and I3 must be binary (0 or 1).")
    
    # Determine the index based on select lines S1 and S0
    index = (S1 << 1) | S0  # Generate a 2-bit index from S1 and S0

    # Return the selected input based on the index
    if index == 0:
        return I0
    elif index == 1:
        return I1
    elif index == 2:
        return I2
    elif index == 3:
        return I3

# Example usage
try:
    S0 = int(input("Enter select line S0 (0 or 1): "))
    S1 = int(input("Enter select line S1 (0 or 1): "))
    I0 = int(input("Enter input I0 (0 or 1): "))
    I1 = int(input("Enter input I1 (0 or 1): "))
    I2 = int(input("Enter input I2 (0 or 1): "))
    I3 = int(input("Enter input I3 (0 or 1): "))

    selected_output = multiplexer_4to1(S0, S1, I0, I1, I2, I3)
    print(f"The selected output based on the select lines is: {selected_output}")
except ValueError as e:
    print(e)

'''
A multiplexer (MUX) is a digital electronic device that selects one of several input signals and forwards 
the selected input to a single output line. The selection of the input is controlled by a set of select lines.
'''

'''
Function Explanation:

def multiplexer_4to1(S0, S1, I0, I1, I2, I3):
The function multiplexer_4to1 is defined with the following parameters:
S0 and S1 are the select lines, which control which of the four inputs will be passed to the output.
I0, I1, I2, and I3 are the input lines. The output will be one of these based on the values of S0 and S1.

"""
The docstring provides a description of the function's purpose: 
selecting one of four inputs based on the values of the two select lines (S0, S1).

Input Validation:
The code ensures that both S0 and S1 are valid binary values (0 or 1).
It also checks that the input lines I0, I1, I2, and I3 are all binary (either 0 or 1).
If any of these inputs are invalid, a ValueError is raised.

index = (S1 << 1) | S0
The index is calculated by combining the select lines S1 and S0:
S1 << 1 shifts S1 by 1 bit to the left (equivalent to multiplying it by 2).
The bitwise OR (|) combines this result with S0, forming a 2-bit index.
This index determines which input (I0, I1, I2, or I3) will be selected.

Return the selected input:
Based on the value of index, the function selects one of the four inputs:
If index == 0, the function returns I0.
If index == 1, it returns I1.
If index == 2, it returns I2.
If index == 3, it returns I3.

Example Usage:

try:
Starts a try block to catch any input validation errors.

S0 = int(input("Enter select line S0 (0 or 1): "))
Prompts the user to input the value for select line S0.

S1 = int(input("Enter select line S1 (0 or 1): "))
Prompts the user to input the value for select line S1.

I0 = int(input("Enter input I0 (0 or 1): "))
Prompts the user to input the value for input I0.

I1 = int(input("Enter input I1 (0 or 1): "))
Prompts the user to input the value for input I1.

I2 = int(input("Enter input I2 (0 or 1): "))
Prompts the user to input the value for input I2.

I3 = int(input("Enter input I3 (0 or 1): "))
Prompts the user to input the value for input I3.

selected_output = multiplexer_4to1(S0, S1, I0, I1, I2, I3)
Calls the multiplexer_4to1 function with the user inputs and stores the selected output in selected_output.

print(f"The selected output based on the select lines is: {selected_output}")
Prints the selected output.

except ValueError as e:
Catches any ValueError exceptions (e.g., invalid input) and prints the error message.
'''