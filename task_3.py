# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

from random import randint
list = []

print(' Введите натуральное положительное число')
n = int(input())
for i in range(n):
    list.append(randint (-n,n))
print(list)

def get_list(list):
    count =0 
    for element in list:
        count +=1
    return count
print('Колличество элементов: ', get_list(list))

x = int(input('Введите первый номер: '))
y = int(input('Введите второй номер: '))
z = int(input('Введите третий номер: '))
m = int(input('Введите четвертый номер: '))
d = int(input('Введите пятый номер: '))

for i in range(len(list)):
    multiplication = list[x -1] * list[y - 1] * list[z - 1] * list[m - 1] * list[d - 1]
print(f'Произведдение чисел на указанных местах равно: {list[x -1]} * {list[y -1]} * {list[z - 1]} * {list[m - 1]} * {list[d - 1]} =', multiplication)
