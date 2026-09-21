def change_string(s):
    s = "X" + s[1:]
    print(f"Inside change_string: {s}")

text = input("Enter a string: ")
print(f"Original string before function call: {text}")
change_string(text)
print(f"Original string after function call:  {text}")

