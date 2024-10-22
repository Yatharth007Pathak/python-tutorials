info = {
    "key" : "value",
    "name" : "yatharth",
    "subject" : ["python", "C", "java"],
    "topics" : ("dict", "set"),
    "age" : "20",
    "cgpa" : 9.6,
    "marks" : [98, 97, 95]
}

print(info)
print(type(info))

print("\n")

print(info.keys())
print(list(info.keys()))
print(tuple(info.keys()))

print("\n")

print(info.values())
print(list(info.values()))
print(tuple(info.values()))


# We can store lists and tuples inside a dictionary