#1
L = [1, 2, [2, 4, [[7, 8], 4, 6]]]
def nested_sum(L):
    total = 0  
    for i in L:
        if isinstance(i, list):  
            total += nested_sum(i)
        else:
            total += i
    return total
print (nested_sum(L))
#2
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