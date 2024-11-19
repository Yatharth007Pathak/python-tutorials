def bcd_adder(A, B):
    # Convert BCD inputs to integers
    decimal_A = int(A, 2)
    decimal_B = int(B, 2)

    # Perform decimal addition
    decimal_sum = decimal_A + decimal_B

    # Check for BCD overflow
    if decimal_sum > 9:
        decimal_sum += 6  # Add binary 6 to correct overflow

    # Convert the corrected sum back to BCD
    bcd_result = bin(decimal_sum)[2:].zfill(4)  # Ensure 4 bits for BCD
    return bcd_result

# Example usage
A = input("Enter the first BCD digit (4-bit binary): ")
B = input("Enter the second BCD digit (4-bit binary): ")

# Validate input
if len(A) == 4 and len(B) == 4 and all(bit in '01' for bit in A) and all(bit in '01' for bit in B):
    result = bcd_adder(A, B)
    print(f"The BCD sum of {A} and {B} is: {result}")
else:
    print("Invalid input! Please enter two valid 4-bit binary numbers.")

'''
A BCD (Binary-Coded Decimal) adder in digital electronics adds two BCD numbers. 
A BCD number represents a decimal digit (0-9) in 4-bit binary form. 
When the result exceeds 9 (binary 1001), it requires a correction by adding 6 (binary 0110) to adjust the result to a valid BCD representation.
'''

'''
Here is a line-by-line breakdown of the Python code for a BCD (Binary-Coded Decimal) adder:

def bcd_adder(A, B):
Defines a function named bcd_adder that takes two arguments: A and B, representing two 4-bit binary inputs in BCD format.

decimal_A = int(A, 2)
Converts the binary string A to its decimal equivalent using the int() function with base 2, and stores it in decimal_A.

decimal_B = int(B, 2)
Converts the binary string B to its decimal equivalent using the int() function with base 2, and stores it in decimal_B.

decimal_sum = decimal_A + decimal_B
Adds the two decimal values (decimal_A and decimal_B) to get the sum in decimal format, and stores it in decimal_sum.

if decimal_sum > 9:
Checks if the decimal sum exceeds 9, which would cause an overflow in BCD (as BCD can only represent values from 0 to 9). 
If the sum exceeds 9, this condition will be true.

decimal_sum += 6
If there is a BCD overflow (sum > 9), adds 6 (binary 0110) to the sum to correct the BCD overflow. 
This step ensures the sum stays within the valid BCD range.

bcd_result = bin(decimal_sum)[2:].zfill(4)
Converts the decimal sum back to binary using the bin() function. The [2:] slices off the '0b' prefix that bin() adds. 
Then, zfill(4) ensures that the binary result is exactly 4 bits long (adding leading zeros if necessary).

return bcd_result
Returns the final BCD result as a 4-bit binary string.

A = input("Enter the first BCD digit (4-bit binary): ")
Prompts the user to enter the first BCD digit as a 4-bit binary number and stores it in variable A.

B = input("Enter the second BCD digit (4-bit binary): ")
Prompts the user to enter the second BCD digit as a 4-bit binary number and stores it in variable B.

if len(A) == 4 and len(B) == 4 and all(bit in '01' for bit in A) and all(bit in '01' for bit in B):
Validates the input by checking if both A and B are 4 bits long and contain only '0' or '1' characters. 
If the conditions are met, the code inside the if block will execute.

result = bcd_adder(A, B)
Calls the bcd_adder function with A and B as arguments and stores the result in the result variable.

print(f"The BCD sum of {A} and {B} is: {result}")
Prints the result of the BCD addition in the format: "The BCD sum of A and B is: result".

else:
If the input does not meet the required conditions (not 4 bits or contains invalid characters), the else block will execute.

print("Invalid input! Please enter two valid 4-bit binary numbers.")
Prints a message informing the user that the input was invalid and that they should enter valid 4-bit binary numbers.
'''