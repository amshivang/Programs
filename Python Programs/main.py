from second_largest import find_third_largest
from analyze_numbers import analyze_numbers
from student_result import evaluate_result
from employee_salary import calculate_salary_details
from circle_area import calculate_circle
from rectangle_area import calculate_rectangle

def task1():
    user_input = input('Enter integers separated by comma: ').strip()
    if user_input:
        raw_numbers = user_input.replace(',', ' ').split()
        numbers = [int(x) for x in raw_numbers]
        result = find_third_largest(*numbers)
        if result is not None:
            print(f'Third largest unique number: {result}')
        else:
            print('Less than 3 unique numbers provided.')

def task2():
    user_input = input('Enter integers separated by comma: ').strip()
    if user_input:
        raw_numbers = user_input.replace(',', ' ').split()
        numbers = [int(x) for x in raw_numbers]
        res = analyze_numbers(*numbers)
        print(f"Even numbers: {res['evens']}")
        print(f"Odd numbers: {res['odds']}")
        print(f"Sum of even numbers: {res['sum_even']}")
        print(f"Sum of odd numbers: {res['sum_odd']}")
        print(f"Number of even numbers: {res['count_even']}")
        print(f"Number of odd numbers: {res['count_odd']}")
        print(f"Average of even numbers: {res['avg_even']:.2f}")
        print(f"Average of odd numbers: {res['avg_odd']:.2f}")

def task3():
    num_subjects_input = input('Enter number of subjects: ').strip()
    if num_subjects_input.isdigit():
        num_subjects = int(num_subjects_input)
        subject_marks = {}
        for i in range(1, num_subjects + 1):
            sub_name = input(f'Enter subject {i} name: ').strip()
            marks = float(input(f'Enter marks for {sub_name}: '))
            subject_marks[sub_name] = marks
        result = evaluate_result(**subject_marks)
        if result:
            print(f"Total Marks: {result['total_marks']:.2f}")
            print(f"Percentage: {result['percentage']:.2f}%")
            print(f"Highest Scoring Subject: {result['highest_subject']} ({result['highest_marks']:.2f})")
            print(f"Result: {result['status']}")

def task4():
    num_employees_input = input('Enter number of employees: ').strip()
    if num_employees_input.isdigit():
        num_employees = int(num_employees_input)
        employee_data = {}
        for i in range(1, num_employees + 1):
            name = input(f'Enter employee {i} name: ').strip()
            salary = float(input(f'Enter salary for {name}: '))
            employee_data[name] = salary
        result = calculate_salary_details(**employee_data)
        if result:
            print(f"Average Salary: {result['avg_salary']:.2f}")
            print(f"Highest Salary: {result['high_salary']:.2f}")
            print(f"Lowest Salary: {result['low_salary']:.2f}")
            print(f"Employee(s) with Highest Salary: {', '.join(result['highest_employees'])}")
            print(f"Employee(s) with Lowest Salary: {', '.join(result['lowest_employees'])}")
            print(f"Employee(s) with Salary above Average: {', '.join(result['above_avg_employees'])}")

def task5():
    radius_input = input('Enter radius of the circle: ').strip()
    try:
        radius = float(radius_input)
        if radius < 0:
            print('Radius must be a non-negative value.')
        else:
            area, circumference = calculate_circle(radius)
            print(f'Area: {area:.4f}')
            print(f'Circumference: {circumference:.4f}')
    except ValueError:
        print('Invalid input! Please enter a numeric radius.')

def task6():
    try:
        length = float(input('Enter length of the rectangle: ').strip())
        breadth = float(input('Enter breadth of the rectangle: ').strip())
        if length < 0 or breadth < 0:
            print('Length and breadth must be non-negative values.')
        else:
            perimeter, area = calculate_rectangle(length, breadth)
            print(f'Perimeter of rectangle: {perimeter:.4f}')
            print(f'Area of rectangle: {area:.4f}')
    except ValueError:
        print('Invalid input! Please enter numeric values for dimensions.')

def main():
    while True:
        print('\n=== MENU ===')
        print('1. Third Largest Unique Number (second_largest.py)')
        print('2. Analyze Numbers (analyze_numbers.py)')
        print('3. Evaluate Student Result (student_result.py)')
        print('4. Employee Salary Details (employee_salary.py)')
        print('5. Circle Area & Circumference (circle_area.py)')
        print('6. Rectangle Perimeter & Area (rectangle_area.py)')
        print('7. Exit')
        choice = input('Enter your choice (1-7): ').strip()
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            task4()
        elif choice == '5':
            task5()
        elif choice == '6':
            task6()
        elif choice == '7':
            print('Exiting program.')
            break
        else:
            print('Invalid choice! Please select 1, 2, 3, 4, 5, 6, or 7.')

if __name__ == '__main__':
    main()