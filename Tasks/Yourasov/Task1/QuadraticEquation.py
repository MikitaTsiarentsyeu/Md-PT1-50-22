a = 3
b = -14
c = -5
D = b**2 - 4 * a * c
print('Дискриминант =', D)
if D > 0:
    print('x1 =', (-b + D**0.5) / 2 * a)
    print('x2 =', (-b + D**0.5) / 2 * a)
elif D == 0:
    print('x =', -b / 2 * a)
elif D < 0:
    print('Корней нет')
   