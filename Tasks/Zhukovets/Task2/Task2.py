import datetime
digit = {
    0: ['', '', ''],
    1: ['один', 'одной', 'одна', 'первого'],
    2: ['два', 'двух', 'две', 'второго'],
    3: ['три', 'трёх', 'три', 'третьего'],
    4: ['четыре', 'четырех', 'четыре', 'четвертого'],
    5: ['пять', 'пяти', 'пять', 'пятого'],
    6: ['шесть', 'шести', 'шесть', 'шестого'],
    7: ['семь', 'семи', 'семь', 'седьмого'],
    8: ['восемь', 'восьми', 'восемь', 'восьмого'],
    9: ['девять', 'девяти', 'девять', 'девятого'],
    10: ['десять', 'десяти', 'десять', 'десятого'],
    11: ['одиннадцать', 'одиннадцати', 'одиннадцать', 'одиннадцатого'],
    12: ['двенадцать', 'двенадцати', 'двенадцать', 'двенадцатого'],
    13: ['тринадцать', 'тринадцати', 'тринадцать'],
    14: ['четырнадцать', 'четырнадцати', 'четырнадцать'],
    15: ['пятнадцать', 'пятнадцати', 'пятнадцать'],
    16: ['шестнадцать', 'шестнадцать', 'шестнадцать'],
    17: ['семнадцать', 'шестнадцать', 'семнадцать'],
    18: ['восемнадцать', 'восемнадцати', 'восемнадцать'],
    19: ['девятнадцать', 'девятнадцати', 'девятнадцать'],
    20: ['двадцать', 'двадцати', 'двадцать'],
    }
tens = {
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    }



def choose_plural(amount: int, variant1, variant2, variant3):
    """Selects the declination depending on the amount"""
    if amount % 10 == 1 and amount % 100 != 11:
        return variant1
    elif amount % 10 >= 2 and amount % 10 <= 4 and \
            (amount % 100 < 10 or amount % 100 >= 20):
        return variant2
    else:
        return variant3


def time_convertor(time_string):
    time_obj = datetime.datetime.strptime(time_string, "%H:%M").time()
    hour = time_obj.hour if time_obj.hour < 12 else time_obj.hour - 12
    minutes = time_obj.minute
    if time_obj.hour == 0 and time_obj.minute == 0:
        return 'Сейчас полночь'
    elif time_obj.hour == 12 and time_obj.minute == 0:
        return 'Сейчас полдень'
    elif minutes == 0:
        value_choose_plural = choose_plural(hour, "час", "часа", "часов")
        value_from_dict_for_hours = digit[hour][0]
        return f'Сейчас {value_from_dict_for_hours} {value_choose_plural} ровно'

    elif minutes == 30:
        value_from_dict_for_hours = digit[hour+1][3]
        return f'Половина {value_from_dict_for_hours}'

    elif minutes < 30:
        value_choose_plural = choose_plural(minutes, "минута", "минуты", "минут")
        value_from_dict_for_hours = digit[hour + 1][3]
        if minutes <= 20:
            value_from_dict_for_minutes = digit[minutes][2]
        else:
            remainder = time_obj.minute - 20
            value_from_dict_for_minutes = f'{tens[20]} {digit[remainder][2]}'
        return f'{value_from_dict_for_minutes} {value_choose_plural} {value_from_dict_for_hours}'

    elif 30 < minutes < 45:
        value_choose_plural = choose_plural(minutes, 'минута', "минуты", "минут")
        value_from_dict_for_hours = digit[hour + 1][3]
        if minutes < 40:
            remainder = minutes - 30
            value_from_dict_for_minutes = f'{tens[30]} {digit[remainder][2]}'
        else:                       # minutes from 40 to 45
            remainder = minutes - 40
            value_from_dict_for_minutes = f'{tens[40]} {digit[remainder][2]}'
        return f'{value_from_dict_for_minutes} {value_choose_plural} {value_from_dict_for_hours}'

    else:                           # minutes <= 45
        value_choose_plural = choose_plural(hour + 1, "час", "часа", "часов")
        value_from_dict_for_hours = digit[hour+1][0]
        value_from_dict_for_minutes = digit[60 - minutes][1]
        str_minutes = "минут" if minutes != 1 else "минуты"
        return f'Без {value_from_dict_for_minutes} {str_minutes} {value_from_dict_for_hours} {value_choose_plural}'


def main():
    while True:
        user_choice = input("Какая опция вас интересует?\n"
                            "Если вы хотите узнать текущее время - нажмите '1'\n"
                            "Если вы хотите задать время - нажмите '2'\n"
                            ":")
        if user_choice == '1':
            time_string = datetime.datetime.now().strftime("%H:%M")
            return time_convertor(time_string)
        elif user_choice == '2':
            time_string = input("Пожалуйста введите интересующее вас время в формате 'ЧЧ:ММ'\n:")
            validation_value1, validation_value2 = time_string.split(":")[0], time_string.split(":")[-1]
            if (validation_value1.isdigit() and len(validation_value1) == 2) \
                    and (validation_value2.isdigit() and len(validation_value2) == 2):
                return time_convertor(time_string)

            else:
                print("Вы ввели интересующую вас дату не в формате 'ЧЧ:ММ', попробуйте ещё раз.")
                print("--------------------------------------------------------------------------")

        else:
            print("Ошибка. Введите выбранную вами опцию используя символы '1' или '2'")


print(main())