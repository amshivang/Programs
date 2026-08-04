# Reverse digits of a given integer entered by the user
try:
    num = int(input("Enter an integer: "))
    sign = -1 if num < 0 else 1
    temp = abs(num)
    rev = 0

    while temp > 0:
        rem = temp % 10
        rev = (rev * 10) + rem
        temp //= 10

    rev *= sign
    print(f"Original: {num}, Reversed: {rev}")
except ValueError:
    print("Invalid input. Please enter an integer.")
