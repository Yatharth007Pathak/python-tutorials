# Sample lists
numbers = [5, 2, 9, 1, 5, 6]
words = ['banana', 'apple', 'cherry', 'date']

# 1. Using identity key function (default behavior)
print("Sorting numbers with default key:")
numbers.sort()
print(numbers)

# 2. Using a key function to sort numbers based on their absolute value (though not necessary here as they are positive)
print("\nSorting numbers with key function (absolute value):")
numbers.sort(key=abs)
print(numbers)

# 3. Using a key function to sort words by their length
print("\nSorting words by length:")
words.sort(key=len)
print(words)

# 4. Using a key function to sort words by their first character
print("\nSorting words by first character:")
words.sort(key=lambda x: x[0])
print(words)

# 5. Using a key function to sort words by their last character
print("\nSorting words by last character:")
words.sort(key=lambda x: x[-1])
print(words)

# 6. Using a key function to sort words in reverse alphabetical order
print("\nSorting words in reverse alphabetical order:")
words.sort(key=lambda x: x, reverse=True)
print(words)

# 7. Using a key function to sort words by the sum of ASCII values of their characters
print("\nSorting words by sum of ASCII values of characters:")
def sum_ascii(word):
    return sum(ord(char) for char in word)

words.sort(key=sum_ascii)
print(words)


'''
Python program to check what different key values can be used with the sort method, you can write a program that demonstrates various types of key functions. 
The key parameter of the sort method allows you to specify a function that takes an element of the list and returns a value to be used for sorting.
'''