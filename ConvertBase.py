def convert_base():
    try:
        # Input number, its base, and the target base
        number = input("Enter the number: ").strip()
        base_from = int(input("Enter the base of the given number (e.g., 2 for binary, 8 for octal): ").strip())
        base_to = int(input("Enter the base to convert to (e.g., 10 for decimal, 16 for hexadecimal): ").strip())
        
        if base_from < 2 or base_from > 36 or base_to < 2 or base_to > 36:
            print("Base must be between 2 and 36.")
            return
        
        # Convert the input number to decimal
        decimal_number = int(number, base_from)
        
        # Convert the decimal number to the target base
        def decimal_to_base(number, base):
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = ""
            while number > 0:
                result = digits[number % base] + result
                number //= base
            return result or "0"  # Return "0" if the number is 0
        
        # Perform the conversion and display the result
        converted_number = decimal_to_base(decimal_number, base_to)
        print(f"The number {number} in base {base_from} is {converted_number} in base {base_to}.")
    except ValueError:
        print("Invalid input! Please ensure the number and base are valid.")

# Call the function
convert_base()

'''
How it works:
Step 1: Takes the input number and its base (base_from) from the user.
Step 2: Converts the number to decimal using Python's int() function.
Step 3: Converts the decimal number to the desired base (base_to) using a custom function decimal_to_base.
Validation: Ensures both bases are between 2 and 36.
'''

'''
Line-by-Line Breakdown:

def convert_base():
Defines a function named convert_base that facilitates conversion between any two bases (2 to 36).

try:
Starts a try block to handle potential errors in user input or calculations.

number = input("Enter the number: ").strip()
Prompts the user to input a number, removes any leading or trailing spaces, and stores it in number.

base_from = int(input("Enter the base of the given number (e.g., 2 for binary, 8 for octal): ").strip())
Prompts the user for the base of the input number, strips spaces, converts it to an integer, and stores it in base_from.

base_to = int(input("Enter the base to convert to (e.g., 10 for decimal, 16 for hexadecimal): ").strip())
Prompts the user for the target base to convert the number into, processes it similarly, and stores it in base_to.

if base_from < 2 or base_from > 36 or base_to < 2 or base_to > 36:
Checks if either the input or target base is outside the valid range (2 to 36). If true, the next line informs the user and stops execution.

print("Base must be between 2 and 36.")
Prints a message explaining the valid range of bases.

return
Exits the function without executing further code if the base range is invalid.

decimal_number = int(number, base_from)
Converts the input number from its specified base (base_from) to a decimal integer using 
Python's int() function and stores it in decimal_number.

def decimal_to_base(number, base):
Defines a nested helper function to convert a decimal number to a specified base.

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A string containing all possible characters for bases up to 36.

result = ""
Initializes an empty string to accumulate the digits of the converted number.

while number > 0:
Loops until the number is reduced to 0, repeatedly extracting the base-specific digits.

result = digits[number % base] + result
Calculates the current digit by finding the remainder of number divided by base, 
retrieves the corresponding character from digits, and prepends it to result.

number //= base
Performs integer division of number by base to prepare for the next digit.

return result or "0"
Returns the converted number if it's non-zero; otherwise, returns "0" (handles cases where the input number is 0).

converted_number = decimal_to_base(decimal_number, base_to)
Calls the helper function to convert the intermediate decimal value (decimal_number) to the target base (base_to) 
and stores the result in converted_number.

print(f"The number {number} in base {base_from} is {converted_number} in base {base_to}.")
Outputs the original number, its base, the target base, and the converted number using an f-string for clarity.

except ValueError:
Catches any errors arising from invalid user inputs, such as non-numeric characters or invalid bases.

print("Invalid input! Please ensure the number and base are valid.")
Prints an error message guiding the user to provide correct inputs.

convert_base()
Calls the convert_base function, triggering the code execution to perform base conversion.
'''