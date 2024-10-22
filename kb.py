def remove_occurrences(lst, value_to_remove):
    # Create a new list with all elements except the ones to remove
    return [element for element in lst if element != value_to_remove]

# Example usage
original_list = [1, 2, 3, 4, 2, 5, 2, 6]
element_to_remove = 2

# Remove all occurrences of element_to_remove
new_list = remove_occurrences(original_list, element_to_remove)

print("Original list:", original_list)
print("List after removing occurrences of", element_to_remove, ":", new_list)

# python program to remove multiple occurrences of an element from a list by using any list function

'''
return [element for element in lst if element != value_to_remove]
Here's a breakdown of what this line does:

List Comprehension: The expression [element for element in lst if element != value_to_remove] is a list comprehension. 
List comprehensions provide a concise way to create lists.

Iteration: for element in lst iterates over each element in the original list lst.

Condition: if element != value_to_remove is a conditional check that filters elements. 
It includes only those element values that are not equal to value_to_remove.

Resulting List: For every element in lst, the list comprehension adds that element to the new list only if it does not match value_to_remove. 
This results in a new list containing all the original elements except the ones that match value_to_remove.
'''