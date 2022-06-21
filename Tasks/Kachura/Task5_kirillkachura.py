def fib (n):
    def fibonacci (n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fibonacci(n-1)+fibonacci(n-2)
    x = []
    for i in range (n):
        x.append(fibonacci(i))
    return x

print(fib(10))

def list_sum (l):
    sum = 0
    for i in l:
        if type(i) == int:
            sum += i
        else:
            sum += list_sum (i)
    return sum

print(list_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))