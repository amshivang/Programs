items = input("Enter list elements separated by space: ").split()
reversed_items = []

for item in items:
    reversed_items.insert(0, item)

print(f"Reversed list: {reversed_items}")
