"""TIME."""

import datetime
pc_time = datetime.datetime.today()
select = input('\"Для получения текущего времени нажмите цифру - 1\"\n\
\"Для ввода времени нажмите цифру - 2\"\n\"Введите цифру\" : ')
print(f'"Вы ввели цифру : {select}"')
dict_val = {
    '00': ['ноль минут', 'двенадцать часов', 'час', 'первого'],
    '01': ['одна минута', 'один час', 'два', 'второго'],
    '02': ['две минуты', 'два часа', 'три', 'третьего'],
    '03': ['три минуты', 'три часа', 'четыре', 'четвертого'],
    '04': ['четыре минуты', 'четыре часа', 'пять', 'пятого'],
    '05': ['пять минут', 'пять часов', 'шесть', 'шестого'],
    '06': ['шесть минут', 'шесть часов', 'семь', 'седьмого'],
    '07': ['семь минут', 'семь часов', 'восемь', 'восьмого'],
    '08': ['восемь минут', 'восемь часов', 'девять', 'девятого'],
    '09': ['девять минут', 'девять часов', 'десять', 'десятого'],
    '10': ['десять минут', 'десять часов', 'одиннадцать', 'одиннадцатого'],
    '11':
    ['одинндцать минут', 'одиннадцать часов', 'двенадцать', 'двенадцатого'],
    '12': ['двенадцать минут', 'двенадцать часов', 'час', 'первого'],
    '13': ['тринадцать минут', 'один час', 'два', 'второго'],
    '14': ['четырнадцать минут', 'два часа', 'три', 'третьего'],
    '15': ['пятнадцать минут', 'три часа', 'четыре', 'четвертого'],
    '16': ['шестнадцать минут', 'четыре часа', 'пять', 'пятого'],
    '17': ['семнадцать минут', 'пять часов', 'шесть', 'шестого'],
    '18': ['восемнадцать минут', 'шесть часов', 'семь', 'седьмого'],
    '19': ['девятнадцать минут', 'семь часов', 'восемь', 'восьмого'],
    '20': ['двадцать минут', 'восемь часов', 'девять', 'девятого'],
    '21': ['двадцать одна минута', 'девять часов', 'десять', 'десятого'],
    '22':
    ['двадцать две минуты', 'десять часов', 'одиннадцать', 'одиннадцатого'],
    '23':
    ['двадцать три минуты', 'одиннадцать часов', 'двенадцать', 'двенадцатого'],
    '24': ['двадцать четыре минуты'],
    '25': ['двадцать пять минут'],
    '26': ['двадцать шесть минут'],
    '27': ['двадцать семь минут'],
    '28': ['двадцать восемь минут'],
    '29': ['двадцать девять минут'],
    '30': ['половина'],
    '31': ['тридцать одна минута'],
    '32': ['тридцать две минуты'],
    '33': ['тридцать три минуты'],
    '34': ['тридцать четыре минуты'],
    '35': ['тридцать пять минут'],
    '36': ['тридцать шесть минут'],
    '37': ['тридцать семь минут'],
    '38': ['тридцать восемь минут'],
    '39': ['тридцать девять минут'],
    '40': ['сорок минут'],
    '41': ['сорок одна минута'],
    '42': ['сорок две минуты'],
    '43': ['сорок три минуты'],
    '44': ['сорок четыре минуты'],
    '45': ['без пятнадцати минут'],
    '46': ['без четырнадцати минут'],
    '47': ['без тринадцати минут'],
    '48': ['без двенадцати минут'],
    '49': ['без одиннадцати минут'],
    '50': ['без десяти минут'],
    '51': ['без девяти минут'],
    '52': ['без восьми минут'],
    '53': ['без семи минут'],
    '54': ['без шести минут'],
    '55': ['без пяти минут'],
    '56': ['без четырех минут'],
    '57': ['без трех минут'],
    '58': ['без двух минут'],
    '59': ['без одной минуты']
}
if select == '1':
    ptime = pc_time.strftime('%H:%M').split(':')
    print(f'\"Текущее время\" - {ptime[0]}:{ptime[1]}')
    time_ch = ptime[0]
    time_mm = ptime[1]
    time_chsh = dict_val.get(time_ch)
    time_mmsh = dict_val.get(time_mm)
    if time_mm == '00':
        print(f'"{time_chsh[1]} - ровно"')
    elif time_mm < '30':
        print(f'"{time_mmsh[0]} {time_chsh[3]}"')
    elif time_mm == '30':
        print(f'"{time_mmsh[0]} {time_chsh[3]}"')
    elif time_mm > '30' and time_mm < '45':
        print(f'"{time_mmsh[0]} {time_chsh[3]}"')
    else:
        print(f'"{time_mmsh[0]} {time_chsh[2]}"')
elif select == '2':
    print('\"Введите время в формате - ЧЧ:ММ\"')
    time_ch = input('Введите часы:')
    time_mm = input('Введите минуты:')
    if time_ch in dict_val and time_mm in dict_val:
        time_chsh = list(dict_val.get(time_ch))
        time_mmsh = list(dict_val.get(time_mm))
        print(f'"Введенное время" {time_ch}:{time_mm}')
        if time_mm == '00':
            print(f'"{time_chsh[1]} - ровно"')
        elif time_mm < '30':
            print(f'"{time_mmsh[0]} {time_chsh[3]}"')
        elif time_mm == '30':
            print(f'"{time_mmsh[0]} {time_chsh[3]}"')
        elif time_mm > '30' and time_mm < '45':
            print(f'"{time_mmsh[0]} {time_chsh[3]}"')
        else:
            print(f'"{time_mmsh[0]} {time_chsh[2]}"')
    else:
        print('\"Введите корректные данные (ЧЧ:ММ)!!!\"')
else:
    print('\"Выберете из предлагаемых цифр и повторите ввод !!!\"')
