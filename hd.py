with open("text6.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open("text6.txt", "w") as f:
    f.write(new_data)



# Replace all occurences of "Java" with "Python" in file text6.txt