def second_largest(*args):
    unique_nums = []
    for num in args:
        if num not in unique_nums:
            unique_nums.append(num)
            
    if len(unique_nums) < 2:
        return None
        
    unique_nums.sort(reverse=True)
    return unique_nums[1]

user_input = input('Enter integers separated by comma: ').strip()
if user_input:
    raw_numbers = user_input.replace(',', ' ').split()
    numbers = [int(x) for x in raw_numbers]
    result = second_largest(*numbers)
    print(f'Second largest unique number: {result}')
