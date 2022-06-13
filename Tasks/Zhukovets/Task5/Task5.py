li = [1, 2, [2, 4, [[7, 8], [4, 6], 5], [5, 6, [2]]]]


def sum_of_list_elem(l: list):
    sum_ = 0
    for elem in l:
        if type(elem) == list:
            sum_ += sum_of_list_elem(elem)
        else:
            sum_ += elem
    return sum_


def fibonacci(n):
    """func without closure, but it doesn't return the string we need """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


number_of_calls = 5
print(*[fibonacci(i) for i in range(1, number_of_calls+1)], sep=',')


def fib_with_closure(number_of_iterations):
    def fib(n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    all_numbers = [str(fib(i)) for i in range(1, number_of_iterations + 1)]
    return ','.join(all_numbers)

print(fib_with_closure(10))

