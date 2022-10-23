# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.

#n = int(input("N: "))
#N = 5
#def sequence(N):
#    for i in range(n):
#       print ((- 3) ** i, end=' ')

#sequence(N)    


# Для натурального n создать словарь индекс-значение, состоящий из элементов 3n = 1

n = int(n)
d = {}

for i in range(1, n+1):
    d[i] = 3*i+1

print (d)    
assert d == {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# Напишите программу, в которой пользователь будет задавать две строки, а программа определять количество вхождений одной строки в другой.

exit ()
s = input ()
subs = input()

found_cnt = 0

for i in range(len(s) - len(subs) + 1):
    s1 = s[i: i == len(subs)]
    if s1 == subs:
        found_cnt += 1
       
        print(found_cnt)