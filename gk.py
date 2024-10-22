def greet(name):
    return f"Hello, {name}!"

def main():
    name = "Alice"
    message = greet(name)
    print(message)

main()



'''
The call stack in Python is a fundamental part of how the Python interpreter keeps track of function calls. 
When a function is called, the following steps occur involving the call stack:

Function Call: When a function is called, Python adds a new frame to the call stack. 
This frame contains information about the function, including its parameters, local variables, 
and the instruction pointer that keeps track of the function's execution.

Execution: The function's code is executed within its frame. 
If the function calls another function, a new frame for the called function is pushed onto the call stack.

Nested Calls: This process can continue with multiple nested function calls, 
each adding a new frame to the top of the call stack. The stack grows as functions call other functions.

Returning from a Function: When a function completes its execution and returns a value, 
its frame is popped from the call stack, and control is returned to the frame below it (the calling function).

Handling Recursion: In the case of recursion, each recursive call creates a new frame, 
and the stack depth increases with each recursive call. If the recursion is too deep, 
Python raises a RecursionError when the call stack exceeds the maximum limit (typically 1000 frames).

Importance of Call Stack
The call stack is crucial for:

Function Call Management: Keeping track of function calls and returns.
Local Scope Management: Isolating local variables of functions.
Debugging: Providing a traceback when an exception occurs, showing the sequence of function calls leading to the error.
'''