def convert_to_decimal():
    try:
        # Input number and base
        number = input("Enter the number: ").strip()
        base = int(input("Enter the base of the number (e.g., 2 for binary, 8 for octal): ").strip())
        
        # Convert to decimal
        decimal_value = int(number, base)
        
        # Display the result
        print(f"The decimal equivalent of {number} in base {base} is: {decimal_value}")
    except ValueError:
        print("Invalid input! Please ensure the number and base are valid.")

# Call the function
convert_to_decimal()

'''
How it works:
The int() function with two arguments converts a string representation of a number in a specified base to decimal.
The try-except block handles invalid inputs, such as invalid digits for the given base or a non-integer base.
'''

'''
Line-by-Line Breakdown:

def convert_to_decimal():
This defines a function named convert_to_decimal. A function groups related code together for reuse.

try:
Begins a try block to handle potential errors during the execution of the code inside it.

number = input("Enter the number: ").strip()
Prompts the user to input a number, removes any leading or trailing spaces using .strip(), and stores it in the variable number.

base = int(input("Enter the base of the number (e.g., 2 for binary, 8 for octal): ").strip())
Prompts the user to input the base of the number (e.g., 2 for binary or 8 for octal), 
removes any spaces, converts the input to an integer, and stores it in the variable base.

decimal_value = int(number, base)
Converts the number (a string) to its decimal equivalent based on the specified base using 
Python's built-in int() function and stores the result in decimal_value.

print(f"The decimal equivalent of {number} in base {base} is: {decimal_value}")
Outputs the decimal equivalent of the number along with the original base and the converted decimal value using an f-string for formatting.

except ValueError:
Defines an exception block that executes if there is a ValueError during the conversion 
(e.g., invalid inputs like "abc" for a number or a base outside valid ranges).

print("Invalid input! Please ensure the number and base are valid.")
If a ValueError occurs, this line displays a user-friendly error message to guide the user.

convert_to_decimal()
Calls the convert_to_decimal function to execute the defined steps.
'''