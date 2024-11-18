def convert_real_number_to_decimal():
    try:
        # Input the number and its base
        real_number = input("Enter the real number: ").strip()
        base = int(input("Enter the base of the number (e.g., 2 for binary, 8 for octal): ").strip())
        
        if base < 2 or base > 36:
            print("Base must be between 2 and 36.")
            return
        
        # Split the number into the integer and fractional parts
        if '.' in real_number:
            integer_part, fractional_part = real_number.split('.')
        else:
            integer_part, fractional_part = real_number, ""
        
        # Convert the integer part to decimal
        integer_decimal = int(integer_part, base) if integer_part else 0
        
        # Convert the fractional part to decimal
        fractional_decimal = 0
        for i, digit in enumerate(fractional_part):
            fractional_decimal += int(digit, base) / (base ** (i + 1))
        
        # Combine the integer and fractional parts
        total_decimal = integer_decimal + fractional_decimal
        print(f"The decimal equivalent of {real_number} in base {base} is: {total_decimal}")
    
    except ValueError:
        print("Invalid input! Please ensure the number and base are valid.")

# Call the function
convert_real_number_to_decimal()

'''
How it works:
Input Parsing: Splits the input into an integer part and a fractional part using split('.').
Conversion: The integer part is converted using Python’s int() function with the specified base.
The fractional part is processed manually by summing each digit's value divided by its positional power (e.g., digit * base^-position).
Validation: Ensures the base is between 2 and 36.
Output: Combines the integer and fractional decimal values into a final result.
'''

'''
Line-by-Line Breakdown:

def convert_real_number_to_decimal():
Defines a function named convert_real_number_to_decimal for converting real numbers 
(including fractional parts) from a specified base to decimal.

try:
Begins a try block to handle errors in user input or calculations.

real_number = input("Enter the real number: ").strip()
Prompts the user to input a real number (with or without a fractional part), removes spaces, and stores it in real_number.

base = int(input("Enter the base of the number (e.g., 2 for binary, 8 for octal): ").strip())
Prompts the user for the base of the number, removes spaces, converts it to an integer, and stores it in base.

if base < 2 or base > 36:
Checks if the base is outside the valid range (2 to 36). If so, the next line informs the user and stops execution.

print("Base must be between 2 and 36.")
Displays a message informing the user of the valid range of bases.

return
Exits the function if the base is invalid.

if '.' in real_number:
Checks if the input number contains a fractional part (indicated by a dot .).

integer_part, fractional_part = real_number.split('.')
Splits the number into its integer and fractional parts if a dot is present.

else:
Executes when the input number does not contain a fractional part.

integer_part, fractional_part = real_number, ""
Assigns the entire number to integer_part and leaves fractional_part empty.

integer_decimal = int(integer_part, base) if integer_part else 0
Converts the integer part to its decimal equivalent using the int() function with the specified base. 
If integer_part is empty, it defaults to 0.

fractional_decimal = 0
Initializes a variable to hold the decimal value of the fractional part.

for i, digit in enumerate(fractional_part):
Iterates through each digit of the fractional part along with its position (index).

fractional_decimal += int(digit, base) / (base ** (i + 1))
Converts each digit of the fractional part to decimal by dividing its decimal equivalent by the base raised to the power of its position.

total_decimal = integer_decimal + fractional_decimal
Combines the integer and fractional parts to get the total decimal equivalent.

print(f"The decimal equivalent of {real_number} in base {base} is: {total_decimal}")
Outputs the original number, its base, and its decimal equivalent using an f-string.

except ValueError:
Catches errors such as invalid characters in the number or an invalid base.

print("Invalid input! Please ensure the number and base are valid.")
Displays an error message guiding the user to provide correct inputs.

convert_real_number_to_decimal()
Calls the function to execute the conversion process
'''