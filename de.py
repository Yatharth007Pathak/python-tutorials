info = {
    "key" : "value",
    "name" : "yatharth",
    "age" : "20",
    "cgpa" : 9.6,
    "marks" : (98, 97, 95)
}

print(info)
print(type(info))

print("\n")

print(info["key"])
print(info["name"])
print(info["age"])
print(info["cgpa"])
print(info["marks"])

print("\n")

info["name"] = "pathak"
print(info)