# Defining the Function to Reverse a List
def reverse_list_with_negative_indices(input_list):
    # Create a new list with elements in reverse order using negative indices
    reversed_list = [input_list[-(i+1)] for i in range(len(input_list))]
    return reversed_list

# Example list
my_list = [10, 20, 30, 40, 50]

# Get the list in reverse order
reversed_list = reverse_list_with_negative_indices(my_list)

# Print the result
print("Original list:", my_list)
print("Reversed list:", reversed_list)

# Python program to represent the list elements in reverse order by by using negative indices

'''
 breakdown of the code

def reverse_list_with_negative_indices(input_list)::
Defines a function named reverse_list_with_negative_indices that takes a single parameter, input_list.

List Comprehension:
[input_list[-(i+1)] for i in range(len(input_list))]:
range(len(input_list)): Generates a sequence of indices from 0 to len(input_list) - 1.

input_list[-(i+1)]:
-(i+1): Calculates the negative index to access elements from the end of the list.
When i = 0, -(i+1) evaluates to -1, accessing the last element.
When i = 1, -(i+1) evaluates to -2, accessing the second-to-last element, and so on.
The list comprehension iterates over the range and collects elements from the end of the list in reverse order.

return reversed_list:
Returns the new list reversed_list which contains elements of input_list in reverse order.
'''