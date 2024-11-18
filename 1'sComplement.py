def convert_to_ones_complement():
    try:
        # Input integer from user
        number = int(input("Enter an integer: ").strip())

        # For a 32-bit system, we represent numbers in a 32-bit format
        if number >= 0:
            # For positive numbers, just convert to binary and ensure it's 32 bits
            ones_complement = bin(number)[2:].zfill(32)
        else:
            # For negative numbers, first convert the absolute value to binary
            magnitude = bin(abs(number))[2:].zfill(32)
            # Invert the bits to get 1's complement
            ones_complement = ''.join('1' if bit == '0' else '0' for bit in magnitude)
        
        print(f"The 1's complement representation of {number} in 32-bit is: {ones_complement}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Call the function
convert_to_ones_complement()

'''
How It Works:
For Positive Numbers:
If the number is non-negative, it's directly converted to binary using bin(number)[2:] and then padded to 32 bits using zfill(32).
For Negative Numbers:
The absolute value of the number is first converted to binary.
Then, each bit of the binary number is flipped (1 becomes 0, and 0 becomes 1) to get the 1's complement.
Padding: We ensure that the final binary representation is exactly 32 bits using zfill(32) for both positive and negative numbers.
'''

'''
Line-by-Line Breakdown:

def convert_to_ones_complement():
Defines the function convert_to_ones_complement, which will convert an integer to its 1's complement binary representation.

try:
Starts a try block to handle potential errors during input or conversion.

number = int(input("Enter an integer: ").strip())
Prompts the user to input an integer, strips any leading or trailing spaces, and converts the input to an integer (number).

if number >= 0:
Checks if the number is positive or zero.

ones_complement = bin(number)[2:].zfill(32)
If the number is non-negative, converts it to binary (bin(number)) and slices off the '0b' prefix. 
The .zfill(32) ensures the binary number is padded to 32 bits.

else:
Executes if the number is negative.

magnitude = bin(abs(number))[2:].zfill(32)
Converts the absolute value of the number to binary (bin(abs(number))), slices off the '0b' prefix, and pads the binary number to 32 bits.

ones_complement = ''.join('1' if bit == '0' else '0' for bit in magnitude)
Inverts the bits of the magnitude (flips all 1s to 0s and vice versa) to obtain the 1's complement representation of the number.

print(f"The 1's complement representation of {number} in 32-bit is: {ones_complement}")
Displays the 1's complement representation of the number in a 32-bit format.

except ValueError:
Catches any ValueError exceptions (e.g., if the input is not a valid integer).

print("Invalid input! Please enter a valid integer.")
Displays an error message if the input is not a valid integer.

convert_to_ones_complement()
Calls the function to execute the 1's complement conversion process.
'''