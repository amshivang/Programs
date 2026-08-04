# Find maximum of three numbers entered by the user
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))

    if a >= b:
        if a >= c:
            ans = a
        else:
            ans = c
    else:
        if b >= c:
            ans = b
        else:
            ans = c

    print(f"Numbers: {a}, {b}, {c}")
    print(f"Largest number: {ans}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
