# Creating a frozenset
frozen_numbers = frozenset([1, 2, 3, 4, 5])
print(frozen_numbers)  # Output: frozenset({1, 2, 3, 4, 5})

# Frozenset operations
print(frozen_numbers.union({6, 7}))  # Output: frozenset({1, 2, 3, 4, 5, 6, 7})
print(frozen_numbers.intersection({3, 4, 5}))  # Output: frozenset({3, 4, 5})



# Frozensets:- Frozensets are immutable sets. We cannot modify them after creation, but we can perform all other set operations.