items = [
    100,
    10.5,
    True,
    "Python",
    [1, 2, 3],
    (10, 20),
    {"name": "Shivang"},
    None,
    4 + 5j
]

print(f"{'Value':<20} | {'Predicted Type'}")
print("-" * 45)
for item in items:
    print(f"{str(item):<20} | {type(item)}")
