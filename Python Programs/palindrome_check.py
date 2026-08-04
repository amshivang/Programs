# Check palindrome string
text = "madam"

is_palindrome = text.lower() == text.lower()[::-1]

print(f"String: '{text}'")
print("Is Palindrome:", is_palindrome)
