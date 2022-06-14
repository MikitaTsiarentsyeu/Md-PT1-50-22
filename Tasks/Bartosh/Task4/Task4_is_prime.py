import math

def is_prime (n): 
    n_sqrt = int(math.sqrt(n))+1
    if n == 2:
        return False
    else:
        for i in range (2, n_sqrt):
            print (n%i, 'остаток')
            if n%i == 0:
                return False
        return True

