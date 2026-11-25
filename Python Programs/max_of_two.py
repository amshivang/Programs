def find_max(num1, num2):
    return num1 if num1 > num2 else num2


if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        greater = find_max(a, b)
        display = int(greater) if greater.is_integer() else greater
        print(f"The greater number is: {display}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
