# Ask the user for a negative number
num = int(input("Enter a negative number: "))

# Ensure the number is negative
if num >= 0:
    print("The number is not negative. Please run the program again and enter a negative number.")
else:
    # Define the number of bits for the representation (e.g., 8 bits)
    num_bits = 8

    # Convert the magnitude of the number to binary and pad to num_bits
    magnitude = bin(abs(num))[2:].zfill(num_bits)

    # Create the 1's complement by inverting the bits
    ones_complement = ''.join('1' if bit == '0' else '0' for bit in magnitude)

    # Add 1 to the 1's complement to get the 2's complement
    twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(num_bits)

    # Print the result
    print(f"The 2's complement representation of {num} is: {twos_complement}")

'''
Python program that asks the user for a negative integer and then converts 
that number to its binary representation in the form of 2's compliment in a 8-bit system
'''
 
"""
Line-by-Line Breakdown:

num = int(input("Enter a negative number: "))
Prompts the user to enter a number. The input() function reads it as a string, and int() converts it to an integer, storing it in the variable num.

if num >= 0:
Checks if the entered number is non-negative.

print("The number is not negative. Please run the program again and enter a negative number.")
If the number is not negative, this message is printed, asking the user to enter a negative number and suggesting they run the program again.

else:
Indicates that the following block of code will execute if the number is negative.

num_bits = 8
Sets the number of bits to be used for the binary representation, which is 8 bits in this case.

magnitude = bin(abs(num))[2:].zfill(num_bits)
Converts the absolute value of the negative number to binary using bin(), removes the '0b' prefix with [2:], 
and pads the result with leading zeros to ensure it has a length of num_bits (8 bits).

ones_complement = ''.join('1' if bit == '0' else '0' for bit in magnitude)
Creates the 1's complement of the binary magnitude by inverting each bit: '0' becomes '1' and '1' becomes '0'. 
The join() method combines these inverted bits into a single string.

twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(num_bits)

int(ones_complement, 2) converts the 1's complement string to an integer using base 2 (binary).
+ 1 adds 1 to this integer, which is the step to obtain the 2's complement.
bin(...)[2:] converts the resulting integer back to a binary string and removes the '0b' prefix.
.zfill(num_bits) pads this binary string with leading zeros to ensure it is num_bits long (8 bits).

print(f"The 2's complement representation of {num} is: {twos_complement}")
Prints the 2's complement representation of the original negative number.
"""