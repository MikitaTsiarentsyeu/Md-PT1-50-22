def check_str(str):
    
    upperCase = 0

    for i in str:
        if i.isupper() == True:
            upperCase += 1
    lowerCase = len(''.join(str.split())) - upperCase

    return print(f"{upperCase} upper case, {lowerCase} lower case")

check_str('The quick Brown Fox')

def is_prime(x):

    i=1
    a=[]

    while i*i <= x:
        if x%i == 0:
            a.append(i)
            if i != x//i:
                a.append(x//i)
        i += 1
        if len(a) > 2:
            break

    if len(a) > 2:
        return False
    else:
       return True

print(is_prime(787))

def get_ranges(args):

    a = []
    count = 0

    for i in range(0, len(args)-1):
        if args[i]+1 == args[i+1]:
            args[i] = '-'

    for j in range(len(args)):
        if args[j] == '-':
            count += 1
        else:
            if count > 0:
                if count == 1:
                    args[j-1] = args[j] - count
                    args[j] = ','+str(args[j])
                else:
                    args[j-1] = args[j] - count
                    args[j] = '_'+str(args[j])
            count = 0

    for y in range(0, len(args)):
        args[y] = str(args[y])

    a = ",".join(args)
    g = a.replace('-,', '')
    k = g.replace(',_', '-')
    p = k.replace(',,', ',')
    '-'.join(str(args))
  
    return print(p)

get_ranges([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,16,17,18,19,20])