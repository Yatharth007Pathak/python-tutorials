'''
K-map Format for 4 Variables (A, B, C, D):
We will label the 16 cells of the K-map as follows:

       00   01   11   10
00  |  m0   m1   m3   m2
01  |  m4   m5   m7   m6
11  |  m12  m13  m15  m14
10  |  m8   m9   m11  m10

Each minterm corresponds to a combination of the values of A, B, C, and D. For example:
m0 corresponds to A'B'C'D'
m1 corresponds to A'B'C'D
m2 corresponds to A'B'CD'
m3 corresponds to A'B'CD
.... and so on for all 16 minterms.

Simplification Logic:
The simplified expression should be in terms of A, B, C, and D. Here's how to proceed:
Pairs: A pair is a group of two adjacent 1s. This can simplify to one variable being constant while the other varies.
Quads: A quad is a group of four adjacent 1s. This can simplify to two variables being constant.
Octets: An octet is a group of eight adjacent 1s. This can simplify to three variables being constant.
'''

def get_simplified_expression(minterms):
    # 4-variable K-map (4x4 grid for A, B, C, D)
    k_map_values = [0] * 16  # 16 cells for a 4-variable K-map
    
    # Mark the minterms with 1 in the K-map
    for minterm in minterms:
        if 0 <= minterm <= 15:
            k_map_values[minterm] = 1
        else:
            print("Invalid minterm input! Please provide minterms between 0 and 15.")
            return
    
    # Output the K-map grid
    print("\nK-map (4 variables):")
    for i in range(4):
        print(f"   {' '.join(map(str, k_map_values[i*4:(i+1)*4]))}")
    
    # Simplify the Boolean expression from the K-map
    expression = []
    
    # Check for quads and octets
    # Horizontal quads
    if k_map_values[0] == 1 and k_map_values[1] == 1 and k_map_values[4] == 1 and k_map_values[5] == 1:
        expression.append("A'B'")

    if k_map_values[2] == 1 and k_map_values[3] == 1 and k_map_values[6] == 1 and k_map_values[7] == 1:
        expression.append("A'B")

    if k_map_values[8] == 1 and k_map_values[9] == 1 and k_map_values[12] == 1 and k_map_values[13] == 1:
        expression.append("AB'")

    if k_map_values[10] == 1 and k_map_values[11] == 1 and k_map_values[14] == 1 and k_map_values[15] == 1:
        expression.append("AB")
    
    # Check for vertical pairs
    if k_map_values[0] == 1 and k_map_values[4] == 1:
        expression.append("A'C'D'")

    if k_map_values[1] == 1 and k_map_values[5] == 1:
        expression.append("A'C'D")

    if k_map_values[2] == 1 and k_map_values[6] == 1:
        expression.append("A'CD'")

    if k_map_values[3] == 1 and k_map_values[7] == 1:
        expression.append("A'CD")

    if k_map_values[8] == 1 and k_map_values[12] == 1:
        expression.append("AC'D'")

    if k_map_values[9] == 1 and k_map_values[13] == 1:
        expression.append("AC'D")

    if k_map_values[10] == 1 and k_map_values[14] == 1:
        expression.append("ACD'")

    if k_map_values[11] == 1 and k_map_values[15] == 1:
        expression.append("ACD")
    
    # Check for individual minterms if no pairs or quads found
    if len(expression) == 0:
        for i in range(16):
            if k_map_values[i] == 1:
                A = "A" if (i & 8) else "A'"
                B = "B" if (i & 4) else "B'"
                C = "C" if (i & 2) else "C'"
                D = "D" if (i & 1) else "D'"
                expression.append(f"{A}{B}{C}{D}")
    
    # Return the simplified expression
    if expression:
        simplified_expression = ' + '.join(expression)
        return f"Simplified Expression: {simplified_expression}"
    else:
        return "Simplified Expression: 0"

def main():
    # User input for minterms (0-15)
    minterms_input = input("Enter the minterms (e.g., 0, 1, 2, 3, 15): ").strip()
    
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

Explanation of the Code:

def get_simplified_expression(minterms):
This function simplifies a Boolean expression based on a 4-variable K-map. 
It accepts a list of minterms (integers between 0 and 15) and returns the simplified Boolean expression.

k_map_values = [0] * 16
Initializes a list k_map_values with 16 elements, all set to 0. 
This list represents the cells of a 4-variable K-map (with 16 possible combinations of four variables A, B, C, and D).

for minterm in minterms:
Iterates over the provided minterms list.

if 0 <= minterm <= 15:
Checks if the minterm is valid (between 0 and 15). If valid, it sets the corresponding K-map value to 1.

k_map_values[minterm] = 1
Sets the cell at the given minterm index to 1, marking that position on the K-map.

else:
If an invalid minterm is provided, it prints an error message and returns from the function.

print("\nK-map (4 variables):")
Prints the header for the K-map.

for i in range(4):
Loops through the K-map rows (4 rows for 16 cells).

print(f" {' '.join(map(str, k_map_values[i*4:(i+1)*4]))}")
Prints each row of the K-map, formatting it as a space-separated string of 1s and 0s.

expression = []
Initializes an empty list expression to store the simplified Boolean terms.

Check for horizontal quads (each check corresponds to finding 4 adjacent cells with 1s in the K-map):
if k_map_values[0] == 1 and k_map_values[1] == 1 and k_map_values[4] == 1 and k_map_values[5] == 1:
This checks for a horizontal quad in the top-left corner and appends the corresponding simplified expression (A'B').
Similar checks are performed for other horizontal quads at positions (2-3), (8-9), and (10-11).

Check for vertical pairs (each check corresponds to finding 2 vertically adjacent cells with 1s):
if k_map_values[0] == 1 and k_map_values[4] == 1:
This checks for a vertical pair in the leftmost column and appends the corresponding simplified expression (A'C'D').
Similar checks are performed for other vertical pairs in columns.

Check for individual minterms:
If no pairs or quads are found, this section iterates over all 16 cells and 
appends the corresponding minterm expression (like A'BCD', AB'C', etc.) for each cell where k_map_values[i] is 1.

if expression:
Checks if any expressions were added to the expression list.

simplified_expression = ' + '.join(expression)
Joins the expressions in the expression list with + to form the final simplified Boolean expression.

return f"Simplified Expression: {simplified_expression}"
Returns the final simplified Boolean expression as a string.

else:
If no expressions were found (i.e., the K-map contains no 1s), it returns "Simplified Expression: 0".

def main():
Defines the main function where user input is handled.

minterms_input = input("Enter the minterms (e.g., 0, 1, 2, 3, 15): ").strip()
Prompts the user to input the minterms as a comma-separated string, then removes any leading/trailing spaces.

minterms = list(map(int, minterms_input.split(',')))
Converts the comma-separated input into a list of integers (minterms).

simplified_expression = get_simplified_expression(minterms)
Calls the get_simplified_expression function to compute the simplified Boolean expression.

print(simplified_expression)
Prints the simplified Boolean expression.

except ValueError:
Handles cases where the input cannot be converted into integers (e.g., if the user enters non-numeric values).

print("Invalid input! Please enter integers separated by commas.")
Prints an error message if the input is invalid.

main()
Calls the main() function to start the program.
'''