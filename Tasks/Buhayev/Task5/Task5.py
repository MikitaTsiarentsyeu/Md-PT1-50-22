
l=[1, 2, [2, 4, [[7, 8], 4, 6]]]

def rsum(arr):
    if not isinstance(arr, list):
        return arr
    if arr == []:
        return 0
    return rsum(arr[0]) + rsum(arr[1:])

print(rsum(l))

rec = lambda x: sum(map(rec, x)) if isinstance(x, list) else x #some interesting implementation of flatten sum of list of lists


print(rec(l))



def fib(N):
    if N < 2: return N
    return fib(N - 1) + fib(N - 2)
    
    
print(*[fib(i) for i in range(10)], sep=', ')
    