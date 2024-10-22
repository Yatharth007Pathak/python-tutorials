a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# Subset (a is a subset of b)
print(a.issubset(b))  # Output: True

# Superset (b is a superset of a)
print(b.issuperset(a))  # Output: True

# Disjoint (no common elements)
c = {6, 7, 8}
print(a.isdisjoint(c))  # Output: True



# Set Comparisons:- We can compare sets using comparison operators.