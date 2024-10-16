import math


def is_side(side):
    if side.replace('.', '').isdigit() and float(side) > 0:
        return True
    else:
        return False


def is_angle(ang):
    if ang.replace('.', '').isdigit() and 0 < float(ang) < 180:
        return True
    else:
        return False


a = input('Введите длину стороны A: ')
while not is_side(a):
    a = input('Неверный формат длины. Введите длину стороны a: ')
a = float(a)
    
b = input('Введите длину стороны B: ')
while not is_side(b):
    b = input('Неверный формат длины. Введите длину стороны b: ')
b = float(b)

ang = input('Введите угол a: ')
while not is_angle(ang):
    ang = input('Неверный формат угла. Введите угол a: ')
ang = math.radians(float(ang))

c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(ang))
print(c)



    