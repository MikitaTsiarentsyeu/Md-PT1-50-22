l = [1,2,3,4,5,6,7,8]

x = 3

m =(len(l)-1) // 2

if l[m] == x:
    print(f"we found it - {m}")
else:
    m =(len(l[:m+1])-1) // 2
    if l[m] == x:
        print(f"we found it - {m}")

def search(l, target, low=0, high=None):
    if not high:
        high = len(l)-1
    if high < low:
        return
    m = (low + high) // 2
    if l[m] == target:
        return m
    elif l[m] > target:
        return search(l, target, low, m-1)
    else:
        return search(l, target, m+1, high)
    

print(search(l, 7))