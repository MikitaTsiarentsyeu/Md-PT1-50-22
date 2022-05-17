from datetime import datetime, time, date


user_mode = int(input('Enter 1 to see spelling of the current time.\nEnter 2 to see spelling of the time you entered.\nYour choice is: '))
while user_mode not in (1,2):
    print('Please enter only "1" or "2"')
    user_mode = int(input('Enter 1 to see spelling of the current time.\nEnter 2 to see spelling of the time you entered.\nYour choice is: '))

    
dict_numbers = {1:"один", 2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одиннадцать", 12:"двеннадцать", 13:"один", 14:"два", 15:"три", 16:"четыре", 17:"пять", 18:"шесть", 19:"семь", 20:"восемь", 21:"девять", 22:"десять", 23:"одиннадцать", 24:"двеннадцать"}
dict_hour = {1:"первого", 2:"второго", 3:"третьего", 4:"четвертого", 5:"пятого", 6:"шестого", 7:"седьмого", 8:"восьмого", 9:"девятого", 10:"десятого", 11:"одиннадцатого", 12:"двеннадцатого", 13:"первого", 14:"второго", 15:"третьего", 16:"четвертого", 17:"пятого", 18:"шестого", 19:"седьмого", 20:"восемого", 21:"девятого", 22:"десятого", 23:"одиннадцатого", 24:"двеннадцатого"}
dict_min = {45:'пятнадцати', 46:'четырнадцати', 47:'тринадцати', 48:'двенадцати', 49:'одиннадцати', 50:'десяти', 51:'девяти', 52:'восьми', 53:'семи', 54:'шести', 55:'пяти', 56:'четырех', 57:'трех', 58:'двух', 59:'одной', 1:'одна', 2:'две', 20:'двадцать', 30:'тридцать', 40:'сорок', 0:'', 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одиннадцать", 12:"двеннадцать", 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семнадцать', 18:'восемьнадцать', 19:'девятнадцать'}


if user_mode == 1:
    current_datetime = datetime.now()
    time_now = str(datetime.time(current_datetime))
    time_now = time_now.split(':')
    hh = int(time_now[0])
    mm = int(time_now[1])
                
else:
    user_time = str(input('Please enter time in format "hh:mm": '))
    (hh, mm) = user_time.split(':')
    hh = int(hh)
    mm = int(mm)
    
if mm == 0:
    if hh in (2, 3, 4, 14, 15, 16):
        print(f'{hh:02}:{mm:02} - {dict_numbers[hh]} часа ровно')
    elif hh in (0, 24):
        print(f'{hh:02}:{mm:02} - полночь')
    elif hh == 12:
        print(f'{hh:02}:{mm:02} - полдень')
    else:
        print(f'{hh:02}:{mm:02} - {dict_numbers[hh]} часов ровно')
        
if mm >= 1 and mm<=44 and mm != 30:
    m1 = mm//10
    m2 = mm%10
    if m2 == 1:
        print(f'{hh:02}:{mm:02} - {dict_min[m1*10]} {dict_min[m2]} минута {dict_hour[hh+1]}')
    elif m2 in (2, 3, 4):
        print(f'{hh:02}:{mm:02} - {dict_min[m1*10]} {dict_min[m2]} минуты {dict_hour[hh+1]}')
    elif mm >=3 and mm<=19:
        print(f'{hh:02}:{mm:02} - {dict_min[mm]} минут {dict_hour[hh+1]}')
    elif mm in (20, 30, 40):
        print(f'{hh:02}:{mm:02} - {dict_min[mm]} минут {dict_hour[hh+1]}')
    else:
        print(f'{hh:02}:{mm:02} - {dict_min[m1*10]} {dict_min[m2]} минут {dict_hour[hh+1]}')
    
if mm == 30:
    print(f'{hh:02}:{mm:02} - половина {dict_hour[hh+1]}')
    
if mm >=45 and mm<=59:
    if hh in (0, 12):
        print(f'{hh:02}:{mm:02} - без {dict_min[mm]} минут час')
    elif mm == 59:
        print(f'{hh:02}:{mm:02} - без {dict_min[mm]} минуты {dict_numbers[hh+1]}')
    else:
        print(f'{hh:02}:{mm:02} - без {dict_min[mm]} минут {dict_numbers[hh+1]}')