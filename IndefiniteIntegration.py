# Indefinite integration of a polynomial function

# Importing the sympy library, which is used for symbolic mathematics in Python
import sympy as sp

# Defining a symbol 'x' that will be used as a variable in the mathematical expression
x = sp.Symbol('x')

# Defining the function f(x) = x^2 + 3x + 2
f = x**2 + 3*x + 2

# Calculating the indefinite integral of the function f with respect to x
F = sp.integrate(f, x)

# Printing the result of the integral
print("∫f(x) dx =", F)

'''
The sympy library in Python is a powerful tool for symbolic mathematics. 
It allows you to perform algebraic operations, calculus, equation solving, 
matrix manipulations, and other mathematical computations symbolically (meaning it works with symbols rather than numerical values)
'''


'''
Here's a line-by-line breakdown of the code:

1. import sympy as sp
This line imports the sympy library, a Python library for symbolic mathematics, under the alias sp.
sympy provides functionalities for algebraic manipulation, calculus, equation solving, and more.

2. x = sp.Symbol('x')
This line defines a symbolic variable x using sp.Symbol().
In symbolic computation, variables are treated as mathematical symbols rather than regular numbers or data types.

3. f = x**2 + 3*x + 2
This line defines a symbolic expression f, which represents the quadratic function f(x) = x^2 + 3x + 2.
The ** operator is used to indicate exponentiation (e.g., x**2 is x^2).

4. F = sp.integrate(f, x)
This line computes the indefinite integral of the function f with respect to the variable x using sp.integrate().
The result is stored in the variable F.
In this case, it computes the integral ∫(x^2 + 3x + 2) dx.

5. print("∫f(x) dx =", F)
This line prints the result of the integral to the console.
The print() function outputs the text "∫f(x) dx =" followed by the value of F (the integral of the function).

The program essentially calculates and prints the indefinite integral of f(x) = x^2 + 3x + 2.
'''