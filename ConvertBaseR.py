def convert_real_number_base():
    try:
        # Input the real number, its base, and the target base
        real_number = input("Enter the real number: ").strip()
        base_from = int(input("Enter the base of the given number (e.g., 2 for binary, 8 for octal, etc.): ").strip())
        base_to = int(input("Enter the base to convert to (e.g., 10 for decimal, 16 for hexadecimal): ").strip())
        
        if base_from < 2 or base_from > 36 or base_to < 2 or base_to > 36:
            print("Base must be between 2 and 36.")
            return
        
        # Split the number into integer and fractional parts
        if '.' in real_number:
            integer_part, fractional_part = real_number.split('.')
        else:
            integer_part, fractional_part = real_number, ""
        
        # Convert the integer part from base_from to decimal
        integer_decimal = int(integer_part, base_from) if integer_part else 0
        
        # Convert the fractional part from base_from to decimal
        fractional_decimal = 0
        for i, digit in enumerate(fractional_part):
            fractional_decimal += int(digit, base_from) / (base_from ** (i + 1))
        
        # Convert the integer part to the target base
        def decimal_to_base(number, base):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while number > 0:
                result = digits[number % base] + result
                number //= base
            return result or "0"
        
        # Convert the fractional part to the target base
        def fractional_to_base(fraction, base, precision=10):
            result = ""
            while fraction > 0 and len(result) < precision:
                fraction *= base
                result += str(int(fraction))
                fraction -= int(fraction)
            return result
        
        # Convert the integer part to the target base
        integer_in_base_to = decimal_to_base(integer_decimal, base_to)
        
        # Convert the fractional part to the target base
        fractional_in_base_to = fractional_to_base(fractional_decimal, base_to)
        
        # Combine the integer and fractional parts
        if fractional_in_base_to:
            converted_number = f"{integer_in_base_to}.{fractional_in_base_to}"
        else:
            converted_number = integer_in_base_to
        
        print(f"The number {real_number} in base {base_from} is: {converted_number} in base {base_to}")
    
    except ValueError:
        print("Invalid input! Please ensure the number and base are valid.")

# Call the function
convert_real_number_base()

'''
How It Works:
Input Parsing: The user inputs the real number, its base (base_from), and the target base (base_to). 
Integer and Fractional Conversion: The number is split into integer and fractional parts.
The integer part is converted from the original base (base_from) to decimal.
The fractional part is also converted to decimal by multiplying each digit by the 
corresponding base raised to the negative power of its position.
Conversion to Target Base: The integer part is converted to the target base using repeated division and modulus operations.
The fractional part is converted by multiplying the fractional value by the target base and extracting the integer part iteratively.
Precision: The fractional part conversion is limited to 10 digits for precision (this can be changed by adjusting the precision parameter).
Validation: Ensures that both bases are between 2 and 36.
Output: Combines the converted integer and fractional parts to form the final result.
'''

'''
Line-by-Line Breakdown:

def convert_real_number_base():
Defines the function convert_real_number_base, which will handle the conversion of real numbers 
between different bases (including fractional parts).

try:
Starts a try block to catch any exceptions during input or calculation.

real_number = input("Enter the real number: ").strip()
Prompts the user to input a real number (possibly including a fractional part), 
removes any leading or trailing spaces, and stores it in real_number.

base_from = int(input("Enter the base of the given number (e.g., 2 for binary, 8 for octal, etc.): ").strip())
Prompts the user for the base of the input number (e.g., binary, octal) and stores it as an integer in base_from.

base_to = int(input("Enter the base to convert to (e.g., 10 for decimal, 16 for hexadecimal): ").strip())
Prompts the user for the target base (e.g., decimal, hexadecimal) and stores it as an integer in base_to.

if base_from < 2 or base_from > 36 or base_to < 2 or base_to > 36:
Checks if the input bases are within the valid range (2 to 36). If not, it proceeds to the next line.

print("Base must be between 2 and 36.")
Displays a message informing the user that the base must be between 2 and 36.

return
Exits the function if any of the bases are out of the valid range.

if '.' in real_number:
Checks if the real_number contains a decimal point, indicating the presence of a fractional part.

integer_part, fractional_part = real_number.split('.')
Splits the real_number into its integer part and fractional part based on the decimal point.

else:
Executes if the real_number does not contain a decimal point.

integer_part, fractional_part = real_number, ""
Assigns the entire real_number to integer_part and sets fractional_part to an empty string, indicating no fractional part.

integer_decimal = int(integer_part, base_from) if integer_part else 0
Converts the integer part from base_from to decimal using int(). If integer_part is empty, defaults to 0.

fractional_decimal = 0
Initializes fractional_decimal to 0, which will hold the decimal value of the fractional part.

for i, digit in enumerate(fractional_part):
Iterates over each digit of the fractional part, along with its position (i).

fractional_decimal += int(digit, base_from) / (base_from ** (i + 1))
Converts each digit of the fractional part from base_from to decimal and adds it to fractional_decimal, 
considering the base and position of the digit.

def decimal_to_base(number, base):
Defines a nested function to convert the integer part from decimal to the target base_to.

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A string containing all valid digits for bases up to 36.

result = ""
Initializes an empty string result to hold the converted integer part.

while number > 0:
Loops as long as number is greater than 0, continuously dividing it by the base to extract each digit.

result = digits[number % base] + result
Finds the remainder when dividing number by base, retrieves the corresponding digit from digits, and prepends it to result.

number //= base
Integer division of number by base to process the next digit.

return result or "0"
Returns the converted number as a string. If number is 0, returns "0".

def fractional_to_base(fraction, base, precision=10):
Defines a nested function to convert the fractional part to the target base_to. 
It has a precision parameter to limit the number of digits in the fractional part.

result = ""
Initializes an empty string result to hold the converted fractional part.

while fraction > 0 and len(result) < precision:
Loops as long as the fractional part is greater than 0 and the result has fewer than the specified precision digits.

fraction *= base
Multiplies the fractional part by base to get the next digit.

result += str(int(fraction))
Converts the integer part of the fraction to a string and appends it to result.

fraction -= int(fraction)
Removes the integer part from fraction to continue processing the next digit.

return result
Returns the fractional part as a string.

integer_in_base_to = decimal_to_base(integer_decimal, base_to)
Converts the integer part from decimal to the target base using decimal_to_base.

fractional_in_base_to = fractional_to_base(fractional_decimal, base_to)
Converts the fractional part from decimal to the target base using fractional_to_base.

if fractional_in_base_to:
Checks if the fractional part is non-empty.

converted_number = f"{integer_in_base_to}.{fractional_in_base_to}"
Combines the converted integer and fractional parts into a final string with a decimal point.

else:
Executes if the fractional part is empty.

converted_number = integer_in_base_to
Assigns the converted integer part as the final result.

print(f"The number {real_number} in base {base_from} is: {converted_number} in base {base_to}")
Displays the original number, its base, and the converted result using an f-string.

except ValueError:
Catches any ValueError exceptions (e.g., invalid input types).

print("Invalid input! Please ensure the number and base are valid.")
Displays an error message informing the user to check their inputs.

convert_real_number_base()
Calls the function to execute the base conversion process.
'''