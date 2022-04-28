x = 110

if x > 0:
    print("the number is positive")
elif x == 0:
    print("the number is zero")
else:
    print("the number is negative")

print("the number is positive") if x > 0 else print("the number is zero") if x == 0 else print("the number is negative")

if x >= 0:
    if x == 0:
        print("the number is zero")
    else:
        print("the number is positive")
else:
    print("the number is negative")



if x == 1:
    print("one")
elif x == 2:
    print("two")
elif x == 3:
    print("three")
elif x == 4:
    print("four")
elif x == 5:
    print("five")
elif x == 6:
    print("six")
else:
    print("text representation was not found")

print("the end")

print("it's true") if not True else print("it's false")

x = True if not True else False
print(x)

x = '''test
    test
test'''
print(x)

"""
test
test
test
"""