from functools import reduce

def check_str(str):
    upper_count = reduce(lambda x, i: x + 1 if(i.isupper()) else x, str, 0)
    lower_count = len(str.replace(' ', '')) - upper_count
    print(f'{upper_count} upper case, {lower_count} lower case')


check_str('My mom Is Great')

def is_prime(number):
    if number % 2 == 0:
        return number == 2
    denominator = 3
    while denominator*denominator <= number and number % denominator != 0:
        denominator += 2
    return denominator*denominator > number

#check numbers
for i in range(2, 25):
    print(f"{i} - {is_prime(i)}")


arr = [1, 2, 3, 4, 5, 8, 9, 10, 14, 15, 16, 18,
       20, 21, 26, 28, 30, 33, 34, 35, 44, 45, 67]




def get_ranges(arr):
    start = arr[0]
    start_index = arr.index(start)
    for i in range(start_index, len(arr)):
        if start == arr[-1]:
            print_single_number(start)
            break 
        if arr[i]+1 == arr[i+1] and arr[i+1] == arr[-1]:
            print_range(start, arr[i+1])
            break
        if arr[i]+1 == arr[i+1]:
            continue  
        else:
            if start == arr[i]:
                print_single_number(start)
            else:
                print_range(start, arr[i])
            start = arr[i+1]

def print_single_number(n): print(f'{n}')
def print_range(n, m): print(f"{n}-{m}")

get_ranges(arr)
