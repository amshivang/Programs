# Input a number and calculate the sum of its digits
try:
    num = int(input("Enter an integer: "))
    temp = abs(num)
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    print(f"The sum of the digits of {num} is: {digit_sum}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
