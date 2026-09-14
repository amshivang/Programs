import string

text = input("Enter a string: ")

no_punct = ""

for char in text:
    if char not in string.punctuation:
        no_punct += char

print(f"Original: {text}")
print(f"Cleaned:  {no_punct}")
