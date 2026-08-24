def calculate_rectangle(length, breadth):
    perimeter = 2 * (length + breadth)
    area = length * breadth
    return perimeter, area

if __name__ == '__main__':
    length = float(input('Enter length of the rectangle: '))
    breadth = float(input('Enter breadth of the rectangle: '))
    if length < 0 or breadth < 0:
        print('Length and breadth must be non-negative values.')
    else:
        perimeter, area = calculate_rectangle(length, breadth)
        print(f'Perimeter: {perimeter:.4f}')
        print(f'Area: {area:.4f}')
