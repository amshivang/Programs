sentence = input("Enter a sentence: ")
words = sentence.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Output: ", end="")
first = True
for word, count in freq.items():
    if not first:
        print(", ", end="")
    print(f"{word}: {count}", end="")
    first = False
