# Count vowels and consonants in a string
text = "Hello Python"
vowels = "aeiouAEIOU"

v_count = 0
c_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"String: '{text}'")
print(f"Vowels: {v_count}, Consonants: {c_count}")
