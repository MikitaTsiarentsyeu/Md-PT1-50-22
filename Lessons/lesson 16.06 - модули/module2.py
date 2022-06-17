print(__name__)

# x = "test value from module2"

x = [1,2,3]

def test_func_from_module2():
    print(f"hello from module2, the x value is {x}")

if __name__ == "__main__":
    test_func_from_module2()