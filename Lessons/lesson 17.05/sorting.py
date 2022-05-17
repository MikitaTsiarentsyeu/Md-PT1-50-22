l = [3,7,5,4,1,-2,2,8,9,5]

s = sorted(l)
print(s)

l = [10,9,8,7,6,5,4,3,2,1]
# l = sorted(l)

print(l)
x = 0
for j in range(len(l)-1):
    for i in range(len(l)-1-j):
        x += 1
        if l[i] > l[i+1]:
            print(l)
            l[i], l[i+1] = l[i+1], l[i]
print(l)
print(x)


l = [3,7,5,4,1,-2,2,8,9,5]
x = 0
for i in range(len(l)):
    m = i
    j = i+1
    while j < len(l):
        x += 1
        if l[j]<l[m]:
            m = j
        j += 1
    l[i], l[m] = l[m], l[i]

print(l)
print(x)

l.sort()