a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (elements in either set)
union_set = a.union(b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (elements in both sets)
intersection_set = a.intersection(b)
print(intersection_set)  # Output: {3, 4}

# Difference (elements in set a but not in set b)
difference_set = a.difference(b)
print(difference_set)  # Output: {1, 2}

# Difference (elements in set b but not in set a)
difference_set = b.difference(a)
print(difference_set)  # Output: {5, 6}

# Symmetric Difference (elements in either set, but not in both)
symmetric_difference_set = a.symmetric_difference(b)
print(symmetric_difference_set)  # Output: {1, 2, 5, 6}



# Set Operations:- Sets support various mathematical operations.