# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
# Введите число N в файле input.txt


def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 3 != 0:
            s += lst[i]
    print(f"Сумма равна: {s}")

lst = [2, 3, 5, 9, 3]
sum_odd_index(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_index(lst)