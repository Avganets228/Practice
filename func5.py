import random


def sorted_num(numbers):
    return sorted(numbers)


numbers = [random.randint(0, 100) for _ in range(int(input('Введите положительное число:')))]

print(sorted_num(numbers))