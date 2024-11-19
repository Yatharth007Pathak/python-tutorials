def half_subtractor(A, B):
    # XOR operation for Difference
    Difference = A ^ B
    # NOT A AND B for Borrow
    Borrow = (~A & 1) & B
    return Difference, Borrow

# Example usage
A = int(input("Enter first binary digit (0 or 1): "))
B = int(input("Enter second binary digit (0 or 1): "))

if A in (0, 1) and B in (0, 1):
    Difference, Borrow = half_subtractor(A, B)
    print(f"Half Subtractor Results: Difference = {Difference}, Borrow = {Borrow}")
else:
    print("Invalid input! Please enter binary digits only (0 or 1).")

# A half subtractor subtracts two binary digits and provides two outputs: Difference and Borrow

'''
Here is a line-by-line breakdown of the Python code for a half subtractor:

def half_subtractor(A, B):
Defines a function named half_subtractor that takes two arguments: A and B, which represent the two binary digits to be subtracted.

Difference = A ^ B
Performs the XOR operation between A and B. The XOR operation produces the difference bit of the subtraction, 
where the result is 1 if the inputs are different, and 0 if they are the same.

Borrow = (~A & 1) & B
Calculates the borrow bit. In binary subtraction, a borrow occurs when A is smaller than B. 
The expression (~A & 1) computes the bitwise NOT of A (flipping all bits) and then masks it with 1 to ensure it is treated as a binary digit. 
The result is then ANDed with B, giving the borrow bit.

return Difference, Borrow
Returns the Difference and Borrow bits as the result of the half subtractor.

A = int(input("Enter first binary digit (0 or 1): "))
Prompts the user to input the first binary digit, converts it to an integer, and stores it in variable A.

B = int(input("Enter second binary digit (0 or 1): "))
Prompts the user to input the second binary digit, converts it to an integer, and stores it in variable B.

if A in (0, 1) and B in (0, 1):
Checks if both A and B are valid binary digits (either 0 or 1). If both are valid, the code inside the if block will be executed.

Difference, Borrow = half_subtractor(A, B)
Calls the half_subtractor function with A and B as arguments, and stores the returned values (the difference and borrow) 
in variables Difference and Borrow.

print(f"Half Subtractor Results: Difference = {Difference}, Borrow = {Borrow}")
Prints the results of the half subtractor, displaying the Difference and Borrow values.

else:
If either A or B is not a valid binary digit, the else block will execute.

print("Invalid input! Please enter binary digits only (0 or 1).")
Prints a message informing the user that the input was invalid and they should enter binary digits (0 or 1) only.
'''