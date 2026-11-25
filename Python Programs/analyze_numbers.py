def analyze_numbers(*args):
    evens = [num for num in args if num % 2 == 0]
    odds = [num for num in args if num % 2 != 0]
    sum_even = sum(evens)
    sum_odd = sum(odds)
    count_even = len(evens)
    count_odd = len(odds)
    return {
        'evens': evens,
        'odds': odds,
        'sum_even': sum_even,
        'sum_odd': sum_odd,
        'count_even': count_even,
        'count_odd': count_odd,
        'avg_even': (sum_even / count_even) if count_even else 0.0,
        'avg_odd': (sum_odd / count_odd) if count_odd else 0.0,
    }


if __name__ == '__main__':
    user_input = input('Enter integers separated by comma: ').strip()
    if user_input:
        raw_numbers = user_input.replace(',', ' ').split()
        numbers = [int(x) for x in raw_numbers]
        res = analyze_numbers(*numbers)
        print(f"Even numbers: {res['evens']}")
        print(f"Odd numbers: {res['odds']}")
        print(f"Sum of even numbers: {res['sum_even']}")
        print(f"Sum of odd numbers: {res['sum_odd']}")
        print(f"Count of even numbers: {res['count_even']}")
        print(f"Count of odd numbers: {res['count_odd']}")
        print(f"Average of even numbers: {res['avg_even']:.2f}")
        print(f"Average of odd numbers: {res['avg_odd']:.2f}")
