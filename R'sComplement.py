def convert_to_r_complement():
    try:
        # Input the number, its base and the number of digits (n) to consider
        number = input("Enter the number: ").strip()
        base = int(input("Enter the base of the number (e.g., 2 for binary, 8 for octal, etc.): ").strip())
        num_digits = int(input("Enter the number of digits (n) in the number: ").strip())
        
        if base < 2 or base > 36:
            print("Base must be between 2 and 36.")
            return
        
        # Convert the number from the given base to decimal
        decimal_number = int(number, base)

        # Calculate r^n
        r_power_n = base ** num_digits
        
        # Calculate the r's complement by subtracting the number from r^n
        r_complement = r_power_n - decimal_number
        
        # Convert the result back to the given base
        r_complement_in_base = ''
        if r_complement == 0:
            r_complement_in_base = '0'
        else:
            while r_complement > 0:
                r_complement_in_base = str(r_complement % base) + r_complement_in_base
                r_complement //= base
        
        # Ensure the result is padded to n digits
        r_complement_in_base = r_complement_in_base.zfill(num_digits)
        
        print(f"The {base}-complement of {number} in base {base} with {num_digits} digits is: {r_complement_in_base}")
    
    except ValueError:
        print("Invalid input! Please ensure the number, base, and number of digits are valid.")

# Call the function
convert_to_r_complement()

'''
How It Works:
Input: The user provides a number in any base (from 2 to 36), the base of that number, and the number of digits (n).
Convert to Decimal: The number is converted from the given base to decimal using Python's int() function.
Compute r's Complement: The r's complement is calculated as r^n - number, where r is the base and n is the number of digits.
Convert Result Back to Base: The r's complement result is then converted back to the original base using the division-remainder method.
Output: The program prints the r's complement in the specified base.
'''

'''
Line-by-Line Breakdown:

def convert_to_r_complement():
Defines the function convert_to_r_complement, which will convert a number to its r's complement in the given base.

try:
Starts a try block to handle any exceptions that may occur during input or processing.

number = input("Enter the number: ").strip()
Prompts the user to input a number, removes any leading or trailing whitespace, and stores it in the variable number.

base = int(input("Enter the base of the number (e.g., 2 for binary, 8 for octal, etc.): ").strip())
Prompts the user to input the base of the number and converts it to an integer (base).

num_digits = int(input("Enter the number of digits (n) in the number: ").strip())
Prompts the user to input the number of digits (n) to consider for the r's complement and converts it to an integer (num_digits).

if base < 2 or base > 36:
Checks if the base is valid (between 2 and 36, inclusive). If not, it prints an error message and exits.

print("Base must be between 2 and 36.")
Displays an error message if the base is out of the valid range.

return
Exits the function if the base is invalid.

decimal_number = int(number, base)
Converts the input number from the given base to a decimal integer (decimal_number).

r_power_n = base ** num_digits
Calculates r^n, which is the base raised to the power of n (the number of digits).

r_complement = r_power_n - decimal_number
Calculates the r's complement by subtracting the decimal number from r^n.

r_complement_in_base = ''
Initializes an empty string to store the r's complement in the desired base.

if r_complement == 0:
Checks if the r's complement is 0.

r_complement_in_base = '0'
If the r's complement is 0, it directly assigns '0' to the result.

else:
If the r's complement is non-zero, the following steps convert it to the desired base.

while r_complement > 0:
Loops as long as r_complement is greater than 0.

r_complement_in_base = str(r_complement % base) + r_complement_in_base
Converts the current remainder of r_complement when divided by the base to a string and prepends it to r_complement_in_base.

r_complement //= base
Divides r_complement by the base (integer division), reducing the value for the next iteration.

r_complement_in_base = r_complement_in_base.zfill(num_digits)
Pads the r's complement result to ensure it has exactly num_digits digits using .zfill().

print(f"The {base}-complement of {number} in base {base} with {num_digits} digits is: {r_complement_in_base}")
Displays the final r's complement in the desired base with the specified number of digits.

except ValueError:
Catches any ValueError exceptions (e.g., if the input is not valid).

print("Invalid input! Please ensure the number, base, and number of digits are valid.")
Displays an error message if any input is invalid.

convert_to_r_complement()
Calls the function to perform the r's complement conversion.
'''