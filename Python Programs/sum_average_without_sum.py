numbers = []
print("Enter 10 integers:")
for i in range(10):
    numbers.append(int(input(f"Enter integer {i + 1}: ")))

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print(f"\nList: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")
