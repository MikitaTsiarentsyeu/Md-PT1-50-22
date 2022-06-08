for i in range(1,101):
    res = ""
    if i % 3 == 0:
        res+="fizz"
    if i % 5 == 0:
        res+="buzz"
    if not res:
        res = i
    print(res)

l = [("fizz"*(i % 3 == 0) + "buzz"*(i % 5 == 0) or i) for i in range(1,101)]
print(l)

FIZZ = "brizz"
buzz = "buzz"
rem_3 = 3
rem_5 = 5

FIZZ = "fizz"

def rem(i, n):
    return i % n == 0

def compose(s, n):
    return s*n

def main():
    print([(compose(FIZZ, rem(i,rem_3)) + compose(buzz, rem(i,rem_5)) or i) for i in range(1, 101)])

main()