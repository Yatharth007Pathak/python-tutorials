def get_simplified_expression(minterms):

    # A K-map (Karnaugh map) is a way of simplifying Boolean expressions. 
    # The 2-variable K-map consists of 4 cells (representing the 4 possible combinations of 2 binary variables). 
    # K-map representation for 2 variables (A, B)
    # K-map is a 2x2 grid:
    # A'B' | A'B
    # AB   | AB'
    # Indices: 0, 1, 3, 2 correspond to minterms A'B', A'B, AB, AB'
    
    # Initialize the K-map with 0s (4 cells for 2 variables)
    k_map_values = [0, 0, 0, 0]
    
    # Mark the minterms with 1 in the K-map
    for minterm in minterms:
        if 0 <= minterm <= 3:
            k_map_values[minterm] = 1
        else:
            print("Invalid minterm input! Please provide minterms between 0 and 3.")
            return
    
    # Output the K-map grid
    print("\nK-map (2 variables):")
    print(f"  {k_map_values[0]}  |  {k_map_values[1]}")
    print(f"-----|-----")
    print(f"  {k_map_values[3]}  |  {k_map_values[2]}")

    # Simplify the Boolean expression from the K-map
    expression = []
    
    # Check for pairs (horizontal and vertical)
    # Horizontal pairs (A'B' and A'B, AB and AB') -> A'
    if k_map_values[0] == 1 and k_map_values[1] == 1:
        expression.append("A'")
    
    if k_map_values[2] == 1 and k_map_values[3] == 1:
        expression.append("A")
    
    # Vertical pairs (A'B' and AB', A'B and AB) -> B'
    if k_map_values[0] == 1 and k_map_values[3] == 1:
        expression.append("B'")
    
    if k_map_values[1] == 1 and k_map_values[2] == 1:
        expression.append("B")
    
    # If no pairs, check for single ones (isolated 1's)
    if len(expression) == 0:
        if k_map_values[0] == 1:
            expression.append("A'B'")
        if k_map_values[1] == 1:
            expression.append("A'B")
        if k_map_values[2] == 1:
            expression.append("AB")
        if k_map_values[3] == 1:
            expression.append("AB'")
    
    # Return the simplified expression
    if expression:
        simplified_expression = ' + '.join(expression)
        return f"Simplified Expression: {simplified_expression}"
    else:
        return "Simplified Expression: 0"

def main():
    # User input for minterms (0, 1, 2, 3)
    minterms_input = input("Enter the minterms (e.g., 0, 1, 2, 3): ").strip()
    
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
Defines a function named get_simplified_expression that takes a list of minterms and returns the simplified Boolean expression.

k_map_values = [0, 0, 0, 0]
Initializes a list k_map_values to represent the K-map values for a 2-variable Boolean function. All values are initially set to 0.

for minterm in minterms:
Loops over each minterm in the minterms list.

if 0 <= minterm <= 3:
Checks if the minterm is within the valid range (0 to 3). If true, it proceeds to set the appropriate K-map value.

k_map_values[minterm] = 1
Sets the corresponding value in k_map_values to 1 for the given minterm.

else:
If a minterm is not in the valid range, the program prints an error message and exits the function.

print("Invalid minterm input! Please provide minterms between 0 and 3.")
Informs the user that the input minterms are invalid.

return
Exits the function early if an invalid minterm is encountered.

print("\nK-map (2 variables):")
Prints a header for the K-map display.

print(f" {k_map_values[0]} | {k_map_values[1]}")
Prints the first row of the K-map with the values of k_map_values[0] and k_map_values[1].

print(f"-----|-----")
Prints a separator line between the rows of the K-map.

print(f" {k_map_values[3]} | {k_map_values[2]}")
Prints the second row of the K-map with the values of k_map_values[3] and k_map_values[2].

expression = []
Initializes an empty list expression to store the simplified Boolean expression.

if k_map_values[0] == 1 and k_map_values[1] == 1:
Checks if both k_map_values[0] and k_map_values[1] are 1. If true, it adds A' to the expression.

expression.append("A'")
Appends the term A' to the expression list.

if k_map_values[2] == 1 and k_map_values[3] == 1:
Checks if both k_map_values[2] and k_map_values[3] are 1. If true, it adds A to the expression.

expression.append("A")
Appends the term A to the expression list.

if k_map_values[0] == 1 and k_map_values[3] == 1:
Checks if both k_map_values[0] and k_map_values[3] are 1. If true, it adds B' to the expression.

expression.append("B'")
Appends the term B' to the expression list.

if k_map_values[1] == 1 and k_map_values[2] == 1:
Checks if both k_map_values[1] and k_map_values[2] are 1. If true, it adds B to the expression.

expression.append("B")
Appends the term B to the expression list.

if len(expression) == 0:
Checks if no terms have been added to the expression list (meaning no simplification was possible).

if k_map_values[0] == 1:
If k_map_values[0] is 1, appends the term A'B' to the expression.

expression.append("A'B'")
Appends A'B' to the expression.

if k_map_values[1] == 1:
If k_map_values[1] is 1, appends the term A'B to the expression.

expression.append("A'B")
Appends A'B to the expression.

if k_map_values[2] == 1:
If k_map_values[2] is 1, appends the term AB to the expression.

expression.append("AB")
Appends AB to the expression.

if k_map_values[3] == 1:
If k_map_values[3] is 1, appends the term AB' to the expression.

expression.append("AB'")
Appends AB' to the expression.

if expression:
Checks if the expression list contains any terms.

simplified_expression = ' + '.join(expression)
Joins the terms in the expression list with + to create a simplified Boolean expression.

return f"Simplified Expression: {simplified_expression}"
Returns the simplified Boolean expression as a string.

else:
If the expression list is empty (no terms were added), the function returns "0" as the simplified expression.

return "Simplified Expression: 0"
Returns "0" if no simplification was possible.

def main():
Defines the main function, which will execute the program.

minterms_input = input("Enter the minterms (e.g., 0, 1, 2, 3): ").strip()
Prompts the user to enter minterms, removes any spaces, and stores the input in minterms_input.

minterms = list(map(int, minterms_input.split(',')))
Splits the input string by commas, converts the resulting strings into integers, and stores them in the list minterms.

simplified_expression = get_simplified_expression(minterms)
Calls the get_simplified_expression function with the minterms and stores the returned simplified expression in simplified_expression.

print(simplified_expression)
Prints the simplified Boolean expression.

except ValueError:
Catches errors (e.g., invalid input that can't be converted to an integer).

print("Invalid input! Please enter integers separated by commas.")
Prints an error message if the input can't be processed as integers.

main()
Calls the main function to start the execution of the program.
'''