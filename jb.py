def convert_to_decimal(number, base):
    try:
        # Convert the number from the given base to a decimal integer
        decimal_number = int(number, base)
        return decimal_number
    except ValueError:
        return "Invalid number or base."

def main():
    # Ask the user for the number and its base
    number = input("Enter the number: ")
    base = int(input("Enter the base (2 to 36): "))

    # Validate the base
    if base < 2 or base > 36:
        print("Base must be between 2 and 36.")
        return
    
    # Convert the number to decimal and display the result
    result = convert_to_decimal(number, base)
    print(f"The decimal equivalent of {number} in base {base} is: {result}")

if __name__ == "__main__":
    main()

# python code where we ask user for a number and its base and convert the number from its base to decimal number system

'''
This script includes:
A function convert_to_decimal to handle the conversion from the given base to decimal.
The main function which takes input from the user, validates the base, and prints the converted decimal number.
Basic error handling for invalid inputs.
'''

"""
here's a breakdown of each line of the provided Python code:

def convert_to_decimal(number, base):
This line defines a function named convert_to_decimal that takes two parameters: number and base.

try:
This begins a try block to catch potential errors during the conversion process.

decimal_number = int(number, base)
This line attempts to convert the number from the given base to a decimal (base-10) integer using the int function. 
The int function can take a string and a base and convert it to a base-10 integer.

return decimal_number
If the conversion is successful, the function returns the decimal number.

except ValueError:
This line begins an except block to handle ValueError exceptions, which can occur if the number is not valid for the specified base.

return "Invalid number or base."
If a ValueError is caught, the function returns a message indicating that the number or base is invalid.

def main():
This line defines the main function named main, which contains the primary logic of the script.

number = input("Enter the number: ")
This line prompts the user to enter a number and stores the input as a string in the variable number.

base = int(input("Enter the base (2 to 36): "))
This line prompts the user to enter the base, converts the input to an integer, and stores it in the variable base.

if base < 2 or base > 36:
This line checks if the entered base is less than 2 or greater than 36.

print("Base must be between 2 and 36.")
If the base is outside the valid range (2 to 36), this line prints an error message.

return
This line exits the main function early if the base is invalid.

result = convert_to_decimal(number, base)
This line calls the convert_to_decimal function with the user-provided number and base and stores the result in the variable result.

print(f"The decimal equivalent of {number} in base {base} is: {result}")
This line prints the result, showing the decimal equivalent of the given number in the specified base.

if __name__ == "__main__":
This line checks if the script is being run directly (not imported as a module).

main()
If the script is run directly, this line calls the main function to execute the program.
"""