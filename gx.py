with open('text2.txt', 'r') as file:
    content = file.read()
    print(content)
    print(type(content))
    # File is automatically closed after this block



# Context Manager:- (with syntax) Using with ensures that the file is properly closed after its suite finishes, even if an exception is raised: