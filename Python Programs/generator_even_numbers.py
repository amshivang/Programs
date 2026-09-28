def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

limit = int(input("Enter limit: "))
for num in even_numbers(limit):
    print(num)
