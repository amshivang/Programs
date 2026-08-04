# Takes three digits from the user and adds the square of each digit
try:
    d1 = int(input("Enter first digit (0-9): "))
    d2 = int(input("Enter second digit (0-9): "))
    d3 = int(input("Enter third digit (0-9): "))

    # Check if they are single digits (optional but helpful for strict correctness)
    if not (0 <= abs(d1) <= 9 and 0 <= abs(d2) <= 9 and 0 <= abs(d3) <= 9):
         print("Note: Some entered values are not single digits, but calculating sum of squares anyway.")

    sum_squares = (d1 ** 2) + (d2 ** 2) + (d3 ** 2)
    print(f"The sum of squares of the digits ({d1}, {d2}, {d3}) is: {sum_squares}")
except ValueError:
    print("Invalid input. Please enter integer values.")
