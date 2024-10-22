# Definite integration of a polynomial function

# Importing the sympy library for symbolic mathematics in Python
import sympy as sp

# Defining a symbol 'x' that will be used as the variable in the mathematical expression
x = sp.Symbol('x')

# Taking user input for a function in terms of 'x' as a string
f = input("Enter the function (in terms of x):")

# Calculating the indefinite integral of the function 'f' with respect to 'x'
F_indefinite = sp.integrate(f, x)

# Printing the result of the indefinite integral
print("Indefinite integral ∫f(x) dx =", F_indefinite)

# Asking the user to input the lower and upper limits for the definite integral
a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))

# Calculating the definite integral of 'f' with respect to 'x' from the lower limit 'a' to the upper limit 'b'
F_definite = sp.integrate(f, (x, a, b))

# Printing the result of the definite integral
print(f"Definite integral ∫f(x) dx from {a} to {b} =", F_definite)


'''
Here's a line-by-line breakdown of the code for both indefinite and definite integrals:

1. import sympy as sp
This imports the sympy library and gives it the alias sp.
Sympy is used for symbolic mathematics, such as algebraic expressions and calculus operations.

2. x = sp.Symbol('x')
This defines x as a symbolic variable that will be used in the function entered by the user. 
It treats x as a mathematical symbol rather than a regular Python variable.

3. f = input("Enter the function (in terms of x):")
This takes input from the user for the function f, which should be a mathematical expression involving the variable x.
For example, the user could input x**2 + 3*x + 2.

4. F_indefinite = sp.integrate(f, x)
This calculates the indefinite integral of the function f with respect to x.
The indefinite integral is an antiderivative of f, and it includes a constant of integration (though not explicitly shown by sympy).

5. print("Indefinite integral ∫f(x) dx =", F_indefinite)
This prints the result of the indefinite integral calculation to the console.
For example, if f = x**2, this will print something like Indefinite integral ∫f(x) dx = x**3 / 3.

6. a = float(input("Enter the lower limit of integration: "))
This prompts the user to input the lower limit (a) for the definite integral and converts it into a floating-point number.

7. b = float(input("Enter the upper limit of integration: "))
This prompts the user to input the upper limit (b) for the definite integral and converts it into a floating-point number.

8. F_definite = sp.integrate(f, (x, a, b))
This calculates the definite integral of the function f over the interval [a,b].
The definite integral gives the net area under the curve of f(x) between the limits a and b.

9. print("Definite integral ∫f(x) dx from {a} to {b} =", F_definite)
This prints the result of the definite integral calculation.
The string {a} and {b} will be replaced by the values of a and b, showing the limits of integration.

Example Output:
If the user enters x**2 as the function, 0 as the lower limit, and 1 as the upper limit, the output will look like:
Indefinite integral ∫f(x) dx = x**3/3
Definite integral ∫f(x) dx from 0.0 to 1.0 = 1/3

In summary, this program calculates and displays both the indefinite and definite integrals of a function provided by the user.
'''