str = "i am a coder from india"

print(str.endswith("ia"))
print(str.endswith("co"))

print(str.capitalize())
print(str)

str = str.capitalize()
print(str)

print(str.replace("i","o"))
print(str.replace("coder","cricketer"))

print(str.find("c"))
print(str.find("from"))
print(str.find("q"))

print(str.count("am"))
print(str.count("a"))

'''
string functions

str.endswith("substr")               # returns true if string ends with substr
str.capitalize                       # capitalizes 1st char
str.replace(old,new)                 # replaces all occurrences of old with new
str.find(word)                       # returns 1st index of 1st occurence
str.count("substr")                  # counts the occurence of substr in string
'''