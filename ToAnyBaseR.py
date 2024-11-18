def convert_decimal_to_base():
    try:
        # Input the decimal real number and the target base
        decimal_number = float(input("Enter a decimal real number: ").strip())
        base = int(input("Enter the base to convert to (e.g., 2 for binary, 8 for octal, etc.): ").strip())
        
        if base < 2 or base > 36:
            print("Base must be between 2 and 36.")
            return
        
        # Digits for bases up to 36
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        # Separate integer and fractional parts
        integer_part = int(decimal_number)
        fractional_part = decimal_number - integer_part

        # Convert the integer part to the target base
        def integer_to_base(number, base):
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
                result += digits[int(fraction)]
                fraction -= int(fraction)
            return result

        # Perform conversions
        integer_converted = integer_to_base(integer_part, base)
        fractional_converted = fractional_to_base(fractional_part, base)

        # Combine the integer and fractional parts
        if fractional_converted:
            converted_number = f"{integer_converted}.{fractional_converted}"
        else:
            converted_number = integer_converted

        print(f"The number {decimal_number} in base {base} is: {converted_number}")
    except ValueError:
        print("Invalid input! Please ensure the number and base are valid.")

# Call the function
convert_decimal_to_base()

'''
How It Works:
Input: The user provides a decimal real number and the target base.
Integer Conversion: Converts the integer part using repeated division and modulus operations.
Fractional Conversion: Multiplies the fractional part by the target base repeatedly, 
extracting the integer part of the result each time to form the converted fractional part.
Precision: Limits the fractional conversion to 10 digits by default (can be adjusted via the precision parameter).
Combining Results: Combines the converted integer and fractional parts to produce the final result.
Validation: Ensures the base is between 2 and 36.
'''

'''
Line-by-Line Breakdown:

def convert_decimal_to_base():
Defines a function named convert_decimal_to_base that converts a decimal real number into a specified base.

try:
Starts a try block to catch and handle errors during execution.

decimal_number = float(input("Enter a decimal real number: ").strip())
Prompts the user to input a decimal real number, removes spaces, converts it to a float, and stores it in decimal_number.

base = int(input("Enter the base to convert to (e.g., 2 for binary, 8 for octal, etc.): ").strip())
Prompts the user for the target base, removes spaces, converts it to an integer, and stores it in base.

if base < 2 or base > 36:
Validates that the base is within the range 2 to 36. If not, the next line informs the user and stops execution.

print("Base must be between 2 and 36.")
Displays a message specifying the valid range of bases.

return
Exits the function if the base is invalid.

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A string containing possible digits for bases up to 36.

integer_part = int(decimal_number)
Extracts the integer part of the input number using int().

fractional_part = decimal_number - integer_part
Calculates the fractional part by subtracting the integer part from the original number.

def integer_to_base(number, base):
Defines a nested function to convert the integer part to the specified base.

result = ""
Initializes an empty string to hold the converted integer part.

while number > 0:
Loops until the integer part is reduced to zero through successive division.

result = digits[number % base] + result
Finds the remainder when dividing number by base, retrieves the corresponding character from digits, and prepends it to result.

number //= base
Performs integer division of number by base to process the next digit.

return result or "0"
Returns the converted integer part. If number was zero, returns "0".

def fractional_to_base(fraction, base, precision=10):
Defines a nested function to convert the fractional part to the specified base with a precision limit of 10 digits.

result = ""
Initializes an empty string to hold the converted fractional part.

while fraction > 0 and len(result) < precision:
Loops until the fractional part becomes zero or the precision limit is reached.

fraction *= base
Multiplies the fractional part by the base to extract the next digit.

result += digits[int(fraction)]
Converts the integer part of the result to a character and appends it to result.

fraction -= int(fraction)
Subtracts the integer part from the fraction to continue processing the next digit.

return result
Returns the converted fractional part.

integer_converted = integer_to_base(integer_part, base)
Calls the integer_to_base function to convert the integer part and stores the result.

fractional_converted = fractional_to_base(fractional_part, base)
Calls the fractional_to_base function to convert the fractional part and stores the result.

if fractional_converted:
Checks if the fractional part exists (non-empty).

converted_number = f"{integer_converted}.{fractional_converted}"
Combines the converted integer and fractional parts with a decimal point.

else:
Executes if there is no fractional part.

converted_number = integer_converted
Assigns the converted integer part as the final result.

print(f"The number {decimal_number} in base {base} is: {converted_number}")
Outputs the original number, the target base, and the converted result using an f-string.

except ValueError:
Catches errors such as invalid input types (e.g., non-numeric values).

print("Invalid input! Please ensure the number and base are valid.")
Displays an error message to guide the user.

convert_decimal_to_base()
Calls the function to execute the conversion process.
'''