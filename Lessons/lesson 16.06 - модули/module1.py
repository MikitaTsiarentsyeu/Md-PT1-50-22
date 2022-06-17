# import module2 as mdl2

# if __name__ == "__main__":
#     print(__name__)

#     module2 = "new text value"

#     print(mdl2.x)
#     mdl2.test_func_from_module2()

####################################

# x = "test"

# from module2 import x as x_from_module2, test_func_from_module2

# print(x)

# print(x_from_module2)

# test_func_from_module2()

##########################

x = "test val"

from module2 import *

print(x)
x.append(4)

test_func_from_module2()

x = "new test val"
print(x)