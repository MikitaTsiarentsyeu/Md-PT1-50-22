eq_val = input("please enter your eq: ")
x = input("please enter x value: ")

print(x)
print(type(eq_val))

eq_val = eq_val.replace(' ', '').replace('y=', '')
c = eq_val.split('x')

res = int(c[0])*int(x) + int(c[1])
print(res)