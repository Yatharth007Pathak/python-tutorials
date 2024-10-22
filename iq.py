print(1 + 3)                          # arithmetic addition
print("Yatharth" + "Pathak")          # concatenating strings
print([1, 2, 3] + [4, 5, 6])          # merging lists



'''
Polymorphism: Operator overloading
When the same operator is allowed to have different meaning according to the context

Operator and Duder function
a + b     # addition                   a.__add__(b) 
a - b     # subtraction                a.__sub__(b)
a * b     # multiplication             a.__mul____(b)
a / b     # division                   a.__truediv____(b)
a % b     # modulus                    a.__mod____(b)
'''


'''
 let's break down each line of the code:

Addition of Integers:
print(1 + 3)
Operation: Addition of two integers.
Explanation: The + operator adds the integers 1 and 3 together.
Output: 4

String Concatenation:
print("Yatharth" + "Pathak")
Operation: Concatenation of two strings.
Explanation: The + operator concatenates the strings "Yatharth" and "Pathak" into a single string.
Output: "YatharthPathak"

List Concatenation:
print([1, 2, 3] + [4, 5, 6])
Operation: Concatenation of two lists.
Explanation: The + operator concatenates the two lists [1, 2, 3] and [4, 5, 6] into a single list.
Output: [1, 2, 3, 4, 5, 6]
'''