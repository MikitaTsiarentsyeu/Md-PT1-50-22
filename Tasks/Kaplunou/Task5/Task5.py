res=0

def list_sum(l):
    
    for i in l:
        if type(i)!=list:
            global res
            res += i
        else:
            list_sum(i)
    return res
    
print(list_sum([1,3,1,[[1, [5,6]], 2, 1]]))

a, b = 0, 1
arr=[0]

def fibbonachi(n):
    if n == 0:
        return None
    if len(arr)==n:
        return arr
    global a, b
    a, b = b, a + b
    arr.append(a)
    fibbonachi(n)
    return arr

print(fibbonachi(7))

    