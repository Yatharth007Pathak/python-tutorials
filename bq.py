# Newline (\n)                                        Inserts a new line in the text at the specified point

text = "Hello\nWorld"
print(text)
# Output:
# Hello
# World

# Tab (\t)                                            Inserts a horizontal tab.

text = "Hello\tWorld"
print(text)
# Output: Hello   World

# Backslash (\\)                                      Inserts a backslash character.

text = "This is a backslash: \\"
print(text)
# Output: This is a backslash: \

# Single Quote (\')                                   Inserts a single quote.

text = 'It\'s a sunny day'
print(text)
# Output: It's a sunny day

# Double Quote (\")                                   Inserts a double quote.

text = "She said, \"Hello!\""
print(text)
# Output: She said, "Hello!"

# Carriage Return (\r)                                Moves the cursor to the beginning of the line.

text = "Hello\rWorld"
print(text)
# Output: World

# Backspace (\b)                                      Moves the cursor back one space, deleting the previous character.

text = "Hello\bWorld"
print(text)
# Output: HellWorld

# Unicode Character (\u or \U)                        Inserts a Unicode character.

text = "\u03A9"  # Greek capital letter Omega
print(text)
# Output: Ω

text = "\U0001F600"  # Grinning face emoji
print(text)
# Output: 😀

# Octal Value (\ooo)                                  Inserts a character based on its octal value.

text = "\101"  # ASCII value for 'A'
print(text)
# Output: A

# Hexadecimal Value (\xhh)                            Inserts a character based on its hexadecimal value.

text = "\x41"  # ASCII value for 'A'
print(text)
# Output: A



'''
Common Escape Sequences

Newline
Inserts a new line in the text at the specified point.

Tab 
Inserts a horizontal tab.

Backslash 
Inserts a backslash character.

Single Quote
Inserts a single quote.

Double Quote
Inserts a double quote.

Carriage Return 
Moves the cursor to the beginning of the line.

Backspace 
Moves the cursor back one space, deleting the previous character.

Unicode Character 
Inserts a Unicode character.

Octal Value 
Inserts a character based on its octal value.

Hexadecimal Value 
Inserts a character based on its hexadecimal value.

'''