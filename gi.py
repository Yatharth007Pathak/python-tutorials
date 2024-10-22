def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)



'''
Recursion is a programming technique where a function calls itself in order to solve a problem. 
In Python, recursion can be a powerful tool for solving problems that can be broken down into smaller, similar subproblems.
Recursion is when a function calls itself repeatedly

Advantages:
Simplicity: Recursive solutions are often simpler and more elegant.
Readability: Code can be more readable when using recursion for problems naturally defined in terms of smaller subproblems.

Disadvantages:
Performance: Recursive solutions can be less efficient due to the overhead of multiple function calls 
and the possibility of deep recursion leading to stack overflow.
Memory: Each function call consumes stack space, which can be problematic for large inputs.
'''