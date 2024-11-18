def convert_from_decimal():
    try:
        # Input a decimal number and the desired base
        decimal_number = int(input("Enter a decimal number: ").strip())
        base = int(input("Enter the base to convert to (e.g., 2 for binary, 8 for octal, etc.): ").strip())
        
        if base < 2 or base > 36:
            print("Base must be between 2 and 36.")
            return
        
        # Function to convert a decimal number to the given base
        def decimal_to_base(number, base):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while number > 0:
                result = digits[number % base] + result
                number //= base
            return result or "0"  # Return "0" if the number is 0
        
        # Convert and display the result
        converted_number = decimal_to_base(decimal_number, base)
        print(f"The number {decimal_number} in base {base} is: {converted_number}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Call the function
convert_from_decimal()

'''
How it works:
The decimal_to_base function converts the decimal number to the desired base using repeated division and modulus operations.
The digits string contains characters for bases up to 36 (digits 0-9 and letters A-Z).
Handles bases between 2 and 36, inclusive, and validates input values.
'''

'''
Line-by-Line Breakdown:

def convert_from_decimal():
This defines a function named convert_from_decimal, grouping the code for converting a decimal number into another base.

try:
Begins a try block to handle errors that might occur during input or calculations.

decimal_number = int(input("Enter a decimal number: ").strip())
Prompts the user to input a decimal number, removes any leading or trailing spaces, converts the input to an integer, 
and stores it in decimal_number.

base = int(input("Enter the base to convert to (e.g., 2 for binary, 8 for octal, etc.): ").strip())
Prompts the user to input the desired base for conversion, removes any spaces, converts it to an integer, and stores it in base.

if base < 2 or base > 36:
Checks if the entered base is outside the valid range (2 to 36). If so, the next line provides feedback and exits the function.

print("Base must be between 2 and 36.")
Prints a message to inform the user about the valid base range.

return
Exits the function without continuing further if the base is invalid.

def decimal_to_base(number, base):
Defines a nested function to perform the actual conversion of the decimal number into the specified base.

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A string containing all possible digits for bases up to 36 (0–9 for digits, A–Z for letters).

result = ""
Initializes an empty string to hold the converted number.

while number > 0:
Loops until the number becomes zero, performing successive division to determine the digits in the target base.

result = digits[number % base] + result
Calculates the remainder of number divided by base to find the current digit, 
retrieves the corresponding character from digits, and prepends it to result.

number //= base
Performs integer division of number by base to prepare for the next iteration.

return result or "0"
Returns the converted number if it exists. If the input number was 0, it returns "0" since no digits were processed in the loop.

converted_number = decimal_to_base(decimal_number, base)
Calls the nested decimal_to_base function with the user's inputs and stores the result in converted_number.

print(f"The number {decimal_number} in base {base} is: {converted_number}")
Outputs the original decimal number, the target base, and the converted number using an f-string.

except ValueError:
Catches errors (e.g., if the user enters non-numeric inputs for the decimal number or base).

print("Invalid input! Please enter valid numbers.")
Displays an error message to inform the user about invalid inputs.

convert_from_decimal()
Calls the convert_from_decimal function, triggering the execution of the defined logic.
'''