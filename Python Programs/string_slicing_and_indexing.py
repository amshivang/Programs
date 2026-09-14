text = input("Enter a string: ")

print(f"I. First 3 characters: {text[:3]}")
print(f"II. Last 2 characters: {text[-2:]}")
print(f"III. Every second character: {text[::2]}")
print(f"IV. Reversed using slicing: {text[::-1]}")
