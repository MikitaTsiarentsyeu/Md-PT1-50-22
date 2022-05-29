for time_hh in range(25):
    for time_mm in range(60):
        time_hh = int(time_hh)
        time_mm = int(time_mm)

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

    
    print(time_mm)
    print(time_hh)

print('check end!')