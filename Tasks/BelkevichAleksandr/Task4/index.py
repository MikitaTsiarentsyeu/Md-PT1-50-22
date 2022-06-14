def check_str():
    return f'{sum(map(str.isupper, "The quick Brown Fox"))} upper case, {sum(map(str.islower, "The quick Brown Fox"))} lower case'

print(check_str()) # -> 3 upper case, 13  lower case



def is_prime(number):
    return all(number % i for i in range(2, number))

print(is_prime(787)) # -> False
print(is_prime(777)) # -> True



def get_ranges(lst):
    numbers = []
    for x in lst:
        if x == lst[0] or numbers[-1] == ", " or x == lst[-1]:
            numbers.append(str(x))
            if x == lst[-1]:
                continue
            if x == lst[lst.index(x) + 1] - 1:
                numbers.append("-")
            if x != lst[lst.index(x) + 1] - 1:
                numbers.append(", ")
        elif x != lst[lst.index(x) + 1] - 1:
            numbers.append(str(x))
            numbers.append(", ")
        
    return "".join(numbers)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10])) #  ->  "0-4, 7-8, 10"
print(get_ranges([4,7,10]))                  # -> "4, 7, 10"
print(get_ranges([2, 3, 8, 9]))              # -> "2-3, 8-9"