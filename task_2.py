# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input(f'Введите натуральное число:\n'))
i = 2
while n % i != 0:
    i += 1
print(f'Наименьший натуральный делитель:\n{i}')