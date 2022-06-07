import os

print(os.name)

print(os.sep)

r"test level 1\test level 2\test level 3\test.txt"

path = ["test level 1", "test level 2", "test level 3", "test.txt"]
# if os.name == "nt":
#     print("\\".join(path))
# else:
#     print("/".join(path))

print(os.sep.join(path))

x = os.path.join("level 1", "level 2")
print(x)

print(os.getcwd())

# os.makedirs(x)
# os.chdir(x)
# print(os.getcwd())

print(os.listdir())
print(os.walk(os.getcwd()))
for l in os.walk(os.getcwd()):
    print(l)

os.removedirs(x)