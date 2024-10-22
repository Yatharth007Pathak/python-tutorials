def factorial(n):
    if(n == 0 or n == 1):  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
    
print(factorial(6))
print(factorial(5))
print(factorial(4))

'''
Basic Recursive Function:- A recursive function must have a base case to prevent infinite recursion, 
and it must call itself with a modified argument.
'''


"""
When factorial(5) is called, it follows these steps:

factorial(5) calls factorial(4)
factorial(4) calls factorial(3)
factorial(3) calls factorial(2)
factorial(2) calls factorial(1)
factorial(1) calls factorial(0)
factorial(0) returns 1 (base case)
factorial(1) returns 1 * 1 = 1
factorial(2) returns 2 * 1 = 2
factorial(3) returns 3 * 2 = 6
factorial(4) returns 4 * 6 = 24
factorial(5) returns 5 * 24 = 120
"""