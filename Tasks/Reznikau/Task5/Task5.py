
def sum_elements(collection):
    """The function calculates the sum of all elements in the collection
    which are being contained on any levels of this collection."""
    n = 0
    for i in collection:
        if type(i) == type(0) or type(i) == type (0.4):
            n += i

        elif type(i) == type([]) or type(i) == type(()) or type(i) == type (set([])):
            n += sum_elements(i)
    
    return n

def fib(x, n = 1, l = [], val1 = 0, val2 = 1):
    """The function gets the collection of first Fibonacci numbers in n amount."""
    if n > x or x <= 0:
        return l
    
    if n == 1:
        l.append(val1)
        fib(x, n+1, l)
        return l

    if n == 2:
        l.append(val2)
        fib(x, n+1, l)
        return l

    if n > 2:
        new_val = val1 + val2
        l.append(new_val)
        fib(x, n+1, l, val2, new_val)
        return l


print(fib(5))
