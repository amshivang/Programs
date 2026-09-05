def find_third_largest(*args):
    unique_nums = []
    for num in args:
        if num not in unique_nums:
            unique_nums.append(num)
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]