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
number_str = input("Enter a real number: ")
initial_base = int(input("Enter its base: "))
target_base = int(input("Enter the base to convert to: "))

# Convert to decimal first
decimal_number = convert_to_decimal(number_str, initial_base)

# Convert from decimal to the target base
converted_number = convert_from_decimal(decimal_number, target_base)

# Print the result
print(f"The number {number_str} in base {initial_base} is {converted_number} in base {target_base}")

# Python program that asks the user for a real number and its base, then converts it to another user-defined base.

"""
here's a detailed breakdown of each line of the provided Python code in plain text:

def convert_to_decimal(number_str, base):
Defines a function named convert_to_decimal that takes two parameters: 
number_str (a string representing the number in the given base) and base (an integer representing the base of the input number).

if '.' in number_str:
    integer_part, fractional_part = number_str.split('.')
else:
    integer_part = number_str
    fractional_part = ''
Checks if number_str contains a decimal point.
If it does, splits number_str into integer_part (before the decimal point) and fractional_part (after the decimal point).
If it does not, assigns number_str to integer_part and sets fractional_part to an empty string.

integer_decimal = 0
power = 0
for digit in integer_part[::-1]:
    integer_decimal += int(digit, base) * (base ** power)
    power += 1
Initializes integer_decimal to 0 and power to 0.
Iterates through each digit in integer_part from right to left (using [::-1] to reverse the string).
Converts each digit from the given base to decimal and adds its value multiplied by base raised to the current power to integer_decimal.
Increments power by 1 for each digit.

fractional_decimal = 0
power = -1
for digit in fractional_part:
    fractional_decimal += int(digit, base) * (base ** power)
    power -= 1
Initializes fractional_decimal to 0 and power to -1.
Iterates through each digit in fractional_part.
Converts each digit from the given base to decimal and adds its value multiplied by base raised to the current power to fractional_decimal.
Decrements power by 1 for each digit.

decimal_number = integer_decimal + fractional_decimal
Combines integer_decimal and fractional_decimal to get the final decimal number.

return decimal_number
Returns the decimal number.

def convert_from_decimal(number, base):
Defines a function named convert_from_decimal that takes two parameters: 
number (a float representing the decimal number) and base (an integer representing the target base).

integer_part = int(number)
integer_result = ''
Converts number to an integer and assigns it to integer_part.
Initializes integer_result to an empty string to store the converted integer part.

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
Checks if integer_part is 0.
If it is, sets integer_result to '0'.
Otherwise, uses a while loop to convert integer_part to the target base:
Calculates the remainder when integer_part is divided by base.
If the remainder is 10 or greater, converts it to a letter (A, B, C, etc.) using chr(55 + remainder) and prepends it to integer_result.
Otherwise, converts the remainder to a string and prepends it to integer_result.
Updates integer_part by performing floor division with base.

fractional_part = number - int(number)
fractional_result = ''
Calculates the fractional part of number by subtracting the integer part from number and assigns it to fractional_part.
Initializes fractional_result to an empty string to store the converted fractional part.

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
Checks if fractional_part is greater than 0.
If it is, appends a decimal point to fractional_result.
Uses a while loop to convert fractional_part to the target base, with a limit of 10 iterations to prevent infinite loops:
Multiplies fractional_part by base.
Extracts the integer part of fractional_part and assigns it to digit.
If digit is 10 or greater, converts it to a letter (A, B, C, etc.) using chr(55 + digit) and appends it to fractional_result.
Otherwise, converts digit to a string and appends it to fractional_result.
Subtracts digit from fractional_part.
Increments count by 1 for each iteration.

return integer_result + fractional_result
Combines integer_result and fractional_result and returns the final converted number as a string.

number_str = input("Enter a real number: ")
initial_base = int(input("Enter its base: "))
target_base = int(input("Enter the base to convert to: "))
Prompts the user to enter a real number, stores it as a string in number_str.
Prompts the user to enter the base of the input number, converts it to an integer, and stores it in initial_base.
Prompts the user to enter the target base for conversion, converts it to an integer, and stores it in target_base.

decimal_number = convert_to_decimal(number_str, initial_base)
Calls convert_to_decimal with number_str and initial_base as arguments, and stores the returned decimal number in decimal_number.

converted_number = convert_from_decimal(decimal_number, target_base)
Calls convert_from_decimal with decimal_number and target_base as arguments, and stores the converted number in converted_number.

print(f"The number {number_str} in base {initial_base} is {converted_number} in base {target_base}")
Prints the converted number in the target base, displaying the original number and its base, along with the converted number and its base.
"""