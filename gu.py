# Read the entire file:

file = open('text1.txt', 'r')
data = file.read()
print(data)
file.close()


print("\n")

# Read all lines into a list:


file = open('text1.txt', 'r')
lines = file.readlines()
print(lines)
file.close()


print("\n")


# Reads one line at a time:

file = open('text1.txt', 'r')
line1 = file.readline()
print(line1)
line2 = file.readline()
print(line2)
line3 = file.readline()
print(line3)
line4 = file.readline()
print(line4)
file.close()



# Reading Files:- There are several ways to read from a file