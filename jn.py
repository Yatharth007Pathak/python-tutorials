# Ask the user for a negative number
num = int(input("Enter a negative number: "))

# Ensure the number is negative
if num >= 0:
    print("The number is not negative. Please run the program again and enter a negative number.")
else:
    # Convert the magnitude of the number to binary
    magnitude = bin(abs(num))[2:]
    
    # Determine the number of bits required to represent the magnitude
    num_bits = len(magnitude)
    
    # Create the sign and magnitude representation
    sign_and_magnitude = '1' + magnitude.zfill(num_bits)
    
    # Print the result
    print(f"The sign and magnitude representation of {num} is: {sign_and_magnitude}")


'''
Python program that asks the user for a negative integer and then 
converts that number to its binary representation in the form of sign and magnitude
'''


"""
Line-by-Line Breakdown:

num = int(input("Enter a negative number: "))
This line prompts the user to enter a number. The input function takes the input as a string, 
and int converts it into an integer, storing it in the variable num.

if num >= 0:
This line checks if the entered number is non-negative (i.e., zero or positive).

print("The number is not negative. Please run the program again and enter a negative number.")
If the condition in the previous line is true (the number is non-negative), this line prints a message 
informing the user that the number is not negative and advises to run the program again with a negative number.

else:
This line starts an else block that will execute if the number is negative (i.e., the condition num >= 0 is false).

magnitude = bin(abs(num))[2:]
This line converts the magnitude (absolute value) of the negative number to its binary representation.
abs(num): Computes the absolute value of num, turning it into a positive number.
bin(...): Converts this positive number to a binary string prefixed with '0b'.
[2:]: Slices off the '0b' prefix, leaving just the binary digits.

num_bits = len(magnitude)
This calculates the number of bits required to represent the magnitude of the number in binary, by finding the length of the magnitude string.

sign_and_magnitude = '1' + magnitude.zfill(num_bits)
This line creates the sign and magnitude representation of the negative number by concatenating '1'. 
(indicating a negative sign) with the binary magnitude calculated in the previous step.
magnitude.zfill(num_bits) ensures that the magnitude part has leading zeros to match the total bit length (the length of the magnitude).

print(f"The sign and magnitude representation of {num} is: {sign_and_magnitude}")
This line prints the final result, showing the sign and magnitude representation of the original negative number.
The {num} and {sign_and_magnitude} are placeholders that will be replaced with the values of num and sign_and_magnitude, respectively.
"""