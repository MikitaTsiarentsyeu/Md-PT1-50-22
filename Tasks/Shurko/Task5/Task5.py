
l = [1, 2, [2, 4, [[7, 8], 4, 6]]]

def sum_of_list(l):
    sum = 0
    for i in l:
        if not isinstance(i, list):
            sum = sum + i
            #print(sum)
        else:
            sum = sum + sum_of_list(i)
            #print(sum)
    return sum
print(sum_of_list(l))


i = 0
l = [0, 1]
def fibonacci(n):
    global l, i
    if n == 2:
        return print(l)
    else:
        l.append(l[i] + l[i+1])
        i +=1
    return fibonacci(n-1)    
fibonacci(10)

############# --- May be this version better? --- ################
def fibonacci(n):
    i = 0 
    l = [0, 1]
    def fib(n):
        nonlocal i, l
        if n == 2:
            return l
        else:
            l.append(l[i] + l[i+1])
            i +=1
        return fib(n-1)
    print(fib(n))
fibonacci(8)