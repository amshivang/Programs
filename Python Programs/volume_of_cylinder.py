# Calculate the volume of a cylinder
import math

try:
    radius = float(input("Enter the radius of the cylinder's base (r): "))
    height = float(input("Enter the height of the cylinder (h): "))

    if radius < 0 or height < 0:
        print("Radius and height must be non-negative values.")
    else:
        volume = math.pi * (radius ** 2) * height
        print(f"\nRadius: {radius}")
        print(f"Height: {height}")
        print(f"Volume of the Cylinder: {volume:.4f}")
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
