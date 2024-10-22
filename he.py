word = "learning"

with open("text6.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")



# Search of the word "learning" exists in the file text6.txt or not