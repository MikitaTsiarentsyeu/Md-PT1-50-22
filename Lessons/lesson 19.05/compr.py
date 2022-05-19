import math

l = [1,2,3,4,5,6,7,8,9,10]
s = {1,2,3,4,5,6,7,8,9,10}
d = {1:"one", 2:"two", 3:"three"}

print([x for x in d.items()])
print(list(d.items()))

res = [x for x in range(20)]
# res = list(range(20))
# res = []
# for x in range(20):
#     res.append(x)
print(res)

res = [math.sin(x*math.pi)**0.5 for x in range(20)]
print(res)

# res = []
# for x in range(20):
#     res.append(math.sin(x*math.pi)**0.5)
# print(res)

print([x*100 for x in range(20) if x != 3 if x != 6 if x != 9])
print([x*100 for x in range(20) if x != 3 and x != 6 and x != 9])

res = []
for x in range(10):
    for y in range(10):
        res.append(f"{x}-{y}")
# print(res)

print([f"{x}-{y}" for x in range(10) for y in range(10)])

l = [[1,2,3], [4,5,6], [7,8,9]]
for x in l:
    for y in x:
        print(y)

print([y for x in l for y in x])

d = {str(x):x*x for x in range(10) if x != 4}
print(d)

d = {}
for x in range(10):
    if x != 4:
        d[str(x)]=x*x

s = {str(x) for x in range(10) if x != 4}
print(s)

d = {v:k for k, v in d.items()}
print(d)

l = [print(x) for x in range(10)]
print(l)

[print(x) for x in range(10)]

for x in range(10):
    print(x)