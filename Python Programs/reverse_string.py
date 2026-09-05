import scapy.all as scapy
text = input("Enter a string to reverse: ")
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
print(f'Original: {text}')
print(f'Reversed: {reversed_text}')
