#1
def check_str(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for i in s:
        if i.isupper():
           d["UPPER_CASE"]+=1
        elif i.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("Number of uppercase characters : ", d["UPPER_CASE"])
    print ("Number of lowercase characters : ", d["LOWER_CASE"])
check_str('The quick Brown Fox')
#2
def is_prime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True
print(is_prime(787))
#3
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