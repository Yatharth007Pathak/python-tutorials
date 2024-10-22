# Reading from the source file
with open('text3.txt', 'r') as source_file:
    content = source_file.read()

# Writing to the destination file
with open('text4.txt', 'w') as destination_file:
    destination_file.write(content)



# Reading from and Writing to a File:- Here's a complete example that reads from one file and writes its content to another file: