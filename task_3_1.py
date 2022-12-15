# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

import os
from task_3_2 import list_from_minusN_to_N as original
from task_3_2 import input_num
from task_3_2 import random_list as random_l

os.system('cls')

number = input_num('Введите чило: ')
print('Исходный массив:')
my_list = original(number)
print(my_list)

print('Индексы')
indexes_list = random_l(len(my_list))
print(indexes_list)

print('Произведение элементов массива с указанными индексами:')
product = 1
for i in indexes_list:
    print(my_list[i], end='')
    if indexes_list.index(i) < len(indexes_list) - 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    product *= my_list[i]

print(product)
