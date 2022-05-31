def times(a:int, b:int):
    return a*b

print(times(2, 3))
print(times([2], 3))
print(times('[2]', 3))

def int_times(a:int, b:int) -> int:
    "the function will return multiplication of int values"
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(int_times(2, 3))
print(int_times([2], 3))
print(int_times('[2]', 3))

print([1,2,3] == [1,2,3])
print([1,2,3] == (1,2,3))

def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq((1,3,2), [1,2,3]))
print(eq(('1','3','2'), "123"))



# public int sum(int a, int b){
#     return a + b;
# }

# public int sum(int a, int b, int c){
#     return a + b + c;
# }

# sum(2, 3)
# sum(2, 3, 4)

def sum(a, b):
    return a + b

def sum(a, b, c):
    return a + b + c

sum(2,3)
