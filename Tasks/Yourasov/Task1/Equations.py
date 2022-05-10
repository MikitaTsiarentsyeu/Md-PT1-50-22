# quadratic equation
from math import sqrt, pi, atan, cos


a = 3
b = -14
c = -5
D = b**2 - 4 * a * c
print('Discriminant =', D)
if D > 0:
    print('x1 =', (-b + D**0.5) / 2 * a)
    print('x2 =', (-b - D**0.5) / 2 * a)
elif D == 0:
    print('x =', -b / 2 * a)
elif D < 0:
    print('No root')

# quadratic equation
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
D = b**2 - 4 * a * c
print('Discriminant =', D)
if D > 0:
    print('x1 =', (-b + D**0.5) / 2 * a)
    print('x2 =', (-b - D**0.5) / 2 * a)
elif D == 0:
    print('x =', -b / 2 * a)
elif D < 0:
    print('No root')   

# cubic equation
a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
d = float(input('Enter d: '))

p = (3 * a * c - b**2) / 3 * a**2
q = (2 * b**3 - 9 * a * b * c + 27 * a**2 * d) / 27 * a**3

if q < 0:
    fi = atan(sqrt(-D) / (-q / 2))
elif q > 0:
    fi = atan(sqrt(-D) / (-q / 2)) + pi
elif q == 0:
    fi = pi / 2

D = (q / 2)**2 + (p / 3)**3
print('Discriminant =', D)

if D > 0:
    y1 = (-q / 2 + sqrt(D))**(1/3) + (-q / 2 - sqrt(D))**(1/3)
    y2 = -0.5 * ((-q / 2 + sqrt(D))**(1/3) + (-q / 2 - sqrt(D))**(1/3)) + sqrt(3) / 2 ((-q / 2 + sqrt(D))**(1/3) - (-q / 2 - sqrt(D))**(1/3))
    y3 = -0.5 * ((-q / 2 + sqrt(D))**(1/3) + (-q / 2 - sqrt(D))**(1/3)) - sqrt(3) / 2 ((-q / 2 + sqrt(D))**(1/3) - (-q / 2 - sqrt(D))**(1/3))
    print('x1 =', y1 - b / 3 * a)
    print('x2 =', y2 - b / 3 * a)
    print('x3 =', y3 - b / 3 * a)
elif D == 0 and p != 0 and q != 0:
    y1 = 2 * (-q / 2)**(1/3)
    y2 = -(-q / 2)**(1/3)
    print('x1 =', y1 - b / 3 * a)
    print('x2 =', y2 - b / 3 * a)
elif D == 0 and p == 0 and q == 0:
    print('x =', -b / 3 * a)
elif D < 0:
    y1 = 2 * sqrt(-p / 3) * cos(fi / 3)
    y2 = 2 * sqrt(-p / 3) * cos(fi / 3 + 2 * pi / 3)
    y3 = 2 * sqrt(-p / 3) * cos(fi / 3 + 4 * pi / 3)
    print('x1 =', y1 - b / 3 * a)
    print('x2 =', y2 - b / 3 * a)
    print('x3 =', y3 - b / 3 * a)   