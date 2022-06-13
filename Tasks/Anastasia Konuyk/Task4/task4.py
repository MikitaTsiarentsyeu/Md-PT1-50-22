def check_str(string):
    return (f'{sum(map(str.isupper, string))} upper case, {sum(map(str.islower, string))} lower case')


def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def get_ranges(user_list):
    rolled_list = []
    for number in user_list:
        if number != user_list[0] + 1:
            rolled_list.append([number])
        elif len(rolled_list[-1]) > 1:
            rolled_list[-1][-1] = number
        else:
            rolled_list[-1].append(number)
        user_list[0] = number
    return (', '.join(['-'.join(map(str, part)) for part in rolled_list]))
