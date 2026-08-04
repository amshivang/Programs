# Remove all punctuation from a string
import string

text = "Hello, World! Welcome to Python 3."
no_punct = "".join(char for char in text if char not in string.punctuation)

print(f"Original: {text}")
print(f"Cleaned:  {no_punct}")
