'''
A JK flip-flop is a type of flip-flop with two inputs: J and K. It has the following behavior based on the values of J and K:

J = 0, K = 0: No change in the output (Q holds its state).
J = 0, K = 1: Reset the output Q to 0, and Q_bar to 1.
J = 1, K = 0: Set the output Q to 1, and Q_bar to 0.
J = 1, K = 1: Toggle the output Q (Q changes state from 0 to 1 or from 1 to 0).

Truth Table for JK Flip-Flop
J     K       clk       Q(next)       Q_bar(next)
x     x        0       No change       No change
0     0        1       No change       No change
0     1        1         Reset            set
1     0        1          Set            Reset
1     1        1         Toggle         Toggle
'''

def jk_flip_flop(J, K, clk, Q, Q_bar):
    """
    JK Flip-Flop: A flip-flop with J and K inputs, and behavior based on the clock input.
    
    :param J: J input (0 or 1)
    :param K: K input (0 or 1)
    :param clk: Clock input (0 or 1)
    :param Q: Current state (output Q)
    :param Q_bar: Inverted output (Q_bar)
    :return: Tuple containing the next state (Q) and its inversion (Q_bar)
    """
    # Ensure inputs are valid binary digits
    if J not in (0, 1) or K not in (0, 1) or clk not in (0, 1):
        raise ValueError("Inputs J, K, and clk must be binary (0 or 1).")

    # On the rising edge of the clock (clk == 1), perform the state change
    if clk == 1:
        if J == 0 and K == 0:
            # No change in the output (Hold the current state)
            Q_next = Q
            Q_bar_next = Q_bar
        elif J == 0 and K == 1:
            # Reset the output (Q = 0, Q_bar = 1)
            Q_next = 0
            Q_bar_next = 1
        elif J == 1 and K == 0:
            # Set the output (Q = 1, Q_bar = 0)
            Q_next = 1
            Q_bar_next = 0
        elif J == 1 and K == 1:
            # Toggle the output (Q = NOT Q, Q_bar = NOT Q_bar)
            Q_next = 1 - Q
            Q_bar_next = 1 - Q_bar
    else:
        # If clock is 0, hold the current state
        Q_next = Q
        Q_bar_next = Q_bar

    return Q_next, Q_bar_next

# Example usage
try:
    J = int(input("Enter the J input (0 or 1): "))
    K = int(input("Enter the K input (0 or 1): "))
    clk = int(input("Enter the clock input (0 or 1): "))
    Q = int(input("Enter the current state Q (0 or 1): "))
    Q_bar = 1 - Q  # Invert Q to get Q_bar
    
    Q_next, Q_bar_next = jk_flip_flop(J, K, clk, Q, Q_bar)
    print(f"Next state (Q): {Q_next}")
    print(f"Next state inverted (Q_bar): {Q_bar_next}")
except ValueError as e:
    print(e)

'''
Here's a line-by-line breakdown of the jk_flip_flop function:

Function definition:
def jk_flip_flop(J, K, clk, Q, Q_bar): defines the function jk_flip_flop, simulating the behavior of a JK Flip-Flop, 
which takes five parameters: J, K, clk, Q, and Q_bar.

Docstring:
The docstring explains the purpose of the function: it simulates the behavior of a JK Flip-Flop, 
describing the parameters and the expected return values. J and K are the inputs, clk is the clock signal, Q is the current state, 
and Q_bar is the inverted state. The function returns the next state (Q_next) and its inversion (Q_bar_next).

Input validation (binary check):
if J not in (0, 1) or K not in (0, 1) or clk not in (0, 1): checks if any of the inputs J, K, or clk are not binary values (either 0 or 1).
raise ValueError("Inputs J, K, and clk must be binary (0 or 1).") raises an error if the condition is true, as the inputs must be binary.

State change on the rising edge of the clock:
if clk == 1: checks if the clock (clk) is at its rising edge (1). State changes only occur on the rising edge of the clock in a JK Flip-Flop.

If J == 0 and K == 0 (Hold the current state):
Q_next = Q keeps the current state.
Q_bar_next = Q_bar keeps the inverted state.

If J == 0 and K == 1 (Reset the output):
Q_next = 0 resets the output to 0.
Q_bar_next = 1 sets the inverted output to 1.

If J == 1 and K == 0 (Set the output):
Q_next = 1 sets the output to 1.
Q_bar_next = 0 sets the inverted output to 0.

If J == 1 and K == 1 (Toggle the output):
Q_next = 1 - Q toggles the state of Q. If Q was 0, it becomes 1, and if Q was 1, it becomes 0.
Q_bar_next = 1 - Q_bar toggles the state of Q_bar accordingly.

Hold the current state when the clock is 0:
else: handles the case when the clock (clk) is not at its rising edge (i.e., clk == 0), in which case the state is held.
Q_next = Q keeps the current state.
Q_bar_next = Q_bar keeps the inverted state.

Returning the next state and its inversion:
return Q_next, Q_bar_next returns the next state (Q_next) and its inversion (Q_bar_next).

Example usage with input prompts:
try: starts a block to attempt user input and handle potential errors.
J = int(input("Enter the J input (0 or 1): ")) asks the user to input the value for J (0 or 1).
K = int(input("Enter the K input (0 or 1): ")) asks the user to input the value for K.
clk = int(input("Enter the clock input (0 or 1): ")) asks the user to input the clock signal value.
Q = int(input("Enter the current state Q (0 or 1): ")) asks for the current state Q.
Q_bar = 1 - Q calculates the inverted state Q_bar by subtracting Q from 1.

Calling the jk_flip_flop function:
Q_next, Q_bar_next = jk_flip_flop(J, K, clk, Q, Q_bar) calls the jk_flip_flop function with the provided inputs and 
stores the result in Q_next and Q_bar_next.

Displaying the next state:
print(f"Next state (Q): {Q_next}") prints the next state Q_next.
print(f"Next state inverted (Q_bar): {Q_bar_next}") prints the inverted next state Q_bar_next.

Error handling:
except ValueError as e: catches any ValueError exceptions, such as invalid input.
print(e) prints the error message if an exception occurs, providing feedback to the user on what went wrong.
'''