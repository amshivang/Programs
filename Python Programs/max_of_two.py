def find_max(num1, num2):
    return num1 if num1 > num2 else num2

a = (input("Enter first number: "))
b = (input("Enter second number: "))
print(f"The greater number is: {find_max(a, b)}")
