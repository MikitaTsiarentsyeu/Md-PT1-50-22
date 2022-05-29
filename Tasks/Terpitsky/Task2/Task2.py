import datetime

current_date_time = datetime.datetime.now()
curent_time = current_date_time.strftime('%H:%M')
hours_dict = {(1,13):("час","первого"), (2, 14):('два',"второго"), (3,15):('три',"третьего"), (4,16):("четыре","четвертого"), (5,17):("пять","пятого"), 
(6,18):("шесть","шестого"), (7,19):("семь", "седьмого"), (8,20):("восемь", "восьмого"), (9,21):("девять", "девятого"), (10,22):("десять", "десятого"), 
(11,23):("одинадцать", "одинадцатого"), (12,0):("двенадцать", "двенадцатого"), (24,24):("двенадцать", "двенадцатого")}
min_dict = {0:"ровно", 1:("одна","одной"), 2:("две","двух"),3:("три","трех"),4:("четыре","четырех"),5:("пять","пяти"),6:("шесть","шести"),7:("семь","семи"),
8:("восемь","восьми"),9:("девять","девяти"),10:("десять","десяти"),11:("одинадцать","одинадцати"),12:("двенадцать","двенадцати"),13:("тринадцать","тринадцати"),
14:("четырнадцать","четырнадцати"),15:("пятнадцать","пятнадцати"),16:"шеснадцать",17:"семнадцать",18:"восемнадцать",19:"девятнадцать"}
min_dict_twent = {2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",30:"половина"}
min_words_dict = {1:"минута", 2:"минуты", 3:"минут"}
hours_words_dict = {1: "час", 2: "часа", 5: "часов"}
day_night_dict = {1:"утро",2:"день",3:"вечер",4:"ночь"}
while True:
    print("Приветствую тебя человек, это программа покажет тебе истинное время, либо какое введешь")
    while True:
        choise = input("Чтобы узнать истинное время, введи 1; чтобы указать свое время, введи 2\n")
        if not choise.isdigit():
            print('Это даже не цифра, нужно ввести 1 или 2')
            continue
        choise = int(choise)
        if choise > 2 or choise < 1:
            print("Нужно ввести цифру 1 или цифру 2, это не невозможно, пожалуйста, сосредоточься")
            continue
        break
    while True:
        if choise == 2:
            while True:
                time_input = input("Будьте любезны ввести время в формате hh:mm:\n")
                if len(time_input) != 5:
                    print("Ошибка ввода, неверное количество символов")
                    continue
                if time_input[2] != ':':
                    print("Ошибка ввода, часы и минуты необходимо разделить символом ';'")
                    continue
                break
        if choise == 1:
            time_input = curent_time
            print(time_input)
        time_input_list = time_input.split(":")
        min_time = time_input_list[0]
        hours_time = time_input_list[1]
        while True:
            if not (hours_time.isdigit() and min_time.isdigit()):
                print('Ошибка ввода, время необходимо ввести цифрами')
                continue
            break
        hours_time = int(time_input_list[0])
        min_time = int(time_input_list[1])
        min_time_list = list(time_input[3:5])
        min_time_twent = int(min_time_list[0])
        min_time_units = int(min_time_list[1])
        break
    #hours
    if min_time == 0: #7:00
        for i in hours_dict:
            if hours_time == i[0] or hours_time == i[1]:
                hours_final = hours_dict[i][0]
    if min_time < 45 and min_time > 0: #7:26
        for i in hours_dict:
            if hours_time == i[0]:
                hours_time = i[0] + 1
                break
            if hours_time == i[1]:
                hours_time = i[1] + 1
                break
        for i in hours_dict:
            if hours_time == i[0] or hours_time == i[1]:
                hours_final = hours_dict[i][1]
    if min_time > 44:
        for i in hours_dict:
            if hours_time == i[0]:
                hours_time = i[0] + 1
                break
            if hours_time == i[1]:
                hours_time = i[1] + 1
                break
        for i in hours_dict:
            if hours_time == i[0] or hours_time == i[1]:
                hours_final = hours_dict[i][0]
    #hours word
    for i in hours_words_dict:
        if min_time in range(1, 45):
            hours_word = hours_words_dict[2]
            break
        if hours_time == 1 or hours_time == 13:
            hours_word = hours_words_dict[1]
        elif hours_time in range(2, 5) or hours_time in range(14, 17):
            hours_word = hours_words_dict[2]
        elif hours_time in range(5, 13) or hours_time in range(17, 24) or hours_time == 0:
            hours_word = hours_words_dict[5]
    #minuts
    if min_time < 20:
        for i in min_dict:
            if min_time == i and min_time < 16:
                min_final = min_dict[i][0]
            elif min_time == i and min_time in range(16, 20):
                min_final = min_dict[i]
    if min_time > 19 and min_time < 45 and min_time != 30:
        for i in min_dict_twent:
            if min_time_twent == i:
                min_final = min_dict_twent[i]
        for i in min_dict:
            if min_time_units == 0:
                break
            if min_time_units == i:
                min_final = min_final + ' ' + min_dict[i][0]
    if min_time > 44:
            min_temp = 60 - min_time
            for i in min_dict:
                if min_temp == i:
                    min_final = 'без' + ' ' + min_dict[i][1]
            if min_temp != 1:
                min_word = min_words_dict[3]
            else: 
                min_word = min_words_dict[2]
    if min_time == 0:
        min_final = min_dict[0]
    if min_time == 30:
        min_final = min_dict_twent[30]
    #min word
    if min_time > 0 and min_time < 45:
        if min_time == 1 or min_time_units == 1:
            min_word = min_words_dict[1]
        elif min_time in range(2, 5) or min_time_units in range(2, 5) and min_time not in range(10, 20):
            min_word = min_words_dict[2]
        else:
            min_word = min_words_dict[3]       
    #san
    if hours_time in range(0, 6):
        day_night_word = day_night_dict[4]
    elif hours_time in range(6, 12):
        day_night_word = day_night_dict[1]
    elif hours_time in range(12, 18):
        day_night_word = day_night_dict[2]
    elif hours_time in range(18, 25):
        day_night_word = day_night_dict[3]

    #ready str
    if min_time in range(1, 30) or min_time in range(31, 60):
        print(f'Время сейчас: {min_final} {min_word} {hours_final}, {day_night_word}')
    elif min_time == 0:
        print(f'Время сейчас: {hours_final} {hours_word} {min_final}, {day_night_word}')
    elif min_time == 30:
        print(f'Время сейчас: {min_final} {hours_final}, {day_night_word}')
    flag = input(f'Еще раз провернем это? введи 1 - для повтора, любой символ для выхода из программы]:')
    if flag != "1":
        break







