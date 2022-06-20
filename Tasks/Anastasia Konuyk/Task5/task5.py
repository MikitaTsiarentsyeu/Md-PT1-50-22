def summa(a):
    return a if type(a) is int else sum([summa(b) for b in a])
print(summa([1, 2, [2, 4, [[7, 8], 4, 6]]]))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter the number of members: "))
print(str([fibonacci(i) for i in range(n)]).strip('[]'))
