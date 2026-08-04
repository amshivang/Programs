# Demonstrate break, continue, and pass statements

print("--- break ---")
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=" ")
print()

print("--- continue ---")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")
print()

print("--- pass ---")
for i in range(1, 6):
    if i == 3:
        pass
    print(i, end=" ")
print()
