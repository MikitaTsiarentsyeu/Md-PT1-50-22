
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
        return l
    else:
        x = l[i] + l[i+1]
        l.append(x)
        i +=1
    return fibonacci(n-1)    
fibonacci(5)
print(l)

    








