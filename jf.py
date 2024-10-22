def convert_base(number, from_base, to_base):

    # Convert the number from the original base to base 10
    base10_number = int(number, from_base)
    
    # Convert the base 10 number to the desired base
    if to_base == 10:
        return str(base10_number)
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    result = ""
    while base10_number > 0:
        result = digits[base10_number % to_base] + result
        base10_number //= to_base
    
    return result

# Get user input
number = input("Enter the number: ")
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))

# Perform the conversion
converted_number = convert_base(number, from_base, to_base)

print(f"The number {number} from base {from_base} to base {to_base} is: {converted_number}")


# Python script that takes a number and its base as input from the user and converts it to another base specified by the user

'''
This script includes the following steps:

Converts the input number from the original base to base 10.
Converts the base 10 number to the desired base.
Asks the user to input the number and the bases.
Outputs the converted number.
'''

"""
here's a detailed breakdown of each line of the code:

def convert_base(number, from_base, to_base):
This line defines a function named convert_base which takes three parameters: number, from_base, and to_base.

base10_number = int(number, from_base)
converting the number from its original base to base 10.
The int function is used to convert the number from the from_base to a base 10 integer (base10_number).

if to_base == 10:
    return str(base10_number)
converting the base 10 number to the desired base.
If the target base (to_base) is 10, the function returns the base10_number converted to a string because no further conversion is needed.

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
This line defines a string digits containing all possible digits for bases up to 36. 
This is used to map numerical values to their respective characters in different bases.

result = ""
This line initializes an empty string result to build the final converted number.

while base10_number > 0:
    result = digits[base10_number % to_base] + result
    base10_number //= to_base
This while loop runs as long as base10_number is greater than 0.

Inside the loop:
base10_number % to_base finds the remainder when base10_number is divided by to_base. This remainder is the next digit in the target base.
digits[base10_number % to_base] fetches the corresponding character for the remainder.
result = digits[base10_number % to_base] + result prepends this character to the result string.
base10_number //= to_base performs integer division on base10_number by to_base, effectively shifting the digits to the right.

return result
This line returns the final converted number as a string.

# Get user input
number = input("Enter the number: ")
from_base = int(input("Enter the base of the number: "))
to_base = int(input("Enter the base to convert to: "))
These lines prompt the user to enter:
The number to be converted.
The from_base, which is converted to an integer using int().
The to_base, which is also converted to an integer using int().

# Perform the conversion
converted_number = convert_base(number, from_base, to_base)
This line calls the convert_base function with the user-provided number, from_base, and to_base, storing the result in converted_number.

print(f"The number {number} from base {from_base} to base {to_base} is: {converted_number}")
This line prints the result of the conversion, showing the original number, its base, the target base, and the converted number. 
The f before the string denotes an f-string, which allows for the inclusion of variables directly within the string.
"""