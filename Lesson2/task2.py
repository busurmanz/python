# Задание 2. Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

def set_products(n: int) -> list:
    set = [1]
    for i in range(2, n+1):
        set.append(set[-1] * i)
    return set

n = int(input('Введите натуральное число: '))
set = set_products(n)
print(set)
