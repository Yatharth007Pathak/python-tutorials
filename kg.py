# Function to read a sequence of integers from the user and return as a list
def read_sequence():
    sequence = input("Enter numbers separated by spaces: ")
    return [int(x) for x in sequence.split()]

# Read two lists of integers from the user
list1 = read_sequence()
list2 = read_sequence()

# Merge the two lists
merged_list = list1 + list2

# Sort the merged list in ascending order
ascending_order = sorted(merged_list)

# Sort the merged list in descending order
descending_order = sorted(merged_list, reverse=True)

# Display the results
print("Merged list in ascending order:", ascending_order)
print("Merged list in descending order:", descending_order)

# Python program that reads two sequences of integers from the user, assigns them to two lists, and then merges both lists in ascending and descending order