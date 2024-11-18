def convert_to_sign_magnitude():
    try:
        # Input integer from user
        number = int(input("Enter an integer: ").strip())

        # Determine the sign bit and the magnitude
        if number < 0:
            sign_bit = '1'
            magnitude = bin(abs(number))[2:]  # Get binary representation of the absolute value
        else:
            sign_bit = '0'
            magnitude = bin(number)[2:]  # Get binary representation of the number

        # Combine the sign bit and magnitude
        sign_magnitude_rep = sign_bit + magnitude
        print(f"The sign and magnitude representation of {number} is: {sign_magnitude_rep}")
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Call the function
convert_to_sign_magnitude()

'''
How It Works:
Sign Bit:
If the number is positive or zero, the sign bit is 0.
If the number is negative, the sign bit is 1.
Magnitude:
The magnitude is the binary representation of the absolute value of the number.
We use bin(abs(number)) to get the binary string of the absolute value and strip the "0b" prefix.
Final Representation: The final output is the sign bit concatenated with the binary magnitude.
'''

'''
Line-by-Line Breakdown:

def convert_to_sign_magnitude():
Defines the function convert_to_sign_magnitude, which will convert an integer to its sign-magnitude binary representation.

try:
Starts a try block to handle potential errors during input or conversion.

number = int(input("Enter an integer: ").strip())
Prompts the user to input an integer, strips any leading or trailing spaces, and converts the input to an integer (number).

if number < 0:
Checks if the number is negative.

sign_bit = '1'
If the number is negative, sets the sign bit to '1'.

magnitude = bin(abs(number))[2:]
If the number is negative, it calculates the magnitude by taking the absolute value of the number, 
converting it to binary (bin(abs(number))), and slicing off the '0b' prefix using [2:].

else:
Executes if the number is positive or zero.

sign_bit = '0'
Sets the sign bit to '0' for non-negative numbers.

magnitude = bin(number)[2:]
Converts the non-negative number to binary (bin(number)) and slices off the '0b' prefix.

sign_magnitude_rep = sign_bit + magnitude
Combines the sign bit ('0' or '1') with the binary representation of the magnitude to form the sign-magnitude representation.

print(f"The sign and magnitude representation of {number} is: {sign_magnitude_rep}")
Displays the sign-magnitude representation of the input number.

except ValueError:
Catches any ValueError exceptions (e.g., if the input is not a valid integer).

print("Invalid input! Please enter a valid integer.")
Displays an error message if the input is not a valid integer.

convert_to_sign_magnitude()
Calls the function to execute the sign-magnitude conversion process.
'''