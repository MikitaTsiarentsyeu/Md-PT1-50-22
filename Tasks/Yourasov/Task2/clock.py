import datetime

working_mode = input('Please choose working mode: \n enter "c" for choose current time or "m" to enter the time manually - ')

if working_mode == 'c':
    current_time = datetime.datetime.now()
    time_hh = int(current_time.hour)
    time_mm = int(current_time.minute)

elif working_mode == 'm':
    manual_time = input('Please enter time in format hh:mm - ')
    if len(manual_time) != 5:
        print('Incorrect time format')
        quit()
    elif manual_time[2] != ':':
        print('Incorrect sign for dividing hours and minutes')
        quit()
    elif not manual_time[:2].isdigit() or not manual_time[3:].isdigit():
        print('Wrong. Please enter time in numbers in format hh:mm')
        quit()
    time_hh = int(manual_time.split(':')[0])
    time_mm = int(manual_time.split(':')[1])
    if time_hh > 24:
        print('Incorrect hours value')
        quit()
    elif time_hh == 24 and time_mm > 0:
        print('Incorrect minutes value for 00 hours')
        quit()
    elif time_mm > 59:
        print('Incorrect minutes value')
        quit()
else:
    print('Please correct choose working mode.')
    quit()

if 12 < time_hh < 24:
    time_hh -= 12

dict_mm = {1:('одна минута', 'одной минуты'), 2:('две минуты', 'двух минут'), 3:('три минуты', 'трех минут'),
4:('четыре минуты', 'четырех минут'), 5:('пять минут', 'пяти минут'), 6:('шесть минут', 'шести минут'),
7:('семь минут', 'семи минут'), 8:('восемь минут', 'восьми минут'), 9:('девять минут', 'девяти минут'),
10:('десять минут', 'десяти минут'), 11:('одиннадцать минут', 'одиннадцати минут'),
12:('двенадцать минут', 'двенадцати минут'), 13:('тринадцать минут', 'тринадцати минут'),
14:('четырнадцать минут', 'четырнадцати минут'), 15:('пятнадцать минут', 'пятнадцати минут'),
16:('шестнадцать минут', 'шестнадцати минут'), 17:('семнадцать минут', 'семнадцати минут'),
18:('восемнадцать минут', 'восемнадцати минут'), 19:('девятнадцать минут', 'девятнадцати минут'),
20:('двадцать минут', 'двадцать'), 30:('тридцать минут', 'тридцать'), 40:('сорок минут', 'сорок')}

dict_hh = {1:('час', 'первого'), 2:('два часа', 'второго'), 3:('три часа', 'третьего'), 4:('четыре часа', 'четвертого'),
5:('пять часов', 'пятого'), 6:('шесть часов', 'шестого'), 7:('семь часов', 'седьмого'), 8:('восемь часов', 'восьмого'),
9:('девять часов', 'девятого'), 10:('десять часов', 'десятого'), 11:('одиннадцать часов', 'одиннадцатого'),
12:('двенадцать часов', 'двенадцатого'), 13:('час', 'первого')}

if time_mm == 0:
    if time_hh == 0 or time_hh == 24:
        print('полночь')
    elif time_hh == 12:
        print('полдень')
    else:
        print(dict_hh[time_hh][0], 'ровно')

elif time_mm <= 20:
    if time_hh == 12:
        print(dict_mm[time_mm][0], dict_hh[time_hh - 11][1])
        quit()
    print(dict_mm[time_mm][0], dict_hh[time_hh + 1][1])

elif 20 < time_mm < 45 and time_mm != 30:
    print(dict_mm[time_mm // 10 * 10][1], dict_mm[time_mm % 10][0], dict_hh[time_hh + 1][1])

elif time_mm == 30:
    print('половина', dict_hh[time_hh + 1][1])

elif time_mm >= 45:
    print('без', dict_mm[60 - time_mm][1], dict_hh[time_hh + 1][0])
