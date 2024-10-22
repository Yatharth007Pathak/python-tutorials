def find_occurrences(lst, element):
    indices = []
    for i in range(len(lst)):
        if lst[i] == element:
            indices.append(i)
    return indices

# Example usage
my_list = [1, 3, 7, 8, 7, 5, 6, 7, 3, 7]
element_to_find = 7

result = find_occurrences(my_list, element_to_find)
print(f"Element {element_to_find} occurs at indices: {result}")

# Python program to find and display the index values of all occurrences of a specific element in a list