import random


def max_num(numbers):
    return max(numbers)


numbers = [random.randint(0, 100) for _ in range(int(input('Введите положительное число:')))]

print(max_num(numbers))
