# Using break
for i in range(10):
    if i == 5:
        break
    print(i)

print("\n")

# Using continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)



'''
Python provides control statements to alter the flow of a loop:

break: Terminates the loop entirely.
continue: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
'''