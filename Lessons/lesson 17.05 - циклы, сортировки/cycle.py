# while True:
#     print("I'm going!!!!!")
#     print("--------------")

x = 0

while x < 10:
    print(x)
    x += 1
else:
    print("the end of cycle")

l = [1,2,3,4,5,6,7,8,9,10]

for i in l:
    print(i)

for i in range(22,33,2):
    print(i)

for i in range(len(l)-1):
    print(l[i]+l[i+1])

print(i)

i = 0
while i < len(l) and i < 5:
    print(l[i])
    i += 1

for i in set(l):
    print(i)

d = {1:"one", 2:"two", 3:"three"}
for i in d:
    print(i)

for i in d.values():
    print(i)

for i in d.items():
    print(i)

for k, v in d.items():
    print(k, v)

# i = 0
# for e in ["one", "two", "three"]:
#     print(i, e)
#     i+=1

for i, e in enumerate(["one", "two", "three"]):
    print(i, e)

l = [[1,2,3], [4,5,6], [7,8,9]]
for i, e in enumerate(l):
    print(f"{i+1} line:")
    for j in e:
        print(j)

l = [1,2,3,4,5,6]
for i in l:
    print(i)
    print(l.pop())
print(l)

# l = [1]
# for i in l:
#     l.append(i)
#     print(l)

x = 0
while True:
    if x == 9:
        break
    x += 1
    if x % 3 == 0:
        print(f"{x} value skipped")
        continue
    print(f"the value is {x}")
else:
    print("hello from the else")

x = 0
while x<10:
    print(x)
    x += 1
else:
    print("hello from the else")

for i in range(10):
    my_new_list = []
    my_new_list.append(i)

print(my_new_list)

for i in range(10):
    if i == 3 or i == 6:
        continue
    if i == 7:
        break
    print(i)
else:
    print("hello from the else")

for i in range(10): pass
print(i)

for i in range(10)[::-1]:
    print(i)

l = [1,2,3,4,5,6]
x = len(l)-1
while x > -1:
    print(l[x])
    x -= 1

print("the end")