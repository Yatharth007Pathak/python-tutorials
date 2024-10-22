def convert_from_decimal(number, base):
    # Convert the integer part to the new base
    integer_part = int(number)
    integer_result = ''

    if integer_part == 0:
        integer_result = '0'
    else:
        while integer_part > 0:
            remainder = integer_part % base
            if remainder >= 10:
                # For bases greater than 10, use letters for values above 9
                integer_result = chr(55 + remainder) + integer_result
            else:
                integer_result = str(remainder) + integer_result
            integer_part = integer_part // base

    # Convert the fractional part to the new base
    fractional_part = number - int(number)
    fractional_result = ''
    if fractional_part > 0:
        fractional_result += '.'
        count = 0  # Limiting the number of digits in the fractional part to prevent infinite loop
        while fractional_part > 0 and count < 10:  # You can adjust the precision by changing the limit
            fractional_part *= base
            digit = int(fractional_part)
            if digit >= 10:
                fractional_result += chr(55 + digit)
            else:
                fractional_result += str(digit)
            fractional_part -= digit
            count += 1

    return integer_result + fractional_result

# Ask the user for input
number = float(input("Enter a real number in decimal system: "))
base = int(input("Enter the base to convert to: "))

# Convert from decimal to the specified base
converted_number = convert_from_decimal(number, base)

# Print the result
print(f"The number {number} in base {base} is {converted_number}")

# Python program that converts a real number in decimal system to any other base specified by the user

"""
here is a detailed breakdown of each line of the provided Python code:

def convert_from_decimal(number, base):
Function Definition: Defines a function named convert_from_decimal that takes two arguments: 
number (a float representing the real number in decimal system) and base (an integer representing the target base).

integer_part = int(number)
integer_result = ''
Initialize Integer Part: Converts the number to an integer, storing it in integer_part. 
Initializes an empty string integer_result to store the converted integer part.

if integer_part == 0:
    integer_result = '0'
else:
    while integer_part > 0:
        remainder = integer_part % base
        if remainder >= 10:
            integer_result = chr(55 + remainder) + integer_result
        else:
           integer_result = str(remainder) + integer_result
        integer_part = integer_part // base
Convert Integer Part:
If integer_part is 0, set integer_result to '0'.
Otherwise, use a while loop to convert integer_part to the target base:
Calculate the remainder of integer_part divided by base.
If the remainder is 10 or greater, convert it to a letter (A, B, C, etc.) using chr(55 + remainder).
Otherwise, convert the remainder to a string and prepend it to integer_result.
Update integer_part by performing floor division with base.

fractional_part = number - int(number)
fractional_result = ''
Initialize Fractional Part: Calculate the fractional part of number by subtracting the integer part from number, 
and store it in fractional_part. Initialize an empty string fractional_result to store the converted fractional part.

if fractional_part > 0:
    fractional_result += '.'
    count = 0
    while fractional_part > 0 and count < 10:
        fractional_part *= base
        digit = int(fractional_part)
        if digit >= 10:
            fractional_result += chr(55 + digit)
        else:
            fractional_result += str(digit)
        fractional_part -= digit
        count += 1
Convert Fractional Part:
If fractional_part is greater than 0, append a decimal point to fractional_result.
Use a while loop to convert fractional_part to the target base, with a limit of 10 iterations to prevent infinite loops:
Multiply fractional_part by base.
Extract the integer part of fractional_part and store it in digit.
If digit is 10 or greater, convert it to a letter (A, B, C, etc.) using chr(55 + digit).
Otherwise, convert digit to a string and append it to fractional_result.
Subtract digit from fractional_part to update fractional_part.
Increment count by 1 to keep track of the number of digits.

return integer_result + fractional_result
Return Result: Concatenate integer_result and fractional_result and return the final converted number as a string.

number = float(input("Enter a real number in decimal system: "))
base = int(input("Enter the base to convert to: "))
User Input: Prompt the user to enter a real number in the decimal system, convert the input to a float, and store it in number. 
Prompt the user to enter the target base, convert the input to an integer, and store it in base.

converted_number = convert_from_decimal(number, base)
Function Call: Call the convert_from_decimal function with number and base as arguments, and store the result in converted_number.

print(f"The number {number} in base {base} is {converted_number}")
Output: Print the converted number in the specified base.
This program converts a decimal number to any user-specified base, handling both the integer and fractional parts separately. 
The use of chr(55 + digit) allows for the representation of digits greater than 9 in bases higher than 10.
"""