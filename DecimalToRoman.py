# function converts a decimal integer into a Roman numeral string.

def convertRoman(n):
    # Define a list of tuples that map integers to their Roman numeral equivalents
    roman_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
        
    # Initialize the result string
    result = ""
        
    # Iterate over the roman_map
    for value, symbol in roman_map:
        # While n is greater than or equal to the value, append the symbol to the result
        while n >= value:
            result += symbol
            n -= value  # Decrease n by the value
            
    return result

# Example usage:
print(convertRoman(5))  # Output: V
print(convertRoman(3))  # Output: III
print(convertRoman(9))  # Output: IX
print(convertRoman(44))  # Output: XLIV
print(convertRoman(1994))  # Output: MCMXCIV

'''
Here's a breakdown of the convertRoman function code line by line:

Function Definition: The function convertRoman(n) is defined, 
where n is an integer representing the decimal number that needs to be converted to a Roman numeral.

Mapping Integers to Roman Numerals: A list named roman_map is defined, 
consisting of tuples that pair integer values with their corresponding Roman numeral representations.
This includes values from 1000 (M) down to 1 (I), with special combinations for 900 (CM), 400 (CD), 90 (XC), 40 (XL), 9 (IX), and 4 (IV).

Initialize Result String: An empty string variable result is initialized. 
This string will hold the final Roman numeral representation as the function processes the input integer.

Iterate Over roman_map: A for loop iterates through each tuple in the roman_map, 
unpacking the values into value (the integer) and symbol (the corresponding Roman numeral).

While Loop for Conversion: Inside the for loop, a while loop checks if n is greater than or equal to value. 
This condition ensures that the function continues to subtract the integer value from n while it is still larger than or equal to that value.

Appending Symbols: If the condition is true, the current symbol (Roman numeral) is appended to the result string, 
and n is decreased by the corresponding value. This process effectively converts part of the integer into its Roman numeral equivalent.

Return Result: After all iterations and conversions are complete, the function returns the final result string, 
which now contains the complete Roman numeral representation of the input integer.

Example Usage: The function is called multiple times with various integer inputs, such as 5, 3, 9, 44, and 1994, 
with the expected outputs printed: V, III, IX, XLIV, and MCMXCIV, respectively.
'''