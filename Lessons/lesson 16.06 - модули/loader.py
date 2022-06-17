import timer

timer.start()

for i in range(1000000000):
    i = i*i

print(timer.finish())