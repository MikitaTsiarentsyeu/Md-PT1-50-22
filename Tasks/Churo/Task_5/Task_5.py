#  1. Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
#l = [1, 2, [2, 4, [[7, 10, 8], 4, 6]]]
#l = [9]

def sum_recursion_list(l, counter = 0):
    for item in l:
        if type(item) == type([]):
            counter = counter + sum_recursion_list(item)
        else:
            counter = counter + item
        #print(item)
            #print(item)
    return counter
print(f"Sum of all elements of nested lists = ", sum_recursion_list(l))



# 2. Написать функцию для вычисления n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

n = 10   # номер элемента ряда Фибоначчи

def fib(n):               
    if n in (1, 2):
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)
#print(fib(n))  #значение элемента
print(f"{[fib(n) for n in range(n)]} Fibonacci series 'с 0' ")   
print(f"{[fib(n) for n in range(1,n+1)]} Fibonacci series 'no 0' ")


