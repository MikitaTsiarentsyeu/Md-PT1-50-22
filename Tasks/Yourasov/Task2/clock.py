import datetime

while True:

    working_mode = input('Please choose working mode: \n enter "c" for choose current time or "m" to enter the time manually - ')

    if working_mode == 'c':
        current_time = datetime.datetime.now()
        time_hh = current_time.hour
        time_mm = current_time.minute

    elif working_mode == 'm':
        manual_time = input('Please enter time in format hh:mm - ')
        if len(manual_time) != 5:
            print('Incorrect time format')
            continue
        if manual_time[2] != ':':
            print('Incorrect sign for dividing hours and minutes')
            continue
        if not manual_time[:2].isdigit() or not manual_time[3:].isdigit():
            print('Wrong. Please enter time in numbers in format hh:mm')
            continue
        time_hh = int(manual_time.split(':')[0])
        time_mm = int(manual_time.split(':')[1])
        if time_hh > 24:
            print('Incorrect hours value')
            continue
        if time_hh == 24 and time_mm > 0:
            print('Incorrect minutes value for 00 hours')
            continue
        if time_mm > 59:
            print('Incorrect minutes value')
            continue
    else:
        print('Please correct choose working mode.')
        continue
    break

if 12 < time_hh:
    time_hh -= 12

dict_num = {1:('час', 'первого', '', 'одна', 'одной'),
    2:('два', 'второго', '', 'две', 'двух'),
    3:('три', 'третьего', '', 'три', 'трех'),
    4:('четыре', 'четвертого', '', 'четыре', 'четырех'),
    5:('пять', 'пятого', '', 'пять', 'пяти'),
    6:('шесть', 'шестого', '', 'шесть', 'шести'),
    7:('семь', 'седьмого', '', 'семь', 'семи'),
    8:('восемь', 'восьмого', '', 'восемь', 'восьми'),
    9:('девять', 'девятого', '', 'девять', 'девяти'),
    10:('десять', 'десятого', '', 'десять', 'десяти'),
    11:('одиннадцать', 'одиннадцатого', '', 'одиннадцать', 'одиннадцати'),
    12:('двенадцать', 'двенадцатого', '', 'двенадцать', 'двенадцати'),
    13:('час', 'первого', '', 'тринадцать', 'тринадцати'),
    14:('', '', '', 'четырнадцать', 'четырнадцати'),
    15:('', '', '', 'пятнадцать', 'пятнадцати'),
    16:('', '', '', 'шестнадцать', 'шестнадцати'),
    17:('', '', '', 'семнадцать', 'семнадцати'),
    18:('', '', '', 'восемнадцать', 'восемнадцати'),
    19:('', '', '', 'девятнадцать', 'девятнадцати'),
    20:('', '', '', 'двадцать', ''),
    30:('', '', '', 'тридцать', ''),
    40:('', '', '', 'сорок', '')}

list_word = ('час ровно', 'часа ровно', 'часов ровно', 'минута', 'минуты', 'минут')

if time_mm == 0:
    if time_hh == 0 or time_hh == 24:
        print('полночь')
    elif time_hh == 12:
        print('полдень')
    elif 1 < time_hh < 5:
        print(dict_num[time_hh][0], list_word[1])
    elif 4 < time_hh < 13:
        print(dict_num[time_hh][0], list_word[2])
    else:
        print(list_word[0])

elif time_mm <= 20:
    if time_mm == 1:
        print(dict_num[time_mm][3], list_word[3], dict_num[time_hh + 1][1])
    elif 1 < time_mm < 5:
        print(dict_num[time_mm][3], list_word[4], dict_num[time_hh + 1][1])
    elif time_mm > 4:
        print(dict_num[time_mm][3], list_word[5], dict_num[time_hh + 1][1])

elif time_mm == 30:
    print('половина', dict_num[time_hh + 1][1])

elif 20 < time_mm < 45:
    if (time_mm % 10) == 1:
        print(dict_num[time_mm // 10 * 10][3], dict_num[time_mm % 10][3], list_word[3], dict_num[time_hh + 1][1])
    if 1 < (time_mm % 10) < 5:
        print(dict_num[time_mm // 10 * 10][3], dict_num[time_mm % 10][3], list_word[4], dict_num[time_hh + 1][1])
    if (time_mm % 10) > 4:
        print(dict_num[time_mm // 10 * 10][3], dict_num[time_mm % 10][3], list_word[5], dict_num[time_hh + 1][1])

elif time_mm >= 45:
    if (60 - time_mm) == 1:
        print('без', dict_num[1][4], list_word[4], dict_num[time_hh + 1][0])
    else:
        print('без', dict_num[60 - time_mm][4], list_word[5], dict_num[time_hh + 1][0])
