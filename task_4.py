# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

a = 1
N = int(input("Введите длинну массива (N): "))
res = sum(i for i in range(a, N + 1) if i % 2 == 0)
print(f'Сумма четных элементов от 1 до {N} включительно -> {res}')
