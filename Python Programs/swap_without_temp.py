# Swap two numbers without using a temporary variable
try:
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))

    print(f"Before swapping: a = {a}, b = {b}")

    # Swapping using arithmetic operations
    a = a + b
    b = a - b
    a = a - b

    print(f"After swapping:  a = {a}, b = {b}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
