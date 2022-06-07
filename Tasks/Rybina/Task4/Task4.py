from math import sqrt    

def check_str(string):
    string = string.replace(" ", "")
    up = 0
    for i in string:
        if i.isupper():
            up += 1
            continue
    return(f"{up} upper case, {len(string)-up} lower case")


def is_prime(n):
    k = 0
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
          k += 1
    if k > 0:
        return False
    else:
        return True

def get_ranges(list):
    new_list = []
    for i in list:
        if list.index(i) == 0:
            new_list.append(str(i))
        elif list.index(i) == len(list)-1:
            last_char = list[len(list)-1]
        elif i == (list[list.index(i)-1] + 1) and i != (list[list.index(i)+1] - 1):
            new_list.append("-")
            new_list.append(str(i))
            new_list.append(", ")
        elif i != (list[list.index(i)-1] + 1) and i == (list[list.index(i)+1] - 1):
            new_list.append(str(i))
        elif i != (list[list.index(i)-1] + 1) and i != (list[list.index(i)+1] - 1):
            new_list.append(", ")
            new_list.append(str(i))
            new_list.append(", ")
    if new_list[-1] == ", ":
        new_list.pop()
    if last_char == int(new_list[-1])+1:
        new_list.append("-")
        new_list.append(str(last_char))
    else:
        new_list.append(", ")
        new_list.append(str(last_char))
    new_list = "".join(new_list).replace(", ,", ",")
    return new_list 

