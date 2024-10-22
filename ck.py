fruits = ["apple", "banana", "cherry"]

# Change the second element
fruits[1] = "blueberry"
print(fruits)  # Output: ["apple", "blueberry", "cherry"]

# Add an element to the end
fruits.append("date")
print(fruits)  # Output: ["apple", "blueberry", "cherry", "date"]

# Sort the list in descending order
fruits.sort(reverse = True)
print(fruits)  # Output: ["date", "cherry", "blueberry", "apple"]

# Sort the list in ascending order
fruits.sort()
print(fruits)  # Output: ["apple", "blueberry", "cherry", "date"]

# Insert an element at a specific position
fruits.insert(1, "kiwi")
print(fruits)  # Output: ["apple", "kiwi", "blueberry", "cherry", "date"]

# Remove an element by value
fruits.remove("kiwi")
print(fruits)  # Output: ["apple", "blueberry", "cherry", "date"]

# Remove an element by index
del fruits[2]
print(fruits)  # Output: ["apple", "blueberry", "date"]

# Remove and return the last element
last_fruit = fruits.pop()
print(last_fruit)  # Output: "date"
print(fruits)  # Output: ["apple", "blueberry"]



# Modifying lists:- Lists are mutable, meaning we can change their content.