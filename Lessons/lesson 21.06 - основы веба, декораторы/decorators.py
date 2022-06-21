def do_twice(func):
    def wrapper():
        print("start working on the task")
        func()
        print("the task is almost done")
        func()
        print("the task is done")
    return wrapper

@do_twice
def print_number_four():
    print(4)

# double_print_number_four = do_twice(print_number_four)

# double_print_number_four()

# print_number_four = do_twice(print_number_four)
print_number_four()

def do_twice(func):
    def wrapper(*args): # not very clear approach
        print(func(args[0], args[1]))
        print(func(args[1], args[0]))
    return wrapper

@do_twice
def sum(a,b):
    return a+b

sum(2,3,4,5,76,8,9,0,98764,321)