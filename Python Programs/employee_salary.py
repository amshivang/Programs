def calculate_salary_details(*args, **kwargs):
    all_salaries = list(args) + list(kwargs.values())
    if not all_salaries:
        return None

    avg_salary = sum(all_salaries) / len(all_salaries)
    high_salary = max(all_salaries)
    low_salary = min(all_salaries)

    named_entries = list(kwargs.items())
    unnamed_entries = [
        (f'Unnamed Employee {i}', salary) for i, salary in enumerate(args, start=1)
    ]
    all_entries = named_entries + unnamed_entries

    highest_employees = [name for name, sal in all_entries if sal == high_salary]
    lowest_employees = [name for name, sal in all_entries if sal == low_salary]
    above_avg_employees = [name for name, sal in all_entries if sal > avg_salary]

    return {
        'avg_salary': avg_salary,
        'high_salary': high_salary,
        'low_salary': low_salary,
        'highest_employees': highest_employees,
        'lowest_employees': lowest_employees,
        'above_avg_employees': above_avg_employees,
    }


def employee_salary(*args, **kwargs):
    result = calculate_salary_details(*args, **kwargs)
    if not result:
        return None

    print(f"Average Salary: {result['avg_salary']:.2f}")
    print(f"Highest Salary: {result['high_salary']:.2f}")
    print(f"Lowest Salary: {result['low_salary']:.2f}")
    print('Employees earning above average:')
    for name, salary in kwargs.items():
        if salary > result['avg_salary']:
            print(f'{name}: {salary:.2f}')
    for i, salary in enumerate(args, start=1):
        if salary > result['avg_salary']:
            print(f'Unnamed Employee {i}: {salary:.2f}')
    return result


if __name__ == '__main__':
    anon_input = input('Enter anonymous employee salaries separated by comma: ').strip()
    anon_salaries = []
    if anon_input:
        anon_salaries = [float(x) for x in anon_input.replace(',', ' ').split()]

    num_named = int(input('Enter number of named employees: '))
    named_salaries = {}
    for i in range(1, num_named + 1):
        name = input(f'Enter employee {i} name: ').strip()
        salary = float(input(f'Enter salary for {name}: '))
        named_salaries[name] = salary

    employee_salary(*anon_salaries, **named_salaries)
