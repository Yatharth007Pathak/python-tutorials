# Implicit Conversion
a = 10       # int
b = 3.14     # float
c = a + b    # int is implicitly converted to float
print(c)     # Output: 13.14


# Explicit Conversion
x = "123"        # str
y = 456          # int
z = int(x) + y   # Explicitly converting str to int
print(z)         # Output: 579



'''
Type conversion is crucial in programming for several reasons:

Data compatibility: Ensures operations are performed on compatible data types.
Error prevention: Helps avoid type errors that can cause programs to crash or produce incorrect results.
Data processing: Facilitates the manipulation and processing of data in different forms.
'''