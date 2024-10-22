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
    
    # Print the result
    print(f"The 1's complement representation of {num} is: {ones_complement}")


'''
Python program that asks the user for a negative integer and then converts 
that number to its binary representation in the form of 1's compliment in a 8-bit system
'''

"""
Line-by-Line Breakdown:

num = int(input("Enter a negative number: "))
Prompts the user to enter a number and converts the input to an integer, storing it in num.

if num >= 0:
Checks if the entered number is non-negative.

print("The number is not negative. Please run the program again and enter a negative number.")
If the number is not negative, this message is displayed, asking the user to enter a negative number and to run the program again.

else:
Indicates that the following block will execute if the number is negative.

num_bits = 8
Defines the number of bits used for the representation. Here, it's set to 8 bits.

magnitude = bin(abs(num))[2:].zfill(num_bits)
in(abs(num))[2:] converts the absolute value of the number to a binary string and strips off the '0b' prefix.
.zfill(num_bits) pads the resulting binary string with leading zeros to ensure it has a length of num_bits (8 in this case).

ones_complement = ''.join('1' if bit == '0' else '0' for bit in magnitude)
This line creates the 1's complement representation by inverting each bit in the binary magnitude. 
For each bit in magnitude, it places a '1' if the bit is '0', and a '0' if the bit is '1'. 
The join() method combines these bits into a single string.

print(f"The 1's complement representation of {num} is: {ones_complement}")
Prints the 1's complement representation of the original negative number.
"""