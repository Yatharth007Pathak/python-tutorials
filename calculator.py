import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return
        
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operation = tk.Label(root, text="Choose operation (+, -, *, /):")
label_operation.pack()

operation_var = tk.StringVar(root)
entry_operation = tk.Entry(root, textvariable=operation_var)
entry_operation.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Result:")
label_result.pack()

# Run the main loop
root.mainloop()

'''
Here's a pointwise breakdown of the code:

import tkinter as tk
Import the Tkinter module and refer to it as tk to create GUI applications in Python.

from tkinter import messagebox
Import messagebox from Tkinter for showing pop-up dialogs like errors or warnings.

def calculate():
Define the calculate() function, which performs basic arithmetic operations.

try:
Start a try block to handle any potential errors when getting user input.

num1 = float(entry_num1.get())
Get the value from entry_num1 and convert it to a float. This is the first number for the calculation.

num2 = float(entry_num2.get())
Get the value from entry_num2 and convert it to a float. This is the second number for the calculation.

operation = operation_var.get()
Get the value from operation_var, which contains the arithmetic operation (+, -, *, /).

if operation == '+':
Check if the operation is addition.

result = num1 + num2
If it's addition, calculate the sum and assign it to result.

elif operation == '-':
Check if the operation is subtraction.

result = num1 - num2
If it's subtraction, calculate the difference and assign it to result.

elif operation == '*':
Check if the operation is multiplication.

result = num1 * num2
If it's multiplication, calculate the product and assign it to result.

elif operation == '/':
Check if the operation is division.

if num2 != 0:
If the second number is not zero, proceed to the next line.

result = num1 / num2
Perform division and assign the result to result.

else:
If the second number is zero, proceed to the next line.

messagebox.showerror("Error", "Cannot divide by zero")
Show an error message indicating that division by zero is not allowed.

return
Exit the calculate() function without performing any further actions.

else:
If the operation is not one of the four supported ones, proceed to the next line.

messagebox.showerror("Error", "Invalid operation")
Show an error message indicating that the entered operation is invalid.

return
Exit the calculate() function.

label_result.config(text=f"Result: {result}")
Update the label_result to display the result of the calculation.

except ValueError:
Catch a ValueError if either of the numbers entered is not a valid float.

messagebox.showerror("Error", "Invalid input")
Show an error message indicating that the input is invalid.

root = tk.Tk()
Create the main application window and assign it to root.

root.title("Simple Calculator")
Set the title of the main window to "Simple Calculator".

label_num1 = tk.Label(root, text="Enter first number:")
Create a label prompting the user to enter the first number.

label_num1.pack()
Pack (place) the label in the window.

Entry_num1 = tk.Entry(root)
Create an entry widget to allow the user to input the first number.

entry_num1.pack()
Pack the entry widget in the window.

label_num2 = tk.Label(root, text="Enter second number:")
Create a label prompting the user to enter the second number.

label_num2.pack()
Pack the label in the window.

entry_num2 = tk.Entry(root)
Create an entry widget to allow the user to input the second number.

entry_num2.pack()
Pack the entry widget in the window.

label_operation = tk.Label(root, text="Choose operation (+, -, *, /):")
Create a label prompting the user to choose an arithmetic operation.

label_operation.pack()
Pack the label in the window.

operation_var = tk.StringVar(root)
Create a StringVar to store the operation selected by the user.

entry_operation = tk.Entry(root, textvariable=operation_var)
Create an entry widget that allows the user to input the desired operation, linked to operation_var.

entry_operation.pack()
Pack the entry widget in the window.

button_calculate = tk.Button(root, text="Calculate", command=calculate)
Create a button labeled "Calculate" that calls the calculate() function when clicked.

button_calculate.pack()
Pack the button in the window.

label_result = tk.Label(root, text="Result:")
Create a label to display the result of the calculation.

label_result.pack()
Pack the label in the window.

root.mainloop()
Start the Tkinter event loop, which keeps the application running and responsive.
'''