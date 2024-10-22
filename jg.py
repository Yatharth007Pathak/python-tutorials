# Ask the user for a number and its base
number = input("Enter the number: ")
base = int(input("Enter the base of the number: "))

# Convert the number to a decimal (base 10) number
decimal_number = int(number, base)

# Print the result
print(f"The decimal (base 10) equivalent of {number} in base {base} is {decimal_number}.")


# easiest python code to ask user a number and its base and convert that number to decimal number

'''
This code uses the built-in int() function, which can convert a string representation of a number in a specified base to a decimal integer. 
Here's how it works:

The input() function asks the user to input a number and its base.
The base is converted to an integer using int().
The number is then converted to a decimal integer using int(number, base).
The result is printed to the user.
'''

"""
Here's a line-by-line breakdown of the code

number = input("Enter the number: "): 
This line prompts the user to enter a number and waits for the user to input a value. 
The input value is taken as a string and stored in the variable number.

base = input("Enter the base of the number: "): 
This line prompts the user to enter the base of the number and waits for the user to input a value. 
The input value is taken as a string and stored in variable base.
int(...): The string input is converted to an integer using the int() function. This integer is then stored in the variable base.

decimal_number = int(number, base): 
This line converts the string number, which is in the specified base, to a decimal (base 10) integer. 
The int() function can take two arguments: the first is the string representation of the number, and the second is the base of that number. 
The result of this conversion is stored in the variable decimal_number

print(...): 
This line prints the result using an f-string, which allows for easy formatting of the output. 
It includes the original number, its base, and the converted decimal value. 
The {} placeholders in the f-string are replaced with the values of number, base, and decimal_number
"""