
def check_str(some_str):
    x, y = 0, 0
    for i in range(len(some_str)):
        if some_str[i].islower():
            x +=1
        if some_str[i].istitle():
            y +=1
    print(f"{y} upper case, {x} lower case" )
#check_str('The quick Brown Fox The quick Brown Fox The quick Brown Fox')

def is_prime(num: int):
    
    x = 2
    while num % x !=0:
        x +=1
    return num == x
    
#print(is_prime(11))

list_ = [0, 1, 2, 3, 4, 7, 8, 10]




l = [0, 1, 2, 3, 4, 7, 8, 10]
l = [4,7,10]
#l = [2, 3, 8, 9]

def get_range(l: list):  # This part of task4 in progress
    my_srt = ""
    new = list()
    new.append(l[0])
    i = 1
    j = 0
    while i < len(l):
        if (l[i]-1) == l[i-1]:
            new[j+1:j+3] =[l[i]]
        
        else: 
            new.append(l[i])
            j +=2
        i +=1
    my_srt = [str(n) for n in new]
    return my_srt
print(get_range(l))




