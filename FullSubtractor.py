def full_subtractor(A, B, Bin):
    # XOR operation for Difference
    Difference = A ^ B ^ Bin
    # Borrow logic: (NOT A AND B) OR (NOT A AND Bin) OR (B AND Bin)
    Borrow = ((~A & 1) & B) | ((~A & 1) & Bin) | (B & Bin)
    return Difference, Borrow

# Example usage
A = int(input("Enter first binary digit (0 or 1): "))
B = int(input("Enter second binary digit (0 or 1): "))
Bin = int(input("Enter borrow input (0 or 1): "))

if A in (0, 1) and B in (0, 1) and Bin in (0, 1):
    Difference, Borrow = full_subtractor(A, B, Bin)
    print(f"Full Subtractor Results: Difference = {Difference}, Borrow = {Borrow}")
else:
    print("Invalid input! Please enter binary digits only (0 or 1).")

# A full subtractor subtracts 3 binary digits: 2 inputs and 1 borrow from a previous subtraction. It provides two outputs: Difference and Borrow

'''
Here is a line-by-line breakdown of the Python code for a full subtractor:

def full_subtractor(A, B, Bin):
Defines a function named full_subtractor that takes three arguments: A, B, and Bin. 
These represent the two binary digits to be subtracted and the borrow input from a previous subtraction, respectively.

Difference = A ^ B ^ Bin
Performs the XOR operation between A, B, and Bin. The XOR operation computes the difference bit. 
The result will be 1 if an odd number of inputs are 1, and 0 if an even number of inputs are 1.

Borrow = ((~A & 1) & B) | ((~A & 1) & Bin) | (B & Bin)
Calculates the borrow bit. The borrow occurs when:
A is smaller than B (i.e., ~A & 1 AND B),
A is smaller than Bin (i.e., ~A & 1 AND Bin), or
Both B and Bin are 1 (i.e., B & Bin).
This logic ensures that the borrow bit is 1 if any of these conditions are met.

return Difference, Borrow
Returns the Difference and Borrow values, which represent the result of the full subtraction operation.

A = int(input("Enter first binary digit (0 or 1): "))
Prompts the user to input the first binary digit, converts it to an integer, and stores it in variable A.

B = int(input("Enter second binary digit (0 or 1): "))
Prompts the user to input the second binary digit, converts it to an integer, and stores it in variable B.

Bin = int(input("Enter borrow input (0 or 1): "))
Prompts the user to input the borrow input (Bin), converts it to an integer, and stores it in variable Bin.

if A in (0, 1) and B in (0, 1) and Bin in (0, 1):
Checks if A, B, and Bin are all valid binary digits (either 0 or 1). If all inputs are valid, the code inside the if block will be executed.

Difference, Borrow = full_subtractor(A, B, Bin)
Calls the full_subtractor function with A, B, and Bin as arguments, 
and stores the returned values (the difference and borrow) in variables Difference and Borrow.

print(f"Full Subtractor Results: Difference = {Difference}, Borrow = {Borrow}")
Prints the results of the full subtractor, displaying the Difference and Borrow values.

else:
If any of the inputs (A, B, or Bin) are not valid binary digits, the else block will execute.

print("Invalid input! Please enter binary digits only (0 or 1).")
Prints a message informing the user that the input was invalid and they should enter binary digits (0 or 1) only.
'''