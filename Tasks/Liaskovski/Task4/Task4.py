l = "The quick Brown Fox"
def check_str(l):
    return (f'upper case: {sum(map(str.isupper, l))}, lower case: {sum(map(str.islower, l))}')
print(check_str(l))


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True
print(is_prime(787))
print(is_prime(777))


def get_ranges(numberlist):
    prev_number = min(numberlist) if numberlist else None
    pagelist = list()

    for number in sorted(numberlist):
        if number != prev_number+1:
            pagelist.append([number])
        elif len(pagelist[-1]) > 1:
            pagelist[-1][-1] = number
        else:
            pagelist[-1].append(number)
        prev_number = number

    return ','.join(['-'.join(map(str,page)) for page in pagelist])

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))
