def sum_num(list_num):
    sum = 0
    for x  in list_num:
        if not isinstance (x, list):
            sum += x
        else:
            sum += sum_num(x)
    return sum

print(sum_num([1, 2, [2, 4, [[7, 8], 4, 6]]]))   



fib_num = [0, 1]
def fib(n):
	if n<=len(fib_num) and n>0:
		return fib_num[n-1]
	else:
		fn = fib(n-1) + fib(n-2)
		fib_num.append(fn)
		return fn
        
fib(5)
print(', '.join(map(str,fib_num)))