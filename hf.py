def check_for_word():
    word = "cutting"
    with open("text6.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            print("Not Found")


check_for_word()



# Search of the word "cutting" exists in the file text6.txt or not using functions