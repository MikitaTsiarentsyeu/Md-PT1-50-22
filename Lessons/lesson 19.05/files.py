f = open("test.txt", 'w')
# print(f)
f.write("test line number 2")
f.close()

with open("test.txt", 'w') as f:
    f.write("test line number 3 with with\n")
    f.writelines([f"line-{x}\n" for x in [1,2,3]])

with open("test.txt", 'r') as f:
    for line in f:
        print(line)
    f.seek(10)
    # print(f.read())
    print(f.readlines())
    # while True:
    #     x = f.read(1)
    #     print(x)
    #     if not x:
    #         break
    # print(f.readline())
    # print(f.readline())
    # print(f.read(30))
    # print(f.read(30))
    # print(f.read())

with open("test.txt", 'a') as f:
    f.seek(0)
    f.write("test line from 'a' mode\n")
    f.writelines([f"line-{x}\n" for x in [1,2,3]])

with open("test.txt", 'r+') as f:
    f.seek(10)
    # print(f.read())
    f.write("test write from r+\n")
    print(f.read())

with open("test.txt", 'a+') as f:
    f.seek(0)
    f.write("another append")
    print(f.read())

with open("test.txt", 'w+') as f:
    f.write("another write")
    f.seek(0)
    f.write("test")
    print(f.read())

print("the end")
