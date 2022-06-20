def sum(lst):
    i = 0
    for elm in lst:
        if (type(elm) == type([])):
            i = i + sum(elm)
        else:
            i = i + elm
    return i
print("The sum is", sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        x = fib(n-1)
        x.append(sum(x[:-3:-1]))
        return x
print(fib(5))
print(fib(10))



