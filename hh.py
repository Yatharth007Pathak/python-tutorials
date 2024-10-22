count = 0

with open("text7.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1

print(count)



# From a file containg numbers separated by comma, print the count of even numbers