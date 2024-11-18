# function that converts Roman numeral strings to their equivalent decimal values.

def romanToDecimal(S):
    # Define a dictionary to map Roman numerals to their respective value
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


    # Initialize total to store the result
    total = 0
    length = len(S)

    # Traverse the string
    for i in range(length):
        # If the current symbol is less than the next symbol, subtract its value
        if i < length - 1 and roman_map[S[i]] < roman_map[S[i + 1]]:
            total -= roman_map[S[i]]
        else:
            # Otherwise, add its value to the total
            total += roman_map[S[i]]
 
    return total
    
# Example usage:
print(romanToDecimal("V"))  # Output: 5
print(romanToDecimal("III"))  # Output: 3
print(romanToDecimal("IX"))  # Output: 9
print(romanToDecimal("MCMXCIV"))  # Output: 1994

'''
Here's a breakdown of the romanToDecimal function code line by line:

Function Definition: The function romanToDecimal(S) is defined, where S is a string representing a Roman numeral.

Mapping Roman Numerals: A dictionary named roman_map is created, mapping Roman numeral characters to their respective integer values. 
This includes mappings for 'I', 'V', 'X', 'L', 'C', 'D', and 'M' to 1, 5, 10, 50, 100, 500, and 1000, respectively.

Initialization: A variable total is initialized to 0, which will hold the cumulative total value of the Roman numeral. 
The variable length is set to the length of the input string S.

Loop Through String: A for loop iterates through each character in the string using its index i, from 0 to length - 1.

Comparison for Subtraction: Inside the loop, an if statement checks if the current symbol 
(i.e., S[i]) is less than the next symbol (i.e., S[i + 1]). This is done by comparing their values using roman_map. 
The condition also ensures that i does not exceed length - 2 to avoid index errors.

Subtract Value: If the condition is true (indicating that the current symbol should be subtracted, 
as in the case of 'IV' where 'I' is less than 'V'), the value of the current symbol is subtracted from total.

Add Value: If the condition is false, meaning the current symbol is either greater than or equal to the next one, its value is added to total.

Return Result: After completing the loop, the function returns final computed total, which represents the decimal value of the Roman numeral.

Example Usage: The function is called multiple times with various Roman numeral inputs, 
such as "V", "III", "IX", and "MCMXCIV", with the expected outputs printed: 5, 3, 9, and 1994, respectively.
'''
