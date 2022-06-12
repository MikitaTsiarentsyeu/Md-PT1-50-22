from math import sqrt


def sum_element(lst):
    sum = 0
    for x in lst:
        if (type(x) == type([])):
            sum = sum + sum_element(x)
        else:
            sum = sum + x
    return sum

print(sum_element([1, 2, [2, 4, [[7, 8], 4, 6]]]))

def fib(n):
    if n < 2:
        return n

    lst = [0, 1]
    while len(lst) < n:
        lst.append(lst[-2] + lst[-1])

    return [str(x) for x in lst]

print(", ".join(fib(15)))