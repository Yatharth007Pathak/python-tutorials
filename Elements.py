# element information using python

import periodictable

def get_element_info(symbol):
    if not periodictable.elements.symbol(symbol):
        print("Invalid element symbol.")
        return
    element = periodictable.elements.symbol(symbol)
    print(f"Element: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic Number: {element.number}")
    print(f"Atomic Weight: {element.mass}")
    print(f"Density: {element.density}")

element_symbol = input("Enter the symbol of the element: ")
get_element_info(element_symbol)

'''
Here's a breakdown of the code that uses the periodictable library to retrieve information about an element based on its symbol:

import periodictable
Importing Periodictable Module: This imports the periodictable library, which contains information about all elements in the periodic table, 
including their symbols, names, atomic numbers, atomic weights, and more.

def get_element_info(symbol):
Defining Function get_element_info: This function takes a single parameter symbol which is expected to be the chemical symbol 
of an element (like 'H' for hydrogen, 'O' for oxygen, etc.).

if not periodictable.elements.symbol(symbol):
    print("Invalid element symbol.")
    return
Checking for Valid Symbol: This checks whether the symbol provided by the user exists in the periodictable library. 
If the symbol is invalid or not found, it prints a message "Invalid element symbol." and exits the function using return.

element = periodictable.elements.symbol(symbol)
Fetching Element Info: This retrieves the element from the periodictable using the symbol provided by the user. 
It stores the element's information in the element variable.

print(f"Element: {element.name}")
print(f"Symbol: {element.symbol}")
print(f"Atomic Number: {element.number}")
print(f"Atomic Weight: {element.mass}")
print(f"Density: {element.density}")
Printing Element Details: The function prints various details about the element:
Element Name: The name of the element (e.g., Hydrogen).
Symbol: The symbol of the element (e.g., H).
Atomic Number: The atomic number (e.g., 1 for hydrogen).
Atomic Weight: The atomic mass of the element.
Density: The density of the element, if available in the dataset. 
(Note that some elements may not have density information available in the periodictable library.)

element_symbol = input("Enter the symbol of the element: ")
User Input: This line prompts the user to enter the symbol of the element they want to look up. 
The input is stored in the variable element_symbol.

get_element_info(element_symbol)
Calling the Function: This calls the get_element_info function with the user-provided element_symbol to print out the element's details.
'''