# # Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# # Найдите произведение элементов на указанных позициях. 

# # import random
# # def write_file(number):
# #     with open('file.txt', 'w') as data:
# #         for i in range(number):
# #             data.write(f"{random.randrange(0, 2*number)}\n")

# read_file = [2, 2, 3, 1, 8]
# indexs = list(map(int,data.read()))
# # def read_file():
# #     with open('file.txt', 'r') as data:
# #         indexs = list(map(int,data.read()))
# #     return indexs

# n = int(input("Введите число N: "))
# lst_number = [i for i in range(-n, n+1)]
# # write_file(n)
# lst_index = read_file()
# prod = 1
# for i in range(len(lst_index)):
#     prod *= lst_number[lst_index[i]]
# print(f"Результат равен = {prod}")


from random import randint
numbers = []

print(' Введите натуральное положительное число')
n = int(input())
for i in range(n):
    numbers.append(randint (-n,n))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Number of elements: ', get_numbers(numbers))

x = int(input('Введите первый индекс: '))
y = int(input('Введите второй индекс: '))
z = int(input('Введите третий индекс: '))
m = int(input('Введите четвертый индекс: '))
d = int(input('Введите пятый индекс: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]*numbers[z - 1]*numbers[m - 1]*numbers[d - 1]
print(f'Произведдение чисел на указанных местах равно: {numbers[x -1]} * {numbers[y -1]} * {numbers[z - 1]} * {numbers[m - 1]} * {numbers[m - 1]} =', mult)