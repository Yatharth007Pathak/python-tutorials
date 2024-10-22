def convert_to_decimal(number_str, base):
    # Split the number into integer and fractional parts
    if '.' in number_str:
        integer_part, fractional_part = number_str.split('.')
    else:
        integer_part = number_str
        fractional_part = ''

    # Convert the integer part
    decimal_integer = int(integer_part, base)

    # Convert the fractional part
    decimal_fraction = 0
    for i, digit in enumerate(fractional_part):
        decimal_fraction += int(digit, base) / (base ** (i + 1))

    # Combine both parts
    decimal_number = decimal_integer + decimal_fraction
    return decimal_number

# Get user input
number_str = input("Enter a real number: ")
base = int(input("Enter the base of the number: "))

# Convert and display the result
decimal_number = convert_to_decimal(number_str, base)
print(f"The decimal equivalent of {number_str} in base {base} is {decimal_number}")

# easiest python program that asks the user for a real number in a given base and converts it to a decimal number

"""
Let's break down each line of the Python code provided:

Function Definition: 
def convert_to_decimal(number_str, base):
Defines a function named convert_to_decimal that takes two arguments: 
number_str (the number in string format) and base (the base of the number system).

Checking for Fractional Part: 
if '.' in number_str:
Checks if the number string contains a decimal point (indicating a fractional part).

Splitting the Number: 
integer_part, fractional_part = number_str.split('.')
If a decimal point is present, splits the string into two parts: 
integer_part (the part before the decimal point) and fractional_part (the part after the decimal point).

Handling Whole Numbers:
else: integer_part = number_str; fractional_part = ''
If there's no decimal point, assigns the entire number_str to integer_part and sets fractional_part to an empty string.

Convert Integer Part: 
decimal_integer = int(integer_part, base)
Converts the integer_part from the given base to a decimal integer using Python’s int function. 
The second argument to int specifies the base of the number system.

Initialize Fractional Part: 
decimal_fraction = 0
Initializes a variable decimal_fraction to accumulate the converted fractional part.

Iterate Over Fractional Digits: 
for i, digit in enumerate(fractional_part)
Loops through each digit in the fractional_part, using enumerate to get both the index i and the digit.

Convert and Add Fractional Digits: 
decimal_fraction += int(digit, base) / (base ** (i + 1))
Converts each digit from the specified base to a decimal integer and divides it by base ** (i + 1) to place it correctly in the fractional part. 
Adds the result to decimal_fraction.

Combine Integer and Fractional Parts: 
decimal_number = decimal_integer + decimal_fraction
Adds the converted integer part and fractional part to get the total decimal number.

Return Decimal Number: 
return decimal_number
Returns the decimal representation of the input number.

User Input for Number: 
number_str = input("Enter a real number: ")
Prompts the user to enter a real number and stores it as a string in number_str.
User Input for Base: 
base = int(input("Enter the base of the number: "))
Prompts the user to enter the base of the number system and converts the input to an integer.

Conversion Call: 
decimal_number = convert_to_decimal(number_str, base)
Calls the convert_to_decimal function with the user-provided number and base, and stores the result in decimal_number.

Display Result: 
print(f"The decimal equivalent of {number_str} in base {base} is {decimal_number}")
Prints the decimal equivalent of the input number in the specified base.
"""