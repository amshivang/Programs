sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

output = ", ".join(f"{word}: {count}" for word, count in freq.items())
print(f"Output: {output}")
