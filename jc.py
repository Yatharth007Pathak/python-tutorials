def base_to_decimal(number, base):
    decimal_number = 0
    power = 0
    
    while number > 0:
        digit = number % 10
        decimal_number += digit * (base ** power)
        number //= 10
        power += 1
    
    return decimal_number

# Ask user for input
number = int(input("Enter the number: "))
base = int(input("Enter the base: "))

# Convert and display the decimal number
decimal_number = base_to_decimal(number, base)
print(f"The decimal equivalent of the number is: {decimal_number}")

# python code where we ask user for a number and its base and convert the number from its base to decimal number system using while loop

'''
Here’s how the code works:

base_to_decimal function: This function takes the number and base as input and converts the number 
from the given base to a decimal number using a while loop.

decimal_number is initialized to 0. This will hold the final decimal value.
power is initialized to 0. This represents the position of the digit in the base system.

The while loop runs as long as number is greater than 0.
It extracts the last digit of number using number % 10.
The digit is then multiplied by the base raised to the power of its position and added to decimal_number.
The number is then divided by 10 to remove the last digit.
The power is incremented by 1.

User input: The user is prompted to enter the number and base.

The function base_to_decimal is called with the user inputs, and the decimal equivalent is printed.
'''