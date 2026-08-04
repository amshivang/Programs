# Swap the values of three variables such that the first variable gets the value of the third.
try:
    a = input("Enter value of first variable (a): ")
    b = input("Enter value of second variable (b): ")
    c = input("Enter value of third variable (c): ")

    print(f"Before swapping: a = {a}, b = {b}, c = {c}")

    # Swapping logic: a gets value of c, b gets value of a, c gets value of b
    a, b, c = c, a, b

    print(f"After swapping:  a = {a}, b = {b}, c = {c}")
except Exception as e:
    print(f"An error occurred: {e}")
