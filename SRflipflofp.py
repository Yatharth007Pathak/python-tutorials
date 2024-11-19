'''
A flip-flop is a basic digital memory circuit used to store one bit of information. 
It has two states (0 and 1) and can hold its state indefinitely until changed. 
The most common types of flip-flops are the SR (Set-Reset) flip-flop, D (Data) flip-flop, T (Toggle) flip-flop, and JK (J-K) flip-flop.
'''

'''
An SR flip-flop (Set-Reset flip-flop) is a basic memory circuit with two inputs: Set (S) and Reset (R). 
It has two outputs: Q and Q_bar (inverted Q). The flip-flop works as follows:

S = 1, R = 0: Set the output Q to 1, and Q_bar to 0.
S = 0, R = 1: Reset the output Q to 0, and Q_bar to 1.
S = 0, R = 0: Hold the current state of the output.
S = 1, R = 1: This is an invalid condition because it would cause both Q and Q_bar to be 1, 
which is not allowed (they should always be complementary).

Truth Table for SR Flip-Flop
S     R       Q(next)       Q_bar(next)
0     0      No change      no change
0     1        Reset           Set
1     0         Set           Reset
1     1       Invalid        Invalid
'''

def sr_flip_flop(S, R, Q, Q_bar):
    """
    SR Flip-Flop: A flip-flop with Set and Reset inputs.
    
    :param S: Set input (0 or 1)
    :param R: Reset input (0 or 1)
    :param Q: Current state (output Q)
    :param Q_bar: Inverted output (Q_bar)
    :return: Tuple containing the next state (Q) and its inversion (Q_bar)
    """
    # Ensure inputs are valid binary digits
    if S not in (0, 1) or R not in (0, 1):
        raise ValueError("Inputs S and R must be binary (0 or 1).")
    
    # Invalid condition: S = 1 and R = 1
    if S == 1 and R == 1:
        raise ValueError("Invalid condition: Both S and R cannot be 1 at the same time.")

    # Set or Reset behavior
    if S == 1 and R == 0:
        Q_next = 1
        Q_bar_next = 0
    elif S == 0 and R == 1:
        Q_next = 0
        Q_bar_next = 1
    elif S == 0 and R == 0:
        Q_next = Q  # Hold the current state
        Q_bar_next = Q_bar
    else:
        Q_next = Q
        Q_bar_next = Q_bar

    return Q_next, Q_bar_next

# Example usage
try:
    S = int(input("Enter the Set input S (0 or 1): "))
    R = int(input("Enter the Reset input R (0 or 1): "))
    Q = int(input("Enter the current state Q (0 or 1): "))
    Q_bar = 1 - Q  # Invert Q to get Q_bar
    
    Q_next, Q_bar_next = sr_flip_flop(S, R, Q, Q_bar)
    print(f"Next state (Q): {Q_next}")
    print(f"Next state inverted (Q_bar): {Q_bar_next}")
except ValueError as e:
    print(e)

'''
Here's a line-by-line breakdown of the code:

Function definition:
def sr_flip_flop(S, R, Q, Q_bar): defines the function sr_flip_flop that simulates the behavior of an SR Flip-Flop, 
taking four parameters: S, R, Q, and Q_bar.

Docstring:
The docstring explains the purpose of the function: it describes the SR Flip-Flop and its parameters (S, R, Q, and Q_bar), 
which represent the Set, Reset, current state, and inverted output, respectively. 
It also specifies that the function will return the next state (Q_next) and its inversion (Q_bar_next).

Input validation (binary check):
if S not in (0, 1) or R not in (0, 1): checks if S or R are not binary values (either 0 or 1).
raise ValueError("Inputs S and R must be binary (0 or 1).") raises an error if the condition is true, 
indicating that S and R must be either 0 or 1.

Invalid condition check (S = 1 and R = 1):
if S == 1 and R == 1: checks for the invalid condition where both S and R are set to 1.
raise ValueError("Invalid condition: Both S and R cannot be 1 at the same time.") 
raises an error since both inputs being 1 at the same time is an invalid condition for an SR Flip-Flop.

Behavior for Set and Reset inputs:
if S == 1 and R == 0: defines the behavior when the Set input (S) is 1 and Reset (R) is 0, setting Q_next to 1 and Q_bar_next to 0.
elif S == 0 and R == 1: defines the behavior when S is 0 and R is 1, setting Q_next to 0 and Q_bar_next to 1.
elif S == 0 and R == 0: handles the case when both S and R are 0, meaning the current state is held (Q_next = Q, Q_bar_next = Q_bar).
The final else: handles any other case, maintaining the current state, which is essentially a safeguard.

Returning the next state and its inversion:
return Q_next, Q_bar_next returns the next state Q_next and its inversion Q_bar_next.

Example usage with input prompts:
try: starts a block to attempt user input and handle potential errors.
S = int(input("Enter the Set input S (0 or 1): ")) asks the user to enter the Set input S as an integer (0 or 1).
R = int(input("Enter the Reset input R (0 or 1): ")) asks the user to enter the Reset input R similarly.
Q = int(input("Enter the current state Q (0 or 1): ")) asks the user to enter the current state Q.
Q_bar = 1 - Q calculates the inverted state Q_bar by subtracting Q from 1.

Calling the sr_flip_flop function:
Q_next, Q_bar_next = sr_flip_flop(S, R, Q, Q_bar) calls the sr_flip_flop function with the provided inputs 
and stores the results in Q_next and Q_bar_next.

Displaying the next state:
print(f"Next state (Q): {Q_next}") prints the next state Q_next.
print(f"Next state inverted (Q_bar): {Q_bar_next}") prints the inverted next state Q_bar_next.

Error handling:
except ValueError as e: catches any ValueError exceptions (e.g., invalid inputs).
print(e) prints the error message if an exception occurs, allowing for user feedback on what went wrong.
'''