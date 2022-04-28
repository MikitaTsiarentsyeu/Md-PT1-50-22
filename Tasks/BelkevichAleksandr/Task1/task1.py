a = 3
b = -14
c = -5

disc = b**2 - (4 * a * c)

if disc < 0:
    print("Корней нет")
elif disc == 0:
    print(-(b/2*a))
elif disc > 0:
    print((-b + disc*0.5) / 2*a)
    print((-b + disc*0.5) / 2*a)

