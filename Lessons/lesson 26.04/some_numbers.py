import decimal
import fractions

print(type(30000000000000000000000000000000000000000000000000000))

print(6+2)
print(6-2)
print(6*2)
print(6/2)
print(6//2)

x = int(2.8)

print(type(x), x)

x = int(-2.8)

print(type(x), x)

x = int('3')

print(type(x), x)

print(type(3.5))

x = 3 + 5.4
print(x, type(x))

x = float('3.6')
print(x, type(x))

print(1.1 + 2.2 == 3.3)


x = decimal.Decimal(0.1)
print(x, type(x))

print(fractions.Fraction(2.5))