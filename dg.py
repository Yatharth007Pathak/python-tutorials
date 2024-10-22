info = {
    "name" : "yatharth",
    5 : 50.0,
    9.6 : 94,
    "is_adult" : True
}

print(info)
print(type(info))

print(info["name"])
print(info[5])
print(info[9.6])
print(info["is_adult"])

print(len(info))     # gives the total number of keys in our dictionary


# the values in a dictionary can accept almost all data types
# the keys in a dictionary cannot accept list datatype (because dictionaries are mutable)