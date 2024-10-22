try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError as ve:
    print(f"ValueError: {ve}")
except ZeroDivisionError as zde:
    print(f"ZeroDivisionError: {zde}")
else:
    print(f"The result is {result}")
finally:
    print("This will always execute")


# In this example:

# The try block contains code that could potentially raise exceptions.
# The except blocks handle specific exceptions (ValueError and ZeroDivisionError).
# The else block runs if no exceptions occur.
# The finally block runs no matter what, whether an exception is raised or not.

'''
The try keyword in Python is used to handle exceptions (errors) that occur during the execution of a program. 
It allows us to test a block of code for errors, and then handle the error gracefully if one occurs.

The except keyword in Python is used to catch and handle exceptions that occur within a try block. 
It allows us to specify what should happen when an exception of a specific type is raised.
We can have multiple except blocks to handle different types of exceptions
'''

"""
Here's the basic syntax of the try and except:

try:
    # code that might raise an exception
    risky_code()
except SomeException as e:
    # code that runs if the exception occurs
    handle_exception(e)
else:
    # code that runs if no exception occurs
    handle_success()
finally:
    # code that runs no matter what
    cleanup()
"""