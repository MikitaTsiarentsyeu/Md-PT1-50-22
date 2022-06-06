def check_str(string):
    return(f'{len([i for i in string if i.isupper()])} upper case, {len([i for i in string if i.islower()])} lower case')



def is_prime(number): 
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True    

   


def get_ranges(list): 
    ranges = []
    for x in list:
        if not ranges:
            ranges.append([x])
        elif int(x)-prev_x == 1:
            ranges[-1].append(x)
        else:
            ranges.append([x])
        prev_x = int(x)
    return(", ".join(["-".join(map(str,[r[0], r[-1]] if len(r) > 1 else r)) for r in ranges]))