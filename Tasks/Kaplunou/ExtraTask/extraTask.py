b = 'thrirteen one three twelve fourteen eighteen nineteen three four eleven six'
a = [" ", "one", "two", "three", "four", "five", "six", "seven", "eigth", "nine", "ten", "eleven",
 "twelve", "thrirteen", "fourteen", "fiveteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
b=b.split(' ')
for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            b.append(a.index(a[j]))
b = list(set(b[len(b)//2::]))
b.sort()
print(b)

d=[]
h=0
c=0

for k in range(0, len(b)-1):
    c=b[k]
    h=b[k+1]
    if k%2==0:
        d.append(c*h)
    else:
        d.append(c+h)    
print(d)

even=[]
for u in b:
    if u%2==0:
        even.append(u)
print(even)