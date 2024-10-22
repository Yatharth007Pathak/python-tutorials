def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci_iterative(10))


# Iterative Fibonacci

'''
Converting Recursion to Iteration
Sometimes, recursive solutions can be converted to iterative ones to improve performance and avoid stack overflow.
'''