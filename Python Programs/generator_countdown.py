def countdown(n):
    while n >= 1:
        yield n
        n -= 1

n = int(input("Enter the value of n: "))
for num in countdown(n):
    print(num)
