import time

def time_decor(func):
    def wrapper(n):
        start = time.time()
        res = func(n)
        global t
        t = time.time() - start
        return res
    return wrapper

def get_time():
    return t