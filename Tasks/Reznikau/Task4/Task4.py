

def check_str(s:str) -> str:
    """The function takes the string and defines the quantity
    of letters in Lower and Upper register."""
    Upper = 0
    Lower = 0
    for l in s:
        lo = l.lower()
        up = l.upper()
        if l == lo and l != up:
            Lower += 1

        if l == up and l != lo:
            Upper += 1

    return f'{Upper} upper case{"" if Upper == 1 else "s"}, {Lower} lower case{"" if Lower == 1 else "s"}'


def is_prime(d:int) -> bool:
    """The function checks the figure exceed null is it prime or not."""
       
    for i in range(2, d-1):
        if d % i == 0:
            return False
    
    return True

def get_ranges(lst:list) ->str:
    """The function gets the list of unique integer figures sorted from low value to high
    and returns the string with short designation of the collection"""
    
    res = ''
    for i in range(len(lst)):
        if i == 0:
            res += str(lst[i])
        
        if i > 0:
            if not (lst[i] - lst[i-1] == 1):
                res += f", {lst[i]}"
                
            else:
                try:
                    if lst[i+1] - lst[i] == 1:
                        continue

                    else:
                        res += f"-{lst[i]}"

                except IndexError:
                    res += f"-{lst[i]}"

    return res
                


# Tests part:

# def is_number(str):
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False


# while True:
#     x = input()
#     if not is_number(x):
#         break
    
#     print(is_prime(int(x)))

# x = input("Please, enter the text:\n")
# print(check_str(x))

while True:
    string = input()
    if string == 's':
        break
    
    x = string.replace(' ', '').split(',')
    for i in range(len(x)):
        x[i] = int(x[i])

    print(get_ranges(x))