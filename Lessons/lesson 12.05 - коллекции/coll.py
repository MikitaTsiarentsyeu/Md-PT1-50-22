d = {}
print(type(d))

d = {"one": 1, 2: "two", 3.0: [1,1,1]}

print(d["one"])
print(d[3.0])
print(d.get(2, -1))
print(d.get(200, "not found"))
print(d.get(200, -1))
print(d.get(200))
# d[200]

d["test"] = 42
d["test"] = "test"

print("one" in d)
print("two" in d)
print("two" in d.keys())
print("two" in d.values())

print(('one', 1) in d.items())

print(d.pop("one"))
print(d)

print(d.popitem())
print(d)

del d[2]
print(d)

# print(d.keys()[0]) error
# del d.keys()[0] error

del d

s = {1:1, 2:2, 3:3}

s = {}
print(type(s))

s = set()
print(type(s))

s = {1, "two", 3.0}
print(s)

s = {1, "two", 3.0, 1, 1}
print(s)

s = list(set([1, "two", 3.0, 1, 1]))
print(s)

s = set("aabbbyyytttdddfff")

# print(s[0]) error
print(len(s))

x = [1,2,3]
y = [3,2,1]
print(x == y)
print(set(x) == set(y))
print(set('testtesttesttest') == set("set"))

x = {1,2,3,4,5}
y = {4,5,6,7}
print(x.union(y))

print(x.intersection(y))

print(set("test test test").intersection(set("set")))
print(set("test test test").union(set("set")))

x = {1,2,3}
y = {2,3}
print(x.issuperset(y))
print(y.issuperset(x))
print(y.issubset(x))

print(set("test test test").issuperset(set("set")))

s = set("123456789")
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s.pop())
print(s)

s = set("123456789")
s.add('10')
s.add('1')
print(s)

s.update([1,2,3,4,5,'1'])
print(s)

print(1 in s)
s.discard(1)
s.discard(1)
print(s)

s.remove(2)
print(s)
# s.remove(2) error

s.clear()
print(s)

del s

l = [[[[[[[[[["some very important value"]]]]]]]]]]
print(len(l[0]), l[0][0][0][0][0][0][0][0][0][0])

l = [[1,2,3], [4,5,6], [7,8,9]]
[1,2,3]
[4,5,6]
[7,8,9]
print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

t = ('test', l)
print(t)
t[1][1][1] = 5.0
print(t)
print(l)

d = {(1,2,3):"some values"}
print(d)

# d = {t:"test"} error
# s = {t, "test"} error