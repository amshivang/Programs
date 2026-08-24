from analyze_numbers import analyze_numbers

if __name__ == '__main__':
    user_input = input('Enter integers separated by comma: ').strip()
    if user_input:
        raw_numbers = user_input.replace(',', ' ').split()
        numbers = [int(x) for x in raw_numbers]
        result = analyze_numbers(*numbers)
        print(f"Even numbers: {result['evens']}")
        print(f"Odd numbers: {result['odds']}")
        print(f"Sum of even numbers: {result['sum_even']}")
        print(f"Sum of odd numbers: {result['sum_odd']}")
        print(f"Number of even numbers: {result['count_even']}")
        print(f"Number of odd numbers: {result['count_odd']}")
        print(f"Average of even numbers: {result['avg_even']:.2f}")
        print(f"Average of odd numbers: {result['avg_odd']:.2f}")
