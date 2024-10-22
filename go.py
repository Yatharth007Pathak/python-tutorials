def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return factorial(n - 1, n * accumulator)

print(factorial(5))



# Tail-recursive version of factorial (though Python does not optimize it)

'''
Tail recursion is a special form of recursion where the recursive call is the last operation in the function. 
Python does not optimize tail-recursive calls, so converting them to iterative solutions can be more efficient.
'''