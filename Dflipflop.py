'''
A D flip-flop (Data flip-flop) is a type of flip-flop used to store a single bit of data. 
The state of the flip-flop is determined by the Data (D) input and the Clock (CLK) input. 
The flip-flop captures the value of the D input on the rising edge of the CLK signal.
It has one input (D), one output (Q), and an inverted output (Q_bar). 
The output follows the D input when the clock transitions from 0 to 1.

D = 1, CLK = 1: The output Q will be set to 1.
D = 0, CLK = 1: The output Q will be set to 0.
The state will hold the previous value when CLK = 0, meaning no change occurs unless the clock signal is high (1).

Truth Table for D Flip-Flop
D    clk       Q(next)       Q_bar(next)
0     0       No change       No change
0     1           0               1
1     0       No change       No change
1     1           1               0
'''

def d_flip_flop(D, clk, Q, Q_bar):
    """
    D Flip-Flop: A flip-flop with a Data input (D) and a Clock input (clk).
    
    :param D: Data input (0 or 1)
    :param clk: Clock input (0 or 1)
    :param Q: Current state (output Q)
    :param Q_bar: Inverted output (Q_bar)
    :return: Tuple containing the next state (Q) and its inversion (Q_bar)
    """
    # Ensure inputs are valid binary digits
    if D not in (0, 1) or clk not in (0, 1):
        raise ValueError("Inputs D and clk must be binary (0 or 1).")

    # On the rising edge of the clock (clk == 1), update the state
    if clk == 1:
        Q_next = D
    else:
        Q_next = Q  # Hold the current state
    
    # Invert Q_next to get Q_bar
    Q_bar_next = 1 - Q_next

    return Q_next, Q_bar_next

# Example usage
try:
    D = int(input("Enter the data input D (0 or 1): "))
    clk = int(input("Enter the clock input clk (0 or 1): "))
    Q = int(input("Enter the current state Q ( 0 or 1): "))
    Q_bar = 1 - Q  # Invert Q to get Q_bar
    
    Q_next, Q_bar_next = d_flip_flop(D, clk, Q, Q_bar)
    print(f"Next state (Q): {Q_next}")
    print(f"Next state inverted (Q_bar): {Q_bar_next}")
except ValueError as e:
    print(e)

'''
Here's a line-by-line breakdown of the d_flip_flop function:

Function definition:
def d_flip_flop(D, clk, Q, Q_bar): defines the d_flip_flop function, simulating the behavior of a D Flip-Flop. 
It takes four parameters: D (data input), clk (clock input), Q (current state), and Q_bar (inverted current state).

Docstring:
The docstring explains the purpose of the function, which simulates the D Flip-Flop behavior. 
It describes the inputs (D, clk, Q, and Q_bar) and the expected return values. 
The function returns a tuple containing the next state (Q_next) and its inversion (Q_bar_next).

Input validation (binary check):
if D not in (0, 1) or clk not in (0, 1): checks if either D or clk is not a binary value (either 0 or 1).
raise ValueError("Inputs D and clk must be binary (0 or 1).") raises a ValueError if the inputs are invalid, 
ensuring that D and clk are either 0 or 1.

State change on the rising edge of the clock:
if clk == 1: checks if the clock signal (clk) is at its rising edge (i.e., clk == 1).
Q_next = D sets the next state (Q_next) equal to the data input D when the clock is at the rising edge.

Hold the current state when the clock is not active:
else: handles the case where clk == 0 (when the clock is not active).
Q_next = Q ensures the current state is held when the clock is 0, meaning the next state remains the same as the current state (Q).

Invert Q_next to get Q_bar_next:
Q_bar_next = 1 - Q_next calculates the inverted state by subtracting Q_next from 1. 
If Q_next is 0, Q_bar_next will be 1; if Q_next is 1, Q_bar_next will be 0.

Returning the next state and its inversion:
return Q_next, Q_bar_next returns the next state (Q_next) and its inversion (Q_bar_next).

Example usage with input prompts:
try: begins a block to handle user input and errors.
D = int(input("Enter the data input D (0 or 1): ")) prompts the user to input the data value D (either 0 or 1).
clk = int(input("Enter the clock input clk (0 or 1): ")) prompts the user to input the clock signal (clk).
Q = int(input("Enter the current state Q ( 0 or 1): ")) asks the user to input the current state (Q).
Q_bar = 1 - Q calculates the inverted state Q_bar by subtracting Q from 1.

Calling the d_flip_flop function:
Q_next, Q_bar_next = d_flip_flop(D, clk, Q, Q_bar) calls the d_flip_flop function with the user-provided inputs and 
stores the results in Q_next and Q_bar_next.

Displaying the next state:
print(f"Next state (Q): {Q_next}") prints the next state (Q_next).
print(f"Next state inverted (Q_bar): {Q_bar_next}") prints the inverted next state (Q_bar_next).

Error handling:
except ValueError as e: catches any ValueError exceptions (e.g., invalid input).
print(e) prints the error message if an exception occurs, providing feedback to the user on what went wrong.
'''