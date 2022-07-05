def sum_elements(l):
    sum_elem = 0
    for i in l:
        if isinstance(i, list) is False:
            sum_elem += i
        else:
            sum_elem += sum_elements(i)
    return sum_elem
print(sum_elements([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the number of elements: "))
print(", ".join(str(fibonacci(x)) for x in range(n)))

