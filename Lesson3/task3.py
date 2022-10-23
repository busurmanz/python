# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.

import random


def input_num():
    while True:
        try:
            n = int(input("Введите длину списка: "))
            return n
        except:
            print("Неправильный ввод, попробуйте снова")


def create_random_lst_float(size):
    lst = []
    while True:
        try:
            iMin = int(input("Введите минимальное рандомное число: "))
            iMax = int(input("Введите максимальное рандомное число: "))
            break
        except:
            print("Неправильный ввод, попробуйте снова")

    for i in range(size):
        numb = random.uniform(iMin, iMax)
        lst.append(round(numb, 2))
    return lst


def zero_float(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] - int(lst[i])
        lst[i] = round(lst[i], 2)
    return lst
        
def difference_float(lst):
    iMax = lst[0]
    iMin = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > iMax:
            iMax = lst[i]
        if lst[i] < iMin:
            iMin = lst[i]
             
    return iMax - iMin




my_lst = create_random_lst_float(input_num())
print()
print(f'Сгенерировали рандомный список из вещественных чисел: \n{my_lst}')
my_lst_2 = zero_float(my_lst)
print()
print(f'Убрали левую часть из элементов списка: \n{my_lst_2}')
print()
print(f'Разница между макимальным и минимальным значением дробной части: {difference_float(my_lst_2)}')
print()