# Check whether a given number is divisible by both 3 and 6
try:
    num = int(input("Enter an integer: "))
    
    is_div_by_3 = (num % 3 == 0)
    is_div_by_6 = (num % 6 == 0)

    if is_div_by_3 and is_div_by_6:
        print(f"Yes, {num} is divisible by both 3 and 6.")
    else:
        print(f"No, {num} is NOT divisible by both 3 and 6.")
        print(f"Divisible by 3: {is_div_by_3}")
        print(f"Divisible by 6: {is_div_by_6}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
