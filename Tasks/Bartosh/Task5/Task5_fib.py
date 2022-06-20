def fib(n, count=2, l=[0,1]):
    if n==1:
        return (l[0])
    elif n == 2:
        return (l)
    elif n==count:
        return (l)
    else:    
        i= l[-1]+l[-2]
        l.append(i)
        count+=1
        return fib(n,count)