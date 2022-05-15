from datetime import datetime

unites = {
    0: ("", "", "полночь", 'до полуночи'),
    1: ('одна',"одной", "час", "первого", "полудня"),
    2: ('две', "двух", "два", "второго"),
    3: ('три',"трех", "три", "третьего"),
    4: ('четыре', "четырех", "четыре", "четвертого"),
    5: ('пять',),
    6: ('шесть',),
    7: ('семь',"","", "седьмого"),
    8: ('восемь',"","", "восьмого"),
    9: ('девять',),
    10: ('десять',),
    11: ('одиннадцать',),
    12: ('двенадцать',"", "полдень", " до полудня"),
    13: ('тринадцать',),
    14: ('четырнадцать',),
    15: ('пятнадцать',),
    16: ('шестнадцать',),
    17: ('семнадцать',),
    18: ('восемнадцать',),
    19: ('девятнадцать',),
}

twenties = {
    2: ('двадцать',),
    3: ('тридцать',),
    4: ('сорок',),
    5: ('пятьдесят',),
    6: ('шестьдесят',),

}


table_of_converted_hours = {i:j for i,j in zip(range(13,24), range(1,12))}

table_of_converted_hours.update({24:0})

special_hours_if_minutes_0 = (0, 1, 12)


def chose_mode():
    print("Пожалуйста выберите вариант работы программы:")
    mode =  input('1: Вывести на экран время на данный момент\n2: Ввести свое время\nваш выбор:   ')
    if mode in ('1','2'): return mode
    else:
        print("Извините, но что-то введено неверно. Попробуйте еще раз\n")


def start_program(mode):
    if mode == '1': return time_at_the_moment()
    return custom_time()


def check_special_hours(hours, minutes):
    if minutes > 0: hours = hours + 1
    if hours in range(13, 25): hours = table_of_converted_hours[hours]
    return hours


def check_time(arr):
    time_list = [int(i[1]) if not i[0] else int(i) for i in arr]
    return  check_special_hours(*time_list), time_list[1]


def time_at_the_moment():
    time = datetime.now().strftime('%H:%M')
    return *check_time(time.split(':')), time


def custom_time():
    try:
        time = input("Пожалуйста, укажите время в формате чч:мм: ")
        datetime.strptime(time, "%H:%M")                #checking the correctness of the entered time
        return *check_time(time.split(':')), time
    except:
        print("Извините, но данные введены не верно")
        custom_time()


def if_minutes_0(hours, _, time):
    if hours in special_hours_if_minutes_0: return f"{time} - {unites[hours][2]} ровно"
    return f"{time} - {unites[hours][0]} ровно"


def if_minutes_30(hours, _, time):
    if hours in (0, 1, 2, 3, 4, 7,8, 12): return f"{time} - полчаса {unites[hours][3]}"
    return f"{time} - полчаса {unites[hours][0][0:-2]}того"


def if_minutes_smaller_45(hours, minutes, time):
    if minutes > 19:
        ten_mins, one_mins = [int(i) for i in str(minutes)]
        if ten_mins > 1:
            minutes_str = twenties[ten_mins][0] + " " + unites[one_mins][0]
    else:
        minutes_str = unites[minutes][0]
    if (minutes%10) == 1 and minutes != 11:
        minutes_str = f"{minutes_str} минута"
    elif ((minutes % 10) in (2, 3, 4) and ((minutes - (minutes % 10)) > 10)) or (minutes in (2,3,4)):
        minutes_str = f"{minutes_str} минуты"
    else:
        minutes_str = f"{minutes_str} минут"
    if hours in (0, 1, 2, 3, 4, 7, 8, 12): return (f"{time} - {minutes_str}  {unites[hours][3]}")
    return (f"{time} - {minutes_str} {unites[hours][0][0:-2]}того")



def if_minutes_bigger_45(hours, minutes, time):
    diff = 60 - minutes
    if diff == 1:
        diff_str = f" без одной минуты"
    elif diff in (2, 3, 4):
        diff_str = f"без {unites[diff][1]} минут"
    else:
        diff_str = f"без {unites[diff][0][0:-1]}и минут"
    if hours in (0, 1, 2, 12): return (f"{time} - {diff_str} {unites[hours][2]}")
    return f"{time} - {diff_str} {unites[hours][0]}"


def main_loop(hours, minutes, time):
    if minutes == 0:
        return if_minutes_0(hours, minutes, time)
    elif minutes == 30:
        return if_minutes_30(hours, minutes, time)
    elif minutes < 45:
        return if_minutes_smaller_45(hours, minutes, time)
    else:
        return if_minutes_bigger_45(hours, minutes, time)


def main():
        mode = chose_mode()
        hours, minutes, time = start_program(mode)
        print(main_loop(hours, minutes, time))
        another_time = input("Желаете воспользоваться программой еще раз (да, нет)?\n:  ")
        if another_time in ('да', "д", "y", 'yes', 'ya'): main()


# write all output in file for checking mistakes in time
def check_output():
    with open('output.txt', 'a') as f:
        for i in range(0,24):
            for j in range(0, 60):

                hours, minutes = check_time([str(i),str(j)])
                time = str(i) + ":" + str(minutes)

                f.writelines(main_loop(hours,minutes,time) + '\n')


# check_output()


if __name__ == '__main__':
    main()








