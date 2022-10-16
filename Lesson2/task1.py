# Задание 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

def sum_number(n: float) -> int:
    num=int(str(n).replace('.', ''))
    sum = 0
    while num != 0:
        sum = sum + num%10
        num //= 10
    return sum

n = float(input('Введите вещественное число: '))
sum = sum_number(n)
print(sum)
