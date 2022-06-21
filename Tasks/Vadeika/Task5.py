"""Task5."""

#  Task 5.1


def fib(n):

    if n == 0:  # Base event 1.
        return 0
    elif n == 1:  # Base event 2.
        return 1
    else:  # Recursion.
        return fib(n - 1) + fib(n - 2)


num = 10  # Input of the length of the Fibonacci sequence.

for i in range(num):
    print(fib(i), end=',')

#  Task 5.2

lst = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def sum_digits(lst_f):
    sum = 0

    for i in lst_f:
        if not isinstance(i, list):  # checking if i is a list.
            sum = sum + i  # if i is not a list, then add it to the sum
        else:
            sum = sum + sum_digits(i)  # sum from the next recursive calls.
    return sum


sum = sum_digits(lst)
print("sum of elements = ", sum)
