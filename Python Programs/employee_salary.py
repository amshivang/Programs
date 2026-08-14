def employee_salary(*args, **kwargs):
    all_salaries = list(args) + list(kwargs.values())
    if not all_salaries:
        return
        
    avg_salary = sum(all_salaries) / len(all_salaries)
    high_salary = max(all_salaries)
    low_salary = min(all_salaries)
    
    print(f'Average Salary: {avg_salary:.2f}')
    print(f'Highest Salary: {high_salary:.2f}')
    print(f'Lowest Salary: {low_salary:.2f}')
    
    print('Employees earning above average:')
    for name, salary in kwargs.items():
        if salary > avg_salary:
            print(f'{name}: {salary:.2f}')
            
    for i, salary in enumerate(args, start=1):
        if salary > avg_salary:
            print(f'Unnamed Employee {i}: {salary:.2f}')

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
