import time_decor as td

@td.time_decor
def loader(n=1000):
    res = 0
    for i in range(n):
        res+=i
    return res

loader(100000)
print(td.get_time())