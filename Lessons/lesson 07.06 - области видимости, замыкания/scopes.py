for i in range(5):
    i+=1

print(i)

x = 100
print(f"global level 1 x{x}")

[x for x in range(1000)]
print(x)

def scope_test():
    # print(f"scope_test level 1 x{x}")
    x = 44
    print(f"scope_test level 1 x{x}")
    x = 55
    print(f"scope_test level 2 x{x}")

def global_access():
    print(f"global_access level 1 x{x}")

global_access()
scope_test()
print(f"global level 2 x{x}")
x = 200
print(f"global level 3 x{x}")

print("---------------------")

test_val = 100

def check_val_1():
    test_val = 200
    print(f"check_val_1 {test_val}")

def check_val_2():
    global test_val
    test_val = 300
    print(f"check_val_2 {test_val}")

def check_val_3(test_val):
    # global test_val -> ERROR
    test_val = 400
    print(f"check_val_3 {test_val}")

check_val_1()
print(f"global {test_val}")
check_val_2()
print(f"global {test_val}")
check_val_3(55)
print(f"global {test_val}")

test_list = [1,2,3]

def check_list():
    test_list = []
    test_list.append(4)

check_list()
print(test_list)


def outer():
    test_val = 500
    def inner():
        nonlocal test_val
        test_val = 600
        print(test_val)
    inner()
    print(test_val)

outer()
print(test_val)