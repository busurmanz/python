# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.


def input_num():
    while True:
        try:
            n = int(input("Введите десятизначное число для преобразования: "))
            return n
        except:
            print("Неправильный ввод, попробуйте снова")


def create_binary_number(num):
    string_number = ""
    while num > 0:
        string_number = str(num % 2) + string_number
        num //= 2
    return string_number


my_number = input_num()
print(f"Из десятичного числа '{my_number}' получается двоичное число: {create_binary_number(my_number)}")
