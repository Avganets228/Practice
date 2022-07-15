import random


def random_num(x):
    numbers = []
    for i in range(x):
        numbers.append(random.randint(0, 1001))
    return numbers

x = int(input('Введите количество чисел: '))
print(random_num(x))