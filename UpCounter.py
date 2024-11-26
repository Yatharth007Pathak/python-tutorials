# Simulating a 4-bit Up Counter

import time

def four_bit_up_counter():
    # The range for a 4-bit counter (0 to 15)
    max_count = 16  # 2^4 = 16
    
    print("4-bit Up Counter:")
    print("-" * 20)
    
    for count in range(max_count):
        # Convert the count to a 4-bit binary string
        binary_value = format(count, '04b')  # '04b' ensures 4-bit binary representation
        print(f"Decimal: {count} | Binary: {binary_value}")
        
        time.sleep(1)  # Simulate time delay for the counter

if __name__ == "__main__":
    four_bit_up_counter()

'''
Here is a detailed, line-by-line breakdown of the given code:

import time
The time module is imported to use the sleep function, which introduces a delay in the program execution.

def four_bit_up_counter():
Defines a function named four_bit_up_counter to simulate a 4-bit up counter.

max_count = 16
Sets the maximum count value for the 4-bit counter. 
Since a 4-bit counter can represent numbers from 0 to 15 (inclusive), the range is 16 (2^4 = 16).

print("4-bit Up Counter:")
Prints a title message to indicate the start of the counter simulation.

print("-" * 20)
Prints a line of dashes (--------------------) to separate the title from the output for better readability.

for count in range(max_count):
Starts a loop that iterates from 0 to 15 (since range(max_count) generates numbers from 0 to max_count - 1).

binary_value = format(count, '04b')
Converts the current decimal value (count) to its binary equivalent. 
The format specifier '04b' ensures the binary number is always 4 bits long by adding leading zeros if necessary.

print(f"Decimal: {count} | Binary: {binary_value}")
Prints the current decimal value and its corresponding 4-bit binary representation.

time.sleep(1)
Pauses the program for 1 second to simulate the timing delay typically seen in hardware counters.

if __name__ == "__main__":
A special Python construct that ensures the code inside this block runs only if the script is executed directly (not imported as a module).

four_bit_up_counter()
Calls the four_bit_up_counter function to execute the counter simulation.
'''