def func(x, y):
    print(f"x - {x}, y - {y}")

x, y = 3, 4

func(x, y)
func(y="test y val", x="test x val")

def sum(arg1=1, arg2=2, arg3=3):
    return arg1+arg2+arg3

print(sum(1,2,3))
print(sum())
print(sum(3,4))
print(sum(arg2=3,arg3=4))

def sum(*args):
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5,6,7,8,9,1,2,4,45,3,2,2,3,45,65,3,2,2,3,4,5))
l = [1,2,3,4,5]
print(sum(*l))

print(1,2,3,4,5,6,8,9,0,-90)

def sum(**kwargs):
    res = 0
    for i in kwargs.values():
        res += i
    return res

d = {"one":1, "two":2, "three":3}
print(sum(**d))

print(sum(one=1, two=2, three=3))
# print(sum(1=1, 2=2, 3=3)) error, the args names must be string literals

def my_print(*args, **kwargs):
    print(*args, sep=kwargs["sep"], end=kwargs["end"])

def my_print(x,y,z,*args,**kwargs):
    print(x,y,z)
    print(*args, sep=kwargs["sep"], end=kwargs["end"])

my_print(1,2,3,4,5,6,sep=',',end='.')