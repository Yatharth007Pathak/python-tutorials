def get_simplified_expression(minterms):
    # 3-variable K-map (2x4 grid for A, B, C)
    # Indices: m0, m1, m3, m2, m4, m5, m7, m6
    # The 8 cells correspond to the minterms for the 3-variable Boolean function: m0, m1, m2, m3, m4, m5, m6, m7.
    # Each cell represents a combination of values of A, B, and C.
    # 0: A'B'C'     1: A'B'C     3: A'BC     2: A'BC'     4: AB'C'     5: AB'C     7: ABC     6: ABC'
    k_map_values = [0] * 8  # 8 cells for a 3-variable K-map
    
    # Mark the minterms with 1 in the K-map
    for minterm in minterms:
        if 0 <= minterm <= 7:
            k_map_values[minterm] = 1
        else:
            print("Invalid minterm input! Please provide minterms between 0 and 7.")
            return
    
    # Output the K-map grid
    print("\nK-map (3 variables):")
    print(f"      00  01  11  10")
    print(f"0   | {k_map_values[0]} | {k_map_values[1]} | {k_map_values[3]} | {k_map_values[2]}")
    print(f"1   | {k_map_values[4]} | {k_map_values[5]} | {k_map_values[7]} | {k_map_values[6]}")  
    
    # Simplify the Boolean expression from the K-map
    expression = []
    
    # Check for pairs, quads, and octets
    # Horizontal pairs (A'BC' and A'BC, AB and AB') -> terms based on A, B, or C
    
    # Check for vertical pairs, quad, or octet
    if k_map_values[0] == 1 and k_map_values[1] == 1:
        expression.append("A'B'C")
    
    if k_map_values[2] == 1 and k_map_values[3] == 1:
        expression.append("A'BC")
    
    if k_map_values[4] == 1 and k_map_values[5] == 1:
        expression.append("AB'C")
    
    if k_map_values[6] == 1 and k_map_values[7] == 1:
        expression.append("ABC")
    
    # Check for groups of four or more
    if k_map_values[0] == 1 and k_map_values[1] == 1 and k_map_values[4] == 1 and k_map_values[5] == 1:
        expression.append("C'")
    
    if k_map_values[2] == 1 and k_map_values[3] == 1 and k_map_values[6] == 1 and k_map_values[7] == 1:
        expression.append("C")
    
    # If no pairs, check for single ones
    if len(expression) == 0:
        if k_map_values[0] == 1:
            expression.append("A'B'C'")
        if k_map_values[1] == 1:
            expression.append("A'B'C")
        if k_map_values[2] == 1:
            expression.append("A'BC'")
        if k_map_values[3] == 1:
            expression.append("A'BC")
        if k_map_values[4] == 1:
            expression.append("ABC'")
        if k_map_values[5] == 1:
            expression.append("ABC")
        if k_map_values[6] == 1:
            expression.append("AB'C'")
        if k_map_values[7] == 1:
            expression.append("AB'C")
    
    # Return the simplified expression
    if expression:
        simplified_expression = ' + '.join(expression)
        return f"Simplified Expression: {simplified_expression}"
    else:
        return "Simplified Expression: 0"

def main():
    # User input for minterms (0-7)
    minterms_input = input("Enter the minterms (e.g., 0, 1, 2, 3, 7): ").strip()
    
    try:
        minterms = list(map(int, minterms_input.split(',')))
        # Get the simplified Boolean expression
        simplified_expression = get_simplified_expression(minterms)
        print(simplified_expression)
    except ValueError:
        print("Invalid input! Please enter integers separated by commas.")

# Run the program
main()

'''
Line-by-Line Breakdown:

def get_simplified_expression(minterms):
Defines a function named get_simplified_expression, which takes a list of minterms as input and returns 
the simplified Boolean expression based on a 3-variable K-map.

k_map_values = [0] * 8
Initializes a list k_map_values with 8 cells, all set to 0. This represents a 3-variable K-map, 
which has 8 possible combinations (from 0 to 7).

for minterm in minterms:
Loops through each minterm in the input list minterms.

if 0 <= minterm <= 7:
Checks if the minterm is within the valid range (0 to 7). If true, it proceeds to set the corresponding K-map value.

k_map_values[minterm] = 1
Sets the K-map value for the corresponding minterm to 1.

else:
If the minterm is outside the valid range (0-7), it prints an error message.

print("Invalid minterm input! Please provide minterms between 0 and 7.")
Prints an error message if a minterm is out of the valid range.

return
Exits the function early if an invalid minterm is provided.

print("\nK-map (3 variables):")
Prints a header for the K-map output.

print(f" 00 01 11 10")
Prints the column headers for the K-map, representing different combinations of variables for the third variable C.

print(f"0 | {k_map_values[0]} | {k_map_values[1]} | {k_map_values[3]} | {k_map_values[2]}")
Prints the first row of the K-map, corresponding to A' (combinations of A = 0).

print(f"1 | {k_map_values[4]} | {k_map_values[5]} | {k_map_values[7]} | {k_map_values[6]}")
Prints the second row of the K-map, corresponding to A (combinations of A = 1).

expression = []
Initializes an empty list expression to hold the simplified Boolean terms.

if k_map_values[0] == 1 and k_map_values[1] == 1:
Checks if both k_map_values[0] and k_map_values[1] are 1. If true, it adds the term A'B'C to the expression.

expression.append("A'B'C")
Appends the term A'B'C to the expression list.

if k_map_values[2] == 1 and k_map_values[3] == 1:
Checks if both k_map_values[2] and k_map_values[3] are 1. If true, it adds the term A'BC to the expression.

expression.append("A'BC")
Appends the term A'BC to the expression list.

if k_map_values[4] == 1 and k_map_values[5] == 1:
Checks if both k_map_values[4] and k_map_values[5] are 1. If true, it adds the term AB'C to the expression.

expression.append("AB'C")
Appends the term AB'C to the expression list.

if k_map_values[6] == 1 and k_map_values[7] == 1:
Checks if both k_map_values[6] and k_map_values[7] are 1. If true, it adds the term ABC to the expression.

expression.append("ABC")
Appends the term ABC to the expression list.

if k_map_values[0] == 1 and k_map_values[1] == 1 and k_map_values[4] == 1 and k_map_values[5] == 1:
Checks if the values for A'B'C' and A'B'C are both 1, and if so, adds C' to the expression.

expression.append("C'")
Appends the term C' to the expression list.

if k_map_values[2] == 1 and k_map_values[3] == 1 and k_map_values[6] == 1 and k_map_values[7] == 1:
Checks if the values for A'BC' and A'BC are both 1, and if so, adds C to the expression.

expression.append("C")
Appends the term C to the expression list.

if len(expression) == 0:
If no pairs have been found, the function checks for single ones in the K-map and adds them to the expression.

if k_map_values[0] == 1:
If k_map_values[0] is 1, appends A'B'C' to the expression.

expression.append("A'B'C'")
Appends A'B'C' to the expression list.

if k_map_values[1] == 1:
If k_map_values[1] is 1, appends A'B'C to the expression.

expression.append("A'B'C")
Appends A'B'C to the expression list.

if k_map_values[2] == 1:
If k_map_values[2] is 1, appends A'BC' to the expression.

expression.append("A'BC'")
Appends A'BC' to the expression list.

if k_map_values[3] == 1:
If k_map_values[3] is 1, appends A'BC to the expression.

expression.append("A'BC")
Appends A'BC to the expression list.

if k_map_values[4] == 1:
If k_map_values[4] is 1, appends ABC' to the expression.

expression.append("ABC'")
Appends ABC' to the expression list.

if k_map_values[5] == 1:
If k_map_values[5] is 1, appends ABC to the expression.

expression.append("ABC")
Appends ABC to the expression list.

if k_map_values[6] == 1:
If k_map_values[6] is 1, appends AB'C' to the expression.

expression.append("AB'C'")
Appends AB'C' to the expression list.

if k_map_values[7] == 1:
If k_map_values[7] is 1, appends AB'C to the expression.

expression.append("AB'C")
Appends AB'C to the expression list.

if expression:
Checks if the expression list contains any terms.

simplified_expression = ' + '.join(expression)
Joins the terms in the expression list with + to create a simplified Boolean expression.

return f"Simplified Expression: {simplified_expression}"
Returns the simplified Boolean expression as a string.

else:
If the expression list is empty, meaning no terms were added, returns "0" as the simplified expression.

return "Simplified Expression: 0"
Returns "0" if no simplification was possible.

def main():
Defines the main function, which handles user input and invokes the get_simplified_expression function.

minterms_input = input("Enter the minterms (e.g., 0, 1, 2, 3, 7): ").strip()
Prompts the user to enter minterms, trims any spaces, and stores the input in minterms_input.

minterms = list(map(int, minterms_input.split(',')))
Splits the input string by commas, converts each part to an integer, and stores the result in minterms.

simplified_expression = get_simplified_expression(minterms)
Calls the get_simplified_expression function with the minterms list and stores the result in simplified_expression.

print(simplified_expression)
Prints the simplified Boolean expression.

except ValueError:
Handles any errors that occur when converting input to integers.

print("Invalid input! Please enter integers separated by commas.")
Prints an error message if the user enters invalid input.

main()
Calls the main function to start the program.
'''