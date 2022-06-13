def check_str(string: str):
    worker_string = string.replace(' ', '').replace(',', '').replace('.', '').replace(':', '')
    upper_c = sum([i.isupper() for i in worker_string])
    return f"{upper_c} - upper case, {len(worker_string)-upper_c} - lower case"


def is_prime(number: int):
    if number % 2 == 0:
        return False
    d = 3
    while d * d < number:
        if number % d == 0:
            return False
        d += 2
    return True


def is_prime2(number: int):   # another non-obvious option
    if number % 2 == 0:
        return False
    d = 3
    while d * d < number and number % d != 0:
        d += 2
    return d * d > number


def get_ranges(li: list):
    elements = []
    for i in li:
        if i == li[-1]:
            elements.append(i)
            break
        elif i == li[0] or elements[-1] == ', ':
            elements.append(i)
            if elements[-1] != li[li.index(i) + 1] - 1:
                elements.append(', ')
            else:
                elements.append('-')
        else:  # elements[-1] == '-'
            if i != li[li.index(i) + 1] - 1:
                elements.append(i)
                elements.append(', ')
    return ''.join([str(elem) for elem in elements])


test_string = "Some Test String with Upper case And Lower CaSe symbols he::::,,,.llO, World!"
print(check_str(test_string))
print(is_prime(71))
print(is_prime2(155))
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10, 11, 15, 114, 115, 120]))