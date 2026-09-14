text = input("Enter a string: ")

print(f"I. Uppercase: {text.upper()}")
print(f"II. Lowercase: {text.lower()}")
print(f"III. Reversed: {text[::-1]}")
print(f"IV. Vowel Count: {sum(char.lower() in 'aeiou' for char in text)}")

