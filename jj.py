def convert_to_decimal(number_str, base):
    # Split the number into the integer and fractional parts
    if '.' in number_str:
        integer_part, fractional_part = number_str.split('.')
    else:
        integer_part = number_str
        fractional_part = ''

    # Convert the integer part to decimal
    integer_decimal = 0
    power = 0
    for digit in integer_part[::-1]:
        integer_decimal += int(digit, base) * (base ** power)
        power += 1

    # Convert the fractional part to decimal
    fractional_decimal = 0
    power = -1
    for digit in fractional_part:
        fractional_decimal += int(digit, base) * (base ** power)
        power -= 1

    # Combine the integer and fractional parts
    decimal_number = integer_decimal + fractional_decimal

    return decimal_number

# Ask the user for input
number_str = input("Enter a real number: ")
base = int(input("Enter its base: "))

# Convert to decimal
decimal_number = convert_to_decimal(number_str, base)

# Print the result
print(f"The decimal equivalent of {number_str} in base {base} is {decimal_number}")

# Python program that asks the user for a real number in a given base and converts it to a decimal number

"""
here's a detailed breakdown of each line of the provided Python code:

def convert_to_decimal(number_str, base):
Function Definition: Defines a function named convert_to_decimal that takes two arguments: 
number_str (a string representing the real number in a given base) and base (an integer representing the base of the number).

if '.' in number_str:
    integer_part, fractional_part = number_str.split('.')
else:
    integer_part = number_str
    fractional_part = ''
Splitting the Number: Checks if the input string number_str contains a decimal point.
If it does, the string is split into two parts: integer_part (the part before the decimal point) and
fractional_part (the part after the decimal point).
If it does not contain a decimal point, the entire string is treated as the integer part, and fractional_part is set to an empty string.

integer_decimal = 0
power = 0
for digit in integer_part[::-1]:
    integer_decimal += int(digit, base) * (base ** power)
    power += 1
Integer Part Conversion: Converts the integer part from the given base to decimal.
Initializes integer_decimal to 0 and power to 0.
Iterates through each digit in integer_part from right to left ([::-1] reverses the string).
Converts each digit from the given base to decimal (int(digit, base)) and 
adds its value multiplied by the base raised to the current power to integer_decimal.
Increments the power for each digit.

fractional_decimal = 0
power = -1
for digit in fractional_part:
    fractional_decimal += int(digit, base) * (base ** power)
    power -= 1
Fractional Part Conversion: Converts the fractional part from the given base to decimal.
Initializes fractional_decimal to 0 and power to -1.
Iterates through each digit in fractional_part.
Converts each digit from the given base to decimal (int(digit, base)) and adds 
its value multiplied by the base raised to the current power to fractional_decimal.
Decrements the power for each digit.

decimal_number = integer_decimal + fractional_decimal
Combining the Parts: Adds integer_decimal and fractional_decimal to get the final decimal number.

return decimal_number
Return Statement: Returns the decimal equivalent of the input number.

number_str = input("Enter a real number: ")
base = int(input("Enter its base: "))
User Input: Prompts the user to enter a real number (number_str) and its base (base). Converts the base input to an integer.

decimal_number = convert_to_decimal(number_str, base)
Function Call: Calls the convert_to_decimal function with the user-provided number_str and base and stores the result in decimal_number.

print(f"The decimal equivalent of {number_str} in base {base} is {decimal_number}")
Output: Prints the decimal equivalent of the input number in the specified base.
The program uses string manipulation and arithmetic operations to convert a number from any given base to a decimal number, 
handling both integer and fractional parts separately.
"""