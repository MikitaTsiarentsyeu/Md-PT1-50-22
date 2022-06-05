def check_str (user_str):
    lo, up = 0, 0
    for i in user_str:
        if ord(i) >=97 and ord(i) <= 122:
            lo += 1
        if ord(i) >=65 and ord(i) <= 90:
            up += 1
    return print(f'{up} upper case, {lo} lower case')



def is_prime (user_number):
        
    if user_number % 2 == 0:
        return False
    
    for i in range (3, int(user_number**0.5)+1, 2):            
        if user_number % i == 0:
            return False
    
    return True



def get_ranges (user_list):
    serv_list = []
    targ_str = ''
    serv_list.append(user_list[0])
    targ_str += f'{user_list[0]}'
    for i in range (1, len(user_list)):
        if user_list[i] != user_list[i-1] + 1:
            if user_list[i-1] not in serv_list:
                serv_list.append(user_list[i-1])
                targ_str += f'-{user_list[i-1]}'
            serv_list.append(user_list[i])
            targ_str += f', {user_list[i]}'
    if user_list[-1] not in serv_list:
        serv_list.append(user_list[-1])
        targ_str += f'-{user_list[-1]}'
                
    return targ_str


user_str = input('enter string please: ')
check_str (user_str)

user_number = int(input('enter number please: '))
print(is_prime (user_number))

user_list = [int(i) for i in input('enter numbers, sorted ascending, separated by space: ').split()]
print(get_ranges(user_list))