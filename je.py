def decimal_to_base(number, base):
    if number == 0:
        return '0'
    
    digits = []
    
    while number > 0:
        remainder = number % base
        digits.append(str(remainder))
        number //= base
    
    # The digits are obtained in reverse order, so we need to reverse them
    digits.reverse()
    
    return ''.join(digits)

# Ask user for input
number = int(input("Enter the decimal number: "))
base = int(input("Enter the base: "))

# Convert and display the number in the desired base
converted_number = decimal_to_base(number, base)
print(f"The number {number} in base {base} is: {converted_number}")

# python code where we ask user for a number in decimal number system and convert the number to any base system using while loop

"""
Here’s how the code works:

decimal_to_base function: This function takes a number and a base as input and converts the decimal number to the desired base using a while loop.

If the number is 0, it directly returns '0'.
digits is initialized as an empty list to store the digits of the converted number.
The while loop runs as long as number is greater than 0.
It computes the remainder of number divided by base and appends it to the digits list.
The number is then divided by the base to prepare for the next iteration.
The digits are obtained in reverse order, so they need to be reversed before joining them into a single string.

User input: The user is prompted to enter the number (in decimal) and the base.

The function decimal_to_base is called with the user inputs, and the converted number is printed.
"""