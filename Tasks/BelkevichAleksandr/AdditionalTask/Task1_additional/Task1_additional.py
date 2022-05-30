lst = []

for _ in "five thirteen two eleven seventeen two one thirteen ten four nineteen".split(" "):
    lst.append({"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, 
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, 
    "eighteen": 18, "nineteen": 19, "twenty": 20}.get(_))

print(lst)

lst = set(lst)

print(lst)

lst = sorted(lst)

print(lst)

for _ in lst:
    if _ == lst[-1]:
        break
    elif lst.index(_) % 2 == 0:
        print(f"multiplication index {lst.index(_)} and {lst.index(_) + 1} {_ * lst[lst.index(_) + 1]}")
    else:
        print(f"sum index {lst.index(_)} and {lst.index(_) + 1} {_ + lst[lst.index(_) + 1]}")


lst.insert(0, 0)

for _ in lst:
    if _ % 2 != 0:
        lst[0] += _

print(lst[0])
