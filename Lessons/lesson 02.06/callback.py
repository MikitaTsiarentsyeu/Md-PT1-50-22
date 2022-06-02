import time, threading

def simple_test(x):
    print(f"hello, I'm very simple, my val is {x}")

def test(test_fucn, x):
    test_fucn(x)

test(simple_test, 4)

def show_text_ad():
    print("some ad here")

def show_symbolic_ad():
    print("@@@@@@#########$$$$$$$$%%%%%%%%%%%\n\n\n\n\n\n\n\n\n\n\n$%^&*&^%$#@#$%^&*(")

def timer(t, callback):
    callback()
    time.sleep(t)
    for i in range(100):
        print(i)
    callback()

def async_timer(t, callback):
    callback()
    threading.Timer(t, callback).start()
    for i in range(6000):
        print(i)

# timer(3, show_text_ad)
# timer(5, show_symbolic_ad)

# async_timer(2, show_symbolic_ad)
