from second_largest import find_third_largest
from analyze_numbers import analyze_numbers
from student_result import evaluate_result

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

def main():
    while True:
        print('\n=== MENU ===')
        print('1. Third Largest Unique Number (second_largest.py)')
        print('2. Analyze Numbers (analyze_numbers.py)')
        print('3. Evaluate Student Result (student_result.py)')
        print('4. Exit')
        choice = input('Enter your choice (1-4): ').strip()
        if choice == '1':
            task1()
        elif choice == '2':
            task2()
        elif choice == '3':
            task3()
        elif choice == '4':
            print('Exiting program.')
            break
        else:
            print('Invalid choice! Please select 1, 2, 3, or 4.')

if __name__ == '__main__':
    main()