# Calculate the Euclidean distance between two points in 2D space
import math

try:
    print("Enter coordinates for Point 1 (x1, y1):")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("Enter coordinates for Point 2 (x2, y2):")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print(f"Point 1: ({x1}, {y1})")
    print(f"Point 2: ({x2}, {y2})")
    print(f"Euclidean Distance: {distance:.4f}")
except ValueError:
    print("Invalid input. Please enter numbers only.")
