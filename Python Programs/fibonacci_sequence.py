# Display Fibonacci sequence up to n terms
n = 10
a, b = 0, 1

print(f"Fibonacci sequence ({n} terms):")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
