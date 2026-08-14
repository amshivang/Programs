def analyze_numbers(*args):
    evens = []
    odds = []
    for num in args:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
            
    print(f'Even numbers: {evens}')
    print(f'Odd numbers: {odds}')
    print(f'Sum of even numbers: {sum(evens)}')
    print(f'Sum of odd numbers: {sum(odds)}')
    print(f'Count of even numbers: {len(evens)}')
    print(f'Count of odd numbers: {len(odds)}')

user_input = input('Enter integers separated by comma: ').strip()
if user_input:
    raw_numbers = user_input.replace(',', ' ').split()
    numbers = [int(x) for x in raw_numbers]
    analyze_numbers(*numbers)