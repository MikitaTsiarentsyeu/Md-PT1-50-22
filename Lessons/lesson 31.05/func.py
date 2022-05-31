import math


def new_sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return a+b

print(new_sum(2,3))
print(new_sum(5,3))
print(new_sum(0,3))
print(new_sum(5,0))

def check_params(a, b):
    print(f"a={a}, b={b}")

check_params("test val 1", 5)
check_params(5, "test val 1")

def documented(a:int, b:str) -> str:
    """this is an example of documented function
        a - the first arg
        b - the second param
        returns some string
    """
    return a*b

print(documented(3,"test"))
print(documented("test",3))
print(documented(5,3))

def return_many(a, b):
    return a*3, b*2

x, y = return_many(4,6)
print(x, y)

# sign = '*'
# if sign == '*':
#     def math_func(a, b):
#         return a*b
# elif sign == '+':
#     def math_func(a, b):
#         return a+b        VERY BAD APPROACH

# def math_func(a, b):
#     return a*b

# def math_func(a, b):
#     return a+b 

def math_func(a, b, sign):
    if sign == "+":
        return a+b
    if sign == "*":
        return a*b
    
print(math_func(3,4, '*'))

def func_top_level():
    func_low_level()
    print("hello from the top level")

def func_low_level():
    print("hello from the low level")

# def func_top_level():

#     def func_low_level():
#         print("hello from the low level")

#     func_low_level()
#     print("hello from the top level") ANOTHER BAD APPROACH

func_top_level()
func_low_level()

def check_int(a:int):
    print(f"a = {a}")
    a += 2
    print(f"a = {a}")
    return a

x = 3
print(check_int(x))
print(x)

def check_list(a:list):
    print(f"a = {a}")
    a[0]+=2
    print(f"a = {a}")
    return a

x = [3]
print(check_list(x))
print(x)

x = [2,4,3,6,5,7,8]
print(sorted(x), x)
x.sort()
print(x)
