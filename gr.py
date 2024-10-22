fruits = ["mango", "grapes", "litchi", "banana", "kiwi", "orange"]

def print_list(list, index = 0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list, index + 1)

print_list(fruits)



# Recursive function to print all elements in a list (use list and index as parameters)