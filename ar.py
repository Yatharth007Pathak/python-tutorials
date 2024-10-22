joker = not True and False or True

print(joker)



'''
break down the expression joker = not True and False or True step by step according to the order of operations in Python:

not operator: The not operator has the highest precedence.
not True evaluates to False.
So, the expression now is:
False and False or True

and operator: The and operator is evaluated next.
False and False evaluates to False.
Now the expression is:
False or True

or operator: The or operator is evaluated last.
False or True evaluates to True.
Therefore, when we print the value of joker, the output will be True.
'''