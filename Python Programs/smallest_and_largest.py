numbers = []
print("Enter 7 integers:")
for i in range(7):
    numbers.append(int(input(f"Enter integer {i + 1}: ")))

smallest = numbers[0]
largest = numbers[0]

for num in numbers[1:]:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f"\nList: {numbers}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
