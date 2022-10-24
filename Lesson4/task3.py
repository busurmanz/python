# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


lst1 = list(map(int, input('Enter the numbers separated by a space :\n').split()))
print(f'Source list : {lst1}')
new_lst = []
[new_lst.append(i) for i in lst1 if i not in new_lst]
print(f'A list of non-repeating elements : {new_lst}')
