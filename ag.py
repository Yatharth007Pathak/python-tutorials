name = "Yatharth Pathak"
age = 20
price = 1000000000.00

age2 = age

print("my name is : ", name)
print("my age is : ", age)

print(age2)



'''
In the context of programming, the terms "implicit" and "explicit" are often used to describe the style 
in which a programming language handles certain operations, data types, and structures. Here’s a detailed explanation:

In implicit programming languages, many operations, data type conversions, and behaviors are automatically 
handled by the language without the programmer needing to specify them explicitly. 
This often makes the code shorter and easier to write, but it can sometimes lead to ambiguity or unexpected behavior.
Characteristics:

Type Inference: The language automatically deduces the types of variables and expressions. 
For example, you don't need to declare the type of a variable explicitly.
Automatic Memory Management: Garbage collection is typically automatic.
Convenience Functions: Many high-level functions and operations are built-in and handle common tasks without needing explicit instructions.
Dynamic Typing: Variables can hold any type of data and types are typically checked at runtime.

Examples:
Python: Python uses dynamic typing and automatic memory management, allowing for more concise code.
JavaScript: JavaScript also uses dynamic typing and automatic type conversions (type coercion).

Code Example (Python):
x = 10  # Implicitly an integer
y = "Hello"  # Implicitly a string
z = x + 5  # Type inference allows operations without explicit type declaration


Explicit programming languages require the programmer to specify many details about the operations, data types, and structures. 
This can lead to more verbose code but often provides greater control, predictability, and efficiency.

Characteristics:
Type Declaration: Types of variables and functions must be explicitly declared.
Manual Memory Management: The programmer may need to manage memory allocation and deallocation.
Strict Syntax: Operations and conversions are more strictly defined, reducing the chance of unexpected behavior.
Static Typing: Types are checked at compile-time, which can prevent many errors before the program runs.

Examples:
C++: Requires explicit type declarations and manual memory management.
Java: Requires explicit type declarations and has strong static typing, though it uses automatic memory management (garbage collection).

Code Example (C++):
int x = 10;  // Explicitly declared as an integer
std::string y = "Hello";  // Explicitly declared as a string
int z = x + 5;  // Operations require explicitly typed variables

'''