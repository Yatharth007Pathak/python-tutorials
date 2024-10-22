# Function to replace multiple occurrences of a substring
def replace_occurrences(original_string, old_substring, new_substring):
    return original_string.replace(old_substring, new_substring)

# Example usage
text = "The weather is sunny. I love sunny days because sunny days are the best."
old = "sunny"
new = "rainy"

# Replacing all occurrences
result = replace_occurrences(text, old, new)
print("Original string:", text)
print("Modified string:", result)

# Python program that replaces multiple occurrences of a specific substring within a string