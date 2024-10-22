def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

print(calculator(5, 3, "add"))
print(calculator(5, 3, "subtract"))
print(calculator(5, 3, "multiply"))
print(calculator(5, 3, "divide"))


# A Simple Calculator using functions