def sum_func(x, y):
    return x+y

def print_sum_func(x, y):
    print(x+y)

def test_func(x, y):
    x = y
    print(x)

r1 = sum_func(2,4)
r2 = sum_func(5,6)
print(r1, r2)

print_sum_func(4,6)

x = 4
test_func(x, 6)
print(x)