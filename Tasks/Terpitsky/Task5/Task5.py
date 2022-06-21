<<<<<<< Updated upstream
def list_summ(my_list, ready_list = [], ready_summ = [0]):
=======
def list_summ(my_list, ready_summ = [0]):
>>>>>>> Stashed changes
    for i in my_list:
        if type(i) == list:
            list_summ([*i])
        else:
            ready_summ[0] += i
<<<<<<< Updated upstream
            ready_list.append(i)
=======
>>>>>>> Stashed changes
    return f'sum of all elements: {ready_summ[0]}'

def fib(n, ready_list = [0,1]):
    if n == 0:
        return
    ready_list.append(ready_list[-1] + ready_list[-2])
    fib(n - 1)
    return ready_list[:-2]


<<<<<<< Updated upstream
print(list_summ([1,1,[],1,4,[1,1],1,1,[1,[[[[1]]]],1],1,1,1,3,[[[[]]]],2,[[2]]]))

print(fib(56))
=======
print(list_summ([1,1,[],1,4,[1,1],1,1,[1,[[[[1]]]],1],1,1,1,3,[[[[]]]],2,[[6]]]))

print(fib(100))
>>>>>>> Stashed changes




