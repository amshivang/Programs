# Check whether a given number is an Armstrong number or not
try:
    num_str = input("Enter a non-negative integer: ").strip()
    num = int(num_str)

    if num < 0:
        print("Armstrong numbers are defined for non-negative integers.")
    else:
        # Number of digits
        n = len(num_str)
        temp = num
        digit_sum = 0

        while temp > 0:
            digit = temp % 10
            digit_sum += digit ** n
            temp //= 10

        if digit_sum == num:
            print(f"Yes, {num} is an Armstrong number.")
            print(f"Calculation: {' + '.join(f'{d}^{n}' for d in num_str)} = {digit_sum}")
        else:
            print(f"No, {num} is NOT an Armstrong number.")
            print(f"Calculation: {' + '.join(f'{d}^{n}' for d in num_str)} = {digit_sum} (not equal to {num})")
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
