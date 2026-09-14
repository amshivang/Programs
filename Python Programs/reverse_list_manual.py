items = input("Enter list elements separated by space: ").split()

left = 0
right = len(items) - 1

while left < right:
    temp = items[left]
    items[left] = items[right]
    items[right] = temp
    left += 1
    right -= 1

print(f"Reversed list: {items}")  