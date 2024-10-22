f = open("text1.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()



'''
Types of all files:-
Text files:- .txt, .docx, .log etc.
Binary files:- .mp4, .mov, .png, .jpeg etc.

File I/O in Python
File input and output (I/O) in Python allows us to read from and write to files on our system.
Python can be usedto perform operations on a file(read and write data).

We have to open a file before reading or writing
f = open("file_name", "mode")
data = f.read()
f.close()

file_name can be sample.txt, demo.docx etc.
mode can be r (read mode), w (write mode)

Here are some common file modes:

'r': open for reading (default)
'w': open for writing (truncating the file first)
'a': open for writing, appending to the end of the file if it exists
'x': create a new file and open it for writing
'b': binary mode
't': text mode (default)
'+': open a disk file for updating (reading and writing)

We can combine these modes, for example, 'rb' for reading in binary mode or 'w+' for writing and reading or 'r+' for reading and writing
'''