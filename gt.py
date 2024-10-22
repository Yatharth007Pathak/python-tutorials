# Opening a file

f = open("text1.txt", "r")             # 'r' mode is for reading
data = f.read(10)                      # reads first 10 letters of the file
print(data)

print("\n")

data = f.read(20)                      # reads next 20 letters of the file
print(data)
print(type(data))
f.close()                              # Don't forget to close the file



# Opening and Closing Files:- We can open a file using the open() function and close it using the close() method.