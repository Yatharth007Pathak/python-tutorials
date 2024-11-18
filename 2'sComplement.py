def convert_to_twos_complement():
    try:
        # Input integer from user
        number = int(input("Enter an integer: ").strip())

        # For a 32-bit system, represent numbers in a 32-bit format
        if number >= 0:
            # For positive numbers or zero, just convert to binary and ensure it's 32 bits
            twos_complement = bin(number)[2:].zfill(32)
        else:
            # For negative numbers, first convert the absolute value to binary
            magnitude = bin(abs(number))[2:].zfill(32)
            # Invert the bits to get 1's complement
            ones_complement = ''.join('1' if bit == '0' else '0' for bit in magnitude)
            # Add 1 to get 2's complement
            twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(32)

        print(f"The 2's complement representation of {number} in 32-bit is: {twos_complement}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Call the function
convert_to_twos_complement()

'''
How It Works:
For Positive Numbers or Zero:
The binary representation of the number is obtained using bin(number)[2:], which removes the "0b" prefix.
The result is padded to 32 bits using zfill(32).
For Negative Numbers:
The absolute value of the number is first converted to binary.
The 1's complement is obtained by inverting each bit.
The 2's complement is obtained by adding 1 to the 1's complement.
Padding: The final binary representation is padded to ensure it is exactly 32 bits.
'''

'''
Line-by-Line Breakdown:

def convert_to_twos_complement():
Defines the function convert_to_twos_complement, which will convert an integer to its 2's complement binary representation.

try:
Starts a try block to handle potential errors during input or conversion.

number = int(input("Enter an integer: ").strip())
Prompts the user to input an integer, strips any leading or trailing spaces, and converts the input to an integer (number).

if number >= 0:
Checks if the number is positive or zero.

twos_complement = bin(number)[2:].zfill(32)
If the number is non-negative, converts it to binary (bin(number)), slices off the '0b' prefix, 
and pads the binary number to 32 bits using .zfill(32).

else:
Executes if the number is negative.

magnitude = bin(abs(number))[2:].zfill(32)
Converts the absolute value of the number to binary (bin(abs(number))), slices off the '0b' prefix, and pads the binary number to 32 bits.

ones_complement = ''.join('1' if bit == '0' else '0' for bit in magnitude)
Inverts the bits of the magnitude (flips all 1s to 0s and vice versa) to obtain the 1's complement representation.

twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(32)
Converts the 1's complement to an integer, adds 1 to it to get the 2's complement, and converts the result back to binary. 
The .zfill(32) ensures it is padded to 32 bits.

print(f"The 2's complement representation of {number} in 32-bit is: {twos_complement}")
Displays the 2's complement representation of the number in 32-bit format.

except ValueError:
Catches any ValueError exceptions (e.g., if the input is not a valid integer).

print("Invalid input! Please enter a valid integer.")
Displays an error message if the input is not a valid integer.

convert_to_twos_complement()
Calls the function to execute the 2's complement conversion process.
'''