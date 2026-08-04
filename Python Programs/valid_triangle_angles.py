# Check if three angles can form a valid triangle
try:
    angle1 = float(input("Enter first angle: "))
    angle2 = float(input("Enter second angle: "))
    angle3 = float(input("Enter third angle: "))

    # Three angles form a valid triangle if their sum is 180 and all angles are greater than 0
    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        if (angle1 + angle2 + angle3) == 180:
            print(f"Angles ({angle1}, {angle2}, {angle3}) can form a valid triangle.")
        else:
            print(f"Angles ({angle1}, {angle2}, {angle3}) cannot form a valid triangle. Sum is {angle1 + angle2 + angle3} instead of 180.")
    else:
        print("All angles must be greater than 0.")
except ValueError:
    print("Invalid input. Please enter numbers only.")
