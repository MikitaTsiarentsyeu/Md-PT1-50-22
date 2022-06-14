from functools import reduce

def cycle(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    cycle(l,f,i+1)

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# cycle(l, print)

def sq(num):
    print(num*num)

# cycle(l, sq)

sq = lambda num: print(num*num)
sq(2)
# cycle(l, sq)

cycle(l, lambda num: print(num*num))

test_str = "Abc Aac aaa ttt"
print(sorted(test_str.split(), key=lambda x: x.lower()))

coll = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(coll))
print(sorted(coll, key=lambda x: x[1]))

#lambda x: x[1]
# def f(x):
#     return x[1]

d = {"one":1, "two":2, "three":3}
print(sorted(d))
print(sorted(d.items(), key=lambda v: v[1]))



map_result = map(print, l)
print(map_result, type(map_result))

x = list(map_result)
print(x)

map_result = map(lambda x: x*x, l)
# print([(lambda x: x*x)(x) for x in l]) not optional
print([x for x in map_result])

map_result = map(lambda x: ((x*100)//3)**0.5, l)
print([x for x in map_result])

filter_result = filter(lambda x: x>4, l)
print([x for x in filter_result])

filter_result = filter(lambda x: x//10, l)
print([x for x in filter_result])

map_filter_result = map(lambda num: chr(num*10), filter(lambda x: x//10, l))
print([x for x in map_filter_result])

print(reduce(lambda x, y: x+y, l))

print(reduce(lambda x, y: x if x < y else y, l))

print(reduce(lambda x, y: f"{x}-{y}", l))

def outer(x):
    return lambda y: x*y

f = outer(3)
print(f(1), f(2), f(3))

l = ['1', '11', '12', '22', '2', '13', '30', '33']
print(sorted(filter(lambda x: int(x) % 2 == 0, l), key=int))