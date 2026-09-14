text = input("Enter a string: ")

print(f"I. Uppercase: {text.upper()}")
print(f"II. Lowercase: {text.lower()}")
print("III. Reversed: ", end="")
i = len(text) - 1
while i >= 0:
    print(text[i], end="")
    i -= 1
print(f"\nIV. Vowel Count: {sum(char.lower() in 'aeiou' for char in text)}")

