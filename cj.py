numbers = [1, 2, 3, 4, 5]

# Get the first three elements
print(numbers[:3])       # Output: [1, 2, 3]

# Get elements from index 2 to the end
print(numbers[2:])       # Output: [3, 4, 5]

# Get elements from index 1 to 3 (excluding 3)
print(numbers[1:3])      # Output: [2, 3]

# Get elements from 3rd last index to 2nd last index 
print(numbers[-3:-1])    # Output; [3,4]


# Slicing Lists:- We can slice lists to access a range of elements
# list_name[starting_index:ending_index]           ending_index is not included