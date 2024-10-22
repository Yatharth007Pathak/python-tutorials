def summation(n):
    if(n == 0):
        return 0
    else:
        return n + summation(n - 1)

print(summation(5))
print(summation(6))
print(summation(7))



# Sum of Natural Numbers using recursive function