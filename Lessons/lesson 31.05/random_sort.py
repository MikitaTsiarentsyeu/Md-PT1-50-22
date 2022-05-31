import random

l = [3,2,5,4,7,6,8,9,1,10,11]

i = random.randint(0,len(l)-1)
j = random.randint(0,len(l)-1)

print(l)

l[i], l[j] = l[j], l[i]

print(l)

def sort(l):
    count = 0
    n = len(l)
    while not check_sorting(l):
        i = generate_index(n)
        j = generate_index(n)
        while i == j:
            j = generate_index(n)
        swap(l, i, j)
        count += 1
    return count

def generate_index(n):
    return random.randint(0,n-1)

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def check_sorting(l): 
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            return False
    return True

    # if sorted(l) == l: funny way to do it
    #     return True
    # return False

print(sort(l))
print(l)