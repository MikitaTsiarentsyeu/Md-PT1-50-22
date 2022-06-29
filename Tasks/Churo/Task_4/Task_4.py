# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.

text = "The quick Brown Fox"

def check_str(text):
    x, y = [], []
    for i in text:
        if i.isupper():
            x.append(i)
        if i.islower():
            y.append(i)
    print (f"\n\n{len(x)} upper case, {len(y)} lower case\n\n")
    #print(x)
    #print(y)
check_str(text)



# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.

import math

user_input = int(input("Please enter a positive number '> 0' \n"))     

def is_prime(user_input):
    if user_input <= 0:
        print("\nincorrect input, number '<= 0' \n")
        exit()
    elif user_input == 1:
        print("False\n")
        exit()
    elif user_input == 2:
        print("True\n")
        exit()
    elif user_input > 2:
        i = 2
        limit = int(math.sqrt(user_input))
        while i <= limit:
            if user_input % i == 0:
                print("False\n")
                exit()
            i += 1
        print("True\n")
is_prime(user_input)



# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, отсортированных по возрастанию, и которая этот список “сворачивает”.

def get_ranges(l):    
    s = f"{l[0]}"
    res = False        
    for i in range(len(l)-1):             
        if l[i+1]-l[i] == 1:
            res = True            
        else:
            if res:
               s += f"-{l[i]}, {l[i+1]}"
            else:
                s += f", {l[i+1]}"
            res = False
    if res:
        s+= f"-{l[-1]}"

    return s
        
print(get_ranges([3, 5, 6, 7, 10, 14, 21, 28, 30, 31, 32]))

