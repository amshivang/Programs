# Check whether a given 4-digit number is a narcissistic number or not
try:
    num_str = input("Enter a 4-digit integer: ").strip()
    num = int(num_str)

    # Validate that it is a genuine 4-digit integer (1000 to 9999)
    if not (1000 <= num <= 9999):
        print("Error: Please enter a positive 4-digit integer (1000 to 9999).")
    else:
        digits = str(num)
        digit_sum = sum(int(digit) ** 4 for digit in digits)

        if digit_sum == num:
            print(f"Yes, {num} is a narcissistic number.")
            print(f"Calculation: {' + '.join(f'{d}^4' for d in digits)} = {digit_sum}")
        else:
            print(f"No, {num} is NOT a narcissistic number.")
            print(f"Calculation: {' + '.join(f'{d}^4' for d in digits)} = {digit_sum} (not equal to {num})")
except ValueError:
    print("Invalid input. Please enter a valid 4-digit integer.")
