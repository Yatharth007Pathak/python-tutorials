# Calculate derivative of polynomial function

# Importing the sympy library for symbolic mathematics
import sympy as sp

# Defining a symbol 'x' to be used as the variable in the function
x = sp.Symbol('x')

# Defining the function f(x) = x^4 + 4x^2 + 5x - 6
f = x**4 + 4*x**2 + 5*x - 6

# Creating the derivative of the function f with respect to x (without evaluating)
sp.Derivative(f, x)

# Creating and evaluating the derivative of f with respect to x
sp.Derivative(f, x, evaluate=True)

# A more concise way to compute the derivative using diff() method
f.diff(x)

# Converting the symbolic expression f and its derivative into callable functions
# expr is the callable form of f(x)
expr = sp.lambdify(x, f)

# expr_der is the callable form of the derivative f'(x)
expr_der = sp.lambdify(x, f.diff(x))

# Evaluating and printing the value of the function f at x = 5
print("f' value of function at x=5:", {expr(5)})

# Evaluating and printing the value of the derivative f'(x) at x = 5
print("f' derivative of function at x=5:", {expr_der(5)})


'''
Here's a line-by-line breakdown of this code, which focuses on calculating derivatives and 
evaluating the function and its derivative at a specific value:

1. import sympy as sp
This imports the sympy library under the alias sp.
SymPy is useful for performing symbolic mathematics, including derivatives, integrals, and equation solving.

2. x = sp.Symbol('x')
This defines x as a symbolic variable, allowing it to be treated as a mathematical symbol in further operations.

3. f = x**4 + 4*x**2 + 5*x - 6
This defines a polynomial function f(x) as f(x) = x^4 + 4x^2 + 5x - 6.

4. sp.Derivative(f, x)
This creates a symbolic representation of the first derivative of f(x) with respect to x.
However, it doesn't evaluate or print the derivative—it's just an unevaluated expression at this stage.

5. sp.Derivative(f, x, evaluate=True)
This computes the first derivative of the function f(x) with respect to x, but the result is not assigned to any variable or printed.
By setting evaluate=True, SymPy actually computes the derivative.

6. f.diff(x)
This is another way of calculating the derivative of f(x) with respect to x, which is equivalent to sp.Derivative(f, x, evaluate=True).
The result is f'(x) = 4x^3 + 8x + 5.

7. expr = sp.lambdify(x, f)
This line creates a numerical function from the symbolic expression f(x) using sp.lambdify().
lambdify turns a symbolic expression into a function that can be evaluated for specific numerical values of x.

8. expr_der = sp.lambdify(x, f.diff(x))
This creates a numerical function from the derivative of f(x) using sp.lambdify().
f.diff(x) is the symbolic derivative, and sp.lambdify(x, f.diff(x)) converts it into a function for numerical evaluation.

9. print("f' value of function at x=5:", {expr(5)})
This prints the value of the original function f(x) at x = 5.
The function expr(5) evaluates the original polynomial f(x) at x = 5.

10. print("f' derivative of function at x=5:", {expr_der(5)})
This prints the value of the derivative f'(x) at x = 5.
The function expr_der(5) evaluates the derivative of f(x) at x=5.

Example Output:
If we substitute x=5 in the function and its derivative:
f(5) = 5^4 +4(5)^2 + 5(5) - 6 = 625 + 100 + 25 - 6 = 744
f'(5) = 4(5)^3 + 8(5) + 5 = 4(125) + 40 + 5 = 545

The output would be:
f' value of function at x=5: 744
f' derivative of function at x=5: 545

In summary, this code computes the derivative of a polynomial, creates numerical functions 
for both the original function and its derivative, and then evaluates both at x=5.
'''