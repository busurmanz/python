# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

import os


def input_num():
    os.system('clear') # списал со stackoverflow классная штука 
    while True:
        try:
            n = int(input("Сколько чисел Фибоначчи нужно вывести: "))
            return n + 1 # сделал, только для того что бы было как в примере задачи
        except:
            print("Неправильный ввод, попробуйте снова")


def fibonacci(num):
    fibonacci_number = []
    fib_1, fib_2 = 1, 1
    for i in range(num - 1):
        fibonacci_number.append(fib_1)
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    fib_1, fib_2 = 0, 1
    for i in range(num):
        fibonacci_number.insert(0, fib_1)
        fib_1, fib_2 = fib_2, fib_1 - fib_2
    return fibonacci_number

my_num = input_num()
print()
print(f'Список чисел Фибоначчи: {fibonacci(my_num)}')
print()