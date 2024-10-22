def convert_decimal_to_base(decimal_number, to_base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if decimal_number == 0:
        return "0"
    
    result = ""
    while decimal_number > 0:
        result = digits[decimal_number % to_base] + result
        decimal_number //= to_base
    
    return result

# Get user input
decimal_number = int(input("Enter the decimal number: "))
to_base = int(input("Enter the base to convert to (e.g., 2 for binary, 8 for octal, 16 for hexadecimal): "))

# Perform the conversion
converted_number = convert_decimal_to_base(decimal_number, to_base)

print(f"The decimal number {decimal_number} in base {to_base} is: {converted_number}")



# python code where we ask user for a number in decimal number system and convert the number to any base number system

"""
Explanation of the Code

def convert_decimal_to_base(decimal_number, to_base):
This line defines a function named convert_decimal_to_base which takes two parameters: decimal_number and to_base.

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
This line defines a string digits containing all possible digits for bases up to 36.
 This is used to map numerical values to their respective characters in different bases.

if decimal_number == 0:
    return "0"
This line checks if the decimal_number is 0 and returns "0" immediately since 0 in any base is still 0.

result = ""
while decimal_number > 0:
    result = digits[decimal_number % to_base] + result
    decimal_number //= to_base
This initializes an empty string result to build the final converted number.
The while loop runs as long as decimal_number is greater than 0.

Inside the loop:
decimal_number % to_base finds the remainder when decimal_number is divided by to_base. This remainder is the next digit in the target base.
digits[decimal_number % to_base] fetches the corresponding character for the remainder.
result = digits[decimal_number % to_base] + result prepends this character to the result string.
decimal_number //= to_base performs integer division on decimal_number by to_base, effectively shifting the digits to the right.

return result
This line returns the final converted number as a string.

# Get user input
decimal_number = int(input("Enter the decimal number: "))
to_base = int(input("Enter the base to convert to (e.g., 2 for binary, 8 for octal, 16 for hexadecimal): "))
These lines prompt the user to enter a decimal number (decimal_number) and the target base (to_base), both converted to integers using int().

# Perform the conversion
converted_number = convert_decimal_to_base(decimal_number, to_base)
This line calls the convert_decimal_to_base function with the user-provided decimal_number and to_base, storing the result in converted_number.

print(f"The decimal number {decimal_number} in base {to_base} is: {converted_number}")
This line prints the result of the conversion, showing the original decimal number, the target base, and the converted number. 
The f before the string denotes an f-string, which allows for the inclusion of variables directly within the string.
"""