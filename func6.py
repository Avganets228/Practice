import random


def tasks_6_to_10(numbers):
    odd_numbers = []
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    max_odd_num = sorted(odd_numbers)[-1]
    max_even_num = sorted(even_numbers)[-1]
    sum_odd_numbers = sum(odd_numbers)
    sum_even_numbers = sum(even_numbers)
    sum_min_max = min(numbers) + max(numbers)
    return 'Максимальное нечетное число ', max_odd_num, 'Максимальное четное число', max_even_num, 'Сумма нечетных чисел', sum_odd_numbers, 'Сумма четных чисел', sum_even_numbers, 'Сумма максимального минимального числа', sum_min_max


numbers = [random.randint(0, 100) for _ in range(int(input('Введите положительное число:')))]

print(tasks_6_to_10(numbers))