# Программа принимает на вход число от 0 до 99, записанное цифрами, и выдает его в текстовом виде
def is_num(num):  # Проверка корректности ввода
    if num.isdigit() and -1 < int(num) < 100 and a[0] != '0':
        return True
    else:
        return False


tens = {'2': 'двадцать', '3': 'тридцать', '4': 'сорок',
        '5': 'пятьдесят', '6': 'шестьдесят', '7': 'семьдесят',
        '8': 'восемьдесят', '9': 'девяносто'}  # Словарь для разряда десятков
units = {'0': 'ноль', '1': 'один', '2': 'два',
         '3': 'три', '4': 'четыре', '5': 'пять',
         '6': 'шесть', '7': 'семь', '8': 'восемь',
         '9': 'девять',
         }  # Словарь для разряда единиц
ten_to_twenty = {'10': 'десять', '11': 'одиннадцать', '12': 'двенадцать',
                 '13': 'тринадцать', '14': 'четырнадцать', '15': 'пятнадцать',
                 '16': 'шестнадцать', '17': 'семнадцать', '18': 'восемнадцать',
                 '19': 'девятнадцать'}  # Словарь для чисел от 10 до 19

a = input('Введите целое число от 0 до 99: ')
while not is_num(a):  # Цикл не заканчивается, пока не будет введено корректное число
    a = input('Неверный формат числа. Введите целое число от 0 до 99: ')

if len(a) == 1:
    print(units[a])
elif int(a) > 19 and a[1] != '0':
   print(f'{tens[a[0]]} {units[a[1]]}')
elif int(a) > 19:
    print(tens[a[0]])
else:
    print(ten_to_twenty[a])
