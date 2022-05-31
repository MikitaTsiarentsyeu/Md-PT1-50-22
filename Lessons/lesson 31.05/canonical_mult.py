def mult(a, b):
    if b < 0:
        a, b = -a, -b
    res = 0
    for i in range(b):
        res += a

    return res

print(mult(2, 3))
print(mult(3, 2))
print(mult(0, 2))
print(mult(3, 0))
print(mult(0, 0))
print(mult(-3, 2))
print(mult(3, -2))
print(mult(-3, -2))