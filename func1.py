def create_array(x, y):
    numbers = [int(i) for i in range(x, y + 1)]
    return numbers


x, y = int(input('Введите число от ')), int(input('Введите число до '))

print(create_array(x, y))
