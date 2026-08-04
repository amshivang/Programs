# Find frequency of characters in a string using a dictionary
text = "apple pie"
freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print(f"String: '{text}'")
print("Character Frequencies:")
print(freq)
