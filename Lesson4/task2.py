# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


number1 = int(input('Enter a number : '))
i = 2  
lst1 = []
old = number1
while i <= number1:
    if number1 % i == 0:
        lst1.append(i)
        number1 //= i
        i = 2
    else:
        i += 1
print(f'Prime factors of a number {old} given in the list : => {lst1}')
