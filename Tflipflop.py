'''
A T flip-flop (Toggle flip-flop) is a type of flip-flop that toggles its output on every rising edge of the clock signal 
when the T (Toggle) input is high (1). If T is low (0), the flip-flop holds its state (no change in the output).

Behavior of the T Flip-Flop:
T = 0: No change in the output (Q holds its state).
T = 1: The output Q toggles (flips) its state.
The output Q changes from 0 to 1 or from 1 to 0 on each rising edge of the clock.
'''

def t_flip_flop(T, clk, Q, Q_bar):
    """
    T Flip-Flop: A flip-flop that toggles its state on the rising edge of the clock
    when T is 1. If T is 0, the state remains the same.
    
    :param T: Toggle input (0 or 1)
    :param clk: Clock input (0 or 1)
    :param Q: Current state (output Q)
    :param Q_bar: Inverted output (Q_bar)
    :return: Tuple containing the next state (Q) and its inversion (Q_bar)
    """
    # Ensure inputs are valid binary digits
    if T not in (0, 1) or clk not in (0, 1):
        raise ValueError("Inputs T and clk must be binary (0 or 1).")

    # On the rising edge of the clock (clk == 1), toggle the state if T = 1
    if clk == 1:
        if T == 1:
            Q_next = 1 - Q  # Toggle the output (Q = NOT Q)
        else:
            Q_next = Q  # Hold the current state (Q = Q)
    else:
        Q_next = Q  # If clock is 0, hold the current state

    Q_bar_next = 1 - Q_next  # Invert Q_next to get Q_bar

    return Q_next, Q_bar_next

# Example usage
try:
    T = int(input("Enter the toggle input T (0 or 1): "))
    clk = int(input("Enter the clock input clk (0 or 1): "))
    Q = int(input("Enter the current state Q (0 or 1): "))
    Q_bar = 1 - Q  # Invert Q to get Q_bar
    
    Q_next, Q_bar_next = t_flip_flop(T, clk, Q, Q_bar)
    print(f"Next state (Q): {Q_next}")
    print(f"Next state inverted (Q_bar): {Q_bar_next}")
except ValueError as e:
    print(e)

'''
Here's a line-by-line breakdown of the t_flip_flop function:

Function definition:
def t_flip_flop(T, clk, Q, Q_bar): defines the t_flip_flop function, which simulates the behavior of a T Flip-Flop. 
It takes four parameters: T (toggle input), clk (clock input), Q (current state), and Q_bar (inverted current state).

Docstring:
The docstring explains the purpose of the function: it simulates the behavior of a T Flip-Flop, 
which toggles its state when the clock is at the rising edge (clk == 1) and T == 1. 
If T == 0, the state remains unchanged. The function returns the next state (Q_next) and its inversion (Q_bar_next).

Input validation (binary check):
if T not in (0, 1) or clk not in (0, 1): checks whether T or clk are not binary values (either 0 or 1).
raise ValueError("Inputs T and clk must be binary (0 or 1).") raises an error if either T or clk is not binary.

State change on the rising edge of the clock:
if clk == 1: checks if the clock signal is at its rising edge (i.e., clk == 1).

If T == 1 (Toggle the state):
Q_next = 1 - Q toggles the output state. If Q was 0, Q_next becomes 1; if Q was 1, Q_next becomes 0.

If T == 0 (Hold the current state):
Q_next = Q keeps the current state unchanged when T == 0.

Hold the current state when the clock is not active:
else: handles the case when the clock is not at its rising edge (i.e., clk == 0).
Q_next = Q ensures the current state is maintained when the clock is not active.

Invert Q_next to get Q_bar_next:
Q_bar_next = 1 - Q_next calculates the inverted state by subtracting Q_next from 1. 
If Q_next is 0, Q_bar_next will be 1; if Q_next is 1, Q_bar_next will be 0.

Returning the next state and its inversion:
return Q_next, Q_bar_next returns the next state (Q_next) and its inversion (Q_bar_next).

Example usage with input prompts:
try: starts a block to handle user input and errors.
T = int(input("Enter the toggle input T (0 or 1): ")) prompts the user to input the toggle value T (either 0 or 1).
clk = int(input("Enter the clock input clk (0 or 1): ")) prompts the user to input the clock signal (clk).
Q = int(input("Enter the current state Q (0 or 1): ")) asks the user to input the current state (Q).
Q_bar = 1 - Q calculates the inverted state Q_bar by subtracting Q from 1.

Calling the t_flip_flop function:
Q_next, Q_bar_next = t_flip_flop(T, clk, Q, Q_bar) calls the t_flip_flop function with the user-provided inputs 
and stores the results in Q_next and Q_bar_next.

Displaying the next state:
print(f"Next state (Q): {Q_next}") prints the next state (Q_next).
print(f"Next state inverted (Q_bar): {Q_bar_next}") prints the inverted next state (Q_bar_next).

Error handling:
except ValueError as e: catches any ValueError exceptions (e.g., invalid input).
print(e) prints the error message if an exception occurs, providing feedback to the user on what went wrong.
'''