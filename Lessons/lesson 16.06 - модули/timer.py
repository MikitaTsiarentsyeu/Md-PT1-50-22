import time

def start():
    global start_time
    start_time = time.time()

def finish():
    return time.time() - start_time

