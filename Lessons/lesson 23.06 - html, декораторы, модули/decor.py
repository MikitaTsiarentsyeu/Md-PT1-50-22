def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def add_comments(func):
    def wrapper(a,b,c=False):
        print("start of the function")
        func()
        print("end of the function")
    return wrapper

@do_twice
@add_comments
def test_func(x, y):
    print("I'm doing something useful")

test_func()