def find_second_largest(*args):
    unique_nums = []
    for num in args:
        if num not in unique_nums:
            unique_nums.append(num)
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]


def find_third_largest(*args):
    unique_nums = []
    for num in args:
        if num not in unique_nums:
            unique_nums.append(num)
    if len(unique_nums) < 3:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[2]


if __name__ == '__main__':
    user_input = input('Enter integers separated by comma: ').strip()
    if user_input:
        numbers = [int(x) for x in user_input.replace(',', ' ').split()]
        result = find_second_largest(*numbers)
        if result is not None:
            print(f'Second largest unique number: {result}')
        else:
            print('Less than 2 unique numbers provided.')
