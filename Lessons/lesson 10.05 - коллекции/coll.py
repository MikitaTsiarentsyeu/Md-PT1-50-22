l = [1,"test",[3,"4"]]
print(type(l), len(l), l)

l = list("test string")
print(l)

print([1,2,3] + [4,5,6])
print([1]*5)

l = [1,2,3,4,5,6,7,8,9]
print(l[0], l[1], l[2])
print(l[0:6:2])
print(l[6:0:-2])
print(l[::-1])

l.append("ten")
print(l)
# l.append([1])

# l+"test" error

l.extend([11, 12])
print(l)

l.extend("test")
print(l)

l.insert(0, "zero")
print(l)

l.insert(13, 13)
print(l)

# l[55] error
l.insert(55, 13)
print(l)

l[0] = 0.0
print(l)

l[14:] = []
print(l)

x = l.pop()
print(x, l)

x = l.pop()
print(x, l)

x = l.pop()
print(x, l)

x = l.pop()
print(x, l)

# [].pop() error

x = l.pop(0)
print(x, l)

l.append(9)

l.remove(9)
print(l)

if 9 in l:
    l.remove(9)
    print(l)

del l[0]
print(l)

# del l[100] error
# print(l)

del l[2:5]
print(l)

l.clear()
print(l)

# [].clear()

del l
# print(l) error


t = ()
print(type(t))

t = (1)
print(type(t), t)

t = (1,)
print(type(t), t)

t = (1, "test", [])
print(type(t), t)

t = (1,2,3)+(4,5,6)
print(t)

print((1,)*5)

print(t[0])
print(t[1:3])

# t[0] = 89 error
# t.append(5) error

t = t[1:3]
print(t)

l = list(t)
print(l)

l.extend((1,2,3))
print(l)

t = tuple(l)
print(t)

# del t

d = {}
print(type(d))

d = {"one":56, "test":"some string", 'one':77}
print(d)

print(d["one"])
d["new object"] = 100
print(d)

print(d.keys())
print(d.values())
print(d.items())

d[("test", 6)] = "tuple value"
print(d)