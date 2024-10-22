num = int(input("Enter a decimal number: "))
base = int(input("Enter the base to convert to : "))
result = ''

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Digits for bases up to 36

if num == 0:
    result = '0'
else:
    while num > 0:
        result = digits[num % base] + result
        num //= base

print("Converted number:", result)


# easiest python code to ask user a number in decimal system and convert that number from decimal base to another base

"""
Here's a line-by-line breakdown of the code

num = int(input("Enter a decimal number: ")):
Prompts the user to enter a decimal number.
int(...): Converts the user input (which is a string) into an integer.
num: Stores the integer value of the decimal number entered by the user.

base = int(input("Enter the base to convert to: "))
Prompts the user to enter the target base.
int(...): Converts the user input (which is a string) into an integer.
base: Stores the integer value of the base to which the decimal number will be converted.

result = '':
Initializes an empty string to build the converted number in the target base.

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
Defines a string containing all possible characters used in bases up to 36.

if num == 0:
    result = '0'
if num == 0:: Checks if the entered decimal number is 0.
result = '0': If the number is 0, directly sets the result to '0', since 0 in any base is still 0.

else:
    while num > 0:
        result = digits[num % base] + result
        num //= base
else:: Executes if the number is not 0.
while num > 0:: Repeats the loop until num becomes 0.
result = digits[num % base] + result: Computes the remainder of num divided by base, uses this remainder as an index to retrieve 
the corresponding character from the digits string, and prepends this character to result.
num //= base: Updates num by performing integer division with base, effectively reducing the number for the next iteration.

print("Converted number:", result):
Outputs the final converted number in the target base.
"""