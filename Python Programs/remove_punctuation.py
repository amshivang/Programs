import string
text = input("Enter a string: ")
no_punct = ''.join((char for char in text if char not in string.punctuation))
print(f'Original: {text}')
print(f'Cleaned:  {no_punct}')
