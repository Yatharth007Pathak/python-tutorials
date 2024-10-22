import string

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.printable)
print(string.punctuation)
print(string.whitespace)


'''
 let's break down the code that uses the string module in Python:

Importing the String Module:
import string
This imports the string module, which contains various string constants and utility functions.

Printing Lowercase ASCII Letters:
print(string.ascii_lowercase)
This prints all lowercase ASCII letters from 'a' to 'z'.
Output: abcdefghijklmnopqrstuvwxyz

Printing Uppercase ASCII Letters:
print(string.ascii_uppercase)
This prints all uppercase ASCII letters from 'A' to 'Z'.
Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Printing All ASCII Letters:
print(string.ascii_letters)
This prints all ASCII letters, both lowercase and uppercase.
Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Printing Digits:
print(string.digits)
This prints all decimal digits from '0' to '9'.
Output: 0123456789

Printing Hexadecimal Digits:
print(string.hexdigits)
This prints all hexadecimal digits, including both lowercase and uppercase letters.
Output: 0123456789abcdefABCDEF

Printing Octal Digits:
print(string.octdigits)
This prints all octal digits from '0' to '7'.
Output: 01234567

Printing Printable Characters:
print(string.printable)
This prints all characters considered printable, which includes digits, letters, punctuation, and whitespace.
Output: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_{|}~ \t\n\r\x0b\x0c`

Printing Punctuation Characters:
print(string.punctuation)
This prints all punctuation characters.
Output: !"#$%&'()*+,-./:;<=>?@[\\]^_{|}~`

Printing Whitespace Characters:
print(string.whitespace)
This prints all whitespace characters, including space, tab (\t), newline (\n), carriage return (\r), 
vertical tab (\x0b), and form feed (\x0c).
Output: \t\n\r\x0b\x0c

Explanation of Constants:
string.ascii_lowercase: A string containing all lowercase ASCII letters.
string.ascii_uppercase: A string containing all uppercase ASCII letters.
string.ascii_letters: A string containing all ASCII letters (both uppercase and lowercase).
string.digits: A string containing all decimal digit characters.
string.hexdigits: A string containing all hexadecimal digit characters (0-9 and a-f, A-F).
string.octdigits: A string containing all octal digit characters (0-7).
string.printable: A string containing all characters that are considered printable (digits, letters, punctuation, and whitespace).
string.punctuation: A string containing all punctuation characters.
string.whitespace: A string containing all whitespace characters.
'''