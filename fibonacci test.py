number = int(input())


def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for a in range(number+1):
    print(fibonacci(a))