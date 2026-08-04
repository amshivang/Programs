# Reverse a string without using slicing
text = "Python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(f"Original: {text}")
print(f"Reversed: {reversed_text}")
