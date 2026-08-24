import math

def calculate_area(radius):
    return math.pi * (radius ** 2)

def calculate_circumference(radius):
    return 2 * math.pi * radius

def calculate_circle(radius):
    area = calculate_area(radius)
    circumference = calculate_circumference(radius)
    return area, circumference

if __name__ == '__main__':
    radius = float(input('Enter radius of the circle: '))
    if radius < 0:
        print('Radius must be a non-negative value.')
    else:
        area, circumference = calculate_circle(radius)
        print(f'Area: {area:.4f}')
        print(f'Circumference: {circumference:.4f}')
