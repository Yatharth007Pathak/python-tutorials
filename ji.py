def to_decimal(num_str, base):
    return int(num_str, base)

def from_decimal(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    if num == 0:
        return '0'
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result

num_str = input("Enter the number: ")
base_from = int(input("Enter the base of the number: "))
base_to = int(input("Enter the base to convert to: "))

decimal_num = to_decimal(num_str, base_from)
converted_num = from_decimal(decimal_num, base_to)

print("Converted number:", converted_num)

# easiest python code that takes a number and its base as input, and then converts it to another user-defined base

"""
Breakdown of entire code:

Functions:
to_decimal(num_str, base): Converts a number from a given base to decimal (base 10).
int(num_str, base): Converts the string num_str from the specified base to a decimal integer.
from_decimal(num, base): Converts a decimal number to the desired base.
digits: A string containing all possible characters for bases up to 36.
result: Initializes an empty string to build the converted number.
if num == 0: return '0': Directly returns '0' if the number is 0.
while num > 0:: Loops until num is 0, building the result string by appending the appropriate character from digits.
num //= base: Updates num by performing integer division with base.

Main Code:
num_str = input("Enter the number: "): Prompts the user to enter the number as a string.
base_from = int(input("Enter the base of the number: ")): Prompts the user to enter the base of the given number.
base_to = int(input("Enter the base to convert to: ")): Prompts the user to enter the target base for conversion.
decimal_num = to_decimal(num_str, base_from): Converts the input number to decimal.
converted_num = from_decimal(decimal_num, base_to): Converts the decimal number to the desired base.
print("Converted number:", converted_num): Outputs the converted number.
"""