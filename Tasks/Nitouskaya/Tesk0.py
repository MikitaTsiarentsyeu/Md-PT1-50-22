# 3x2 - 14x - 5 = 0 
# D = b2 - 4ac
# x1 = (-b + math.sqrt(D)) / 2a
# x2 = (-b - math.sqrt(D)) / 2a

a = 3
b = -14
c = -5
D = b ** 2 - 4 * a * c
print (D)

x1 = (- b + (D ** 0.5)) // (2 * a)
x2 = (- b - (D ** 0.5)) // (2 * a)
print (x1, x2)

import math
x1 = (- b + math.sqrt (D)) // (2 * a)
x2 = (- b - math.sqrt (D)) // (2 * a)
print (x1, x2)
