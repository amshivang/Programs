# Compute factorial of a number using for loop
num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print(f"Factorial of {num} is: {fact}")
