# def level1(l_number):
#     print(f"start of level {l_number}")
#     print(level2(l_number+1))
#     print(f"end of level {l_number}")
#     return l_number

# def level2(l_number):
#     print(f"start of level {l_number}")
#     print(level3(l_number+1))
#     print(f"end of level {l_number}")
#     return l_number

# def level3(l_number):
#     print(f"start of level {l_number}")
#     print(level4(l_number+1))
#     print(f"end of level {l_number}")
#     return l_number

# def level4(l_number):
#     print(f"start of level {l_number}")
#     print(f"end of level {l_number}")
#     return l_number

# print(level1(1))

def level1(l_number):
    if l_number > 4:
        return l_number
    print(f"start of level {l_number}")
    print(level1(l_number+1))
    print(f"end of level {l_number}")
    return l_number

# print(level1(1))

def print_n_times(text, n):
    while True:
        if n == 0:
            break
        print(text)
        n -= 1

def print_n_times(text, n):
    if n == 0:
        return n
    print(text)
    print_n_times(text, n-1)
    print(n)
    return n

print_n_times("To infinity and beyond!!!", 3)

# 4! = 1*2*3*4

def factorial(n):
    level = f"function {n}"
    if n == 1:
        return 1
    c = n*factorial(n-1)
    return c

print(factorial(4))

x = 123456

def digit_sum(n): #n = 123 -> 6
    if n == 0:
        return n
    c = n % 10
    return c + digit_sum(n//10)

digit_sum(123456)

def digit_sum(n):
    str_n = str(n)
    if len(str_n) == 1:
        return int(str_n)
    i = int(str_n[0])
    return i + digit_sum(int(str_n[1:]))

digit_sum(123456)

