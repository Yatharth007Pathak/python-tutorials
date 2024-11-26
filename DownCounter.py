# Simulating a 4-bit Down Counter

import time

def four_bit_down_counter():
    # The range for a 4-bit counter (15 to 0)
    max_count = 16  # 2^4 = 16
    
    print("4-bit Down Counter:")
    print("-" * 20)
    
    # Start from 15 and decrement to 0
    for count in range(max_count-1, -1, -1):
        # Convert the count to a 4-bit binary string
        binary_value = format(count, '04b')  # '04b' ensures 4-bit binary representation
        print(f"Decimal: {count} | Binary: {binary_value}")
        
        time.sleep(1)  # Simulate time delay for the counter

if __name__ == "__main__":
    four_bit_down_counter()

'''
Here's a detailed, line-by-line breakdown of the code for the 4-bit Down Counter:

import time
The time module is imported to use the sleep function for creating delays in the program execution.

def four_bit_down_counter():
Defines a function named four_bit_down_counter to simulate a 4-bit down counter.

max_count = 16
Defines the maximum count for the 4-bit counter. A 4-bit counter can represent numbers from 0 to 15 (inclusive), so the range is 16 (2^4 = 16).

print("4-bit Down Counter:")
Prints a title to indicate the start of the counter simulation.

print("-" * 20)
Prints a line of dashes (--------------------) for better separation and readability.

for count in range(max_count-1, -1, -1):
Initiates a loop that starts at 15 (one less than max_count), decrements by 1 in each iteration, and stops at 0 (inclusive). 
The range(start, stop, step) function defines this countdown.

binary_value = format(count, '04b')
Converts the current decimal value (count) into a binary string representation. 
The format specifier '04b' ensures that the binary string is always 4 bits long, adding leading zeros as necessary.

print(f"Decimal: {count} | Binary: {binary_value}")
Prints the current decimal value and its corresponding 4-bit binary representation, displaying both formats side-by-side.

time.sleep(1)
Pauses the program for 1 second before moving to the next iteration, simulating the delay seen in real hardware counters.

if __name__ == "__main__":
Ensures that the code block below it is executed only when the script is run directly and not imported as a module.

four_bit_down_counter()
Calls the four_bit_down_counter function to start the simulation of the 4-bit down counter.
'''