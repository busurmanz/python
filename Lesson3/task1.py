# Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.

import random


def input_num():
    while True:
        try:
            n = int(input("Введите длину списка: "))
            return n
        except:
            print("Неправильный ввод, попробуйте снова")
            

def create_random_lst(size):
    lst = []
    while True:
        try:
            iMin = int(input("Введите минимальное рандомное число: "))
            iMax = int(input("Введите максимальное рандомное число: "))
            break
        except:
            print("Неправильный ввод, попробуйте снова")
  
    for i in range(size):
        lst.append(random.randint(iMin, iMax))
    return lst


def sum_odd_number(lst):
    sum = 0
    for i in range(1, len(lst),2):
        sum = lst[i] + sum
    return sum


my_lst = create_random_lst(input_num())
print(my_lst)
print(f'Сумма чисел стоящих на нечетной позиции равна: {sum_odd_number(my_lst)}')