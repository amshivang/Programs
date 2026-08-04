# Check whether a given 4-digit number is a narcissistic number or not
try:
    num_str = input("Enter a 4-digit integer: ").strip()
    num = int(num_str)

    # Validate that it is a 4-digit number
    if len(num_str) != 4 or num < 0:
        print("Error: Please enter a positive 4-digit integer (1000 to 9999).")
    else:
        # Sum of 4th powers of each digit
        digit_sum = sum(int(digit) ** 4 for digit in num_str)

        if digit_sum == num:
            print(f"Yes, {num} is a narcissistic number.")
            print(f"Calculation: {' + '.join(f'{d}^4' for d in num_str)} = {digit_sum}")
        else:
            print(f"No, {num} is NOT a narcissistic number.")
            print(f"Calculation: {' + '.join(f'{d}^4' for d in num_str)} = {digit_sum} (not equal to {num})")
except ValueError:
    print("Invalid input. Please enter a valid 4-digit integer.")
