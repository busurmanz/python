# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


txt1 = input('Enter the words separated by a space :\n')
print(f'Source text : => {txt1}')
find_txt = 'абв'
lst = [i for i in txt1.split() if find_txt not in i]
print(f'Result : => {" ".join(lst)}')
