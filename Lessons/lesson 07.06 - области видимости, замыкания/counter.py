counter_base = 0

# def counter(n): DEPENDENT COUNTERS
#     global counter_base
#     counter_base = n
#     def inner():
#         global counter_base
#         counter_base += 1
#         return counter_base
#     return inner

def counter(n):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner
    
f = counter(100)
g = counter(1)

print(f())
print(f())
print(f())
print(g())
print(g())
print(g())
