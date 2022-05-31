import datetime
dict = {0:["полночь","первого","ноль минут"],
    1:["один час","второго","одна минута"],
    2:["два часа","третьего","две минуты"],
    3:["три часа","четвертого","три минуты"],
    4:["четыре часа","пятого","четыре минуты"],
    5:["пять часов","шестого","пять минут"],
    6:["шесть часов","седьмого","шесть минут"],
    7:["семь часов","восьмого","семь минут"],
    8:["восемь часов","девятого","восемь минут"],
    9:["девять часов","десятого","девять минут"],
    10:["десять часов","одинадцатого","десять минут"],
    11:["одиннадцать часов","двенадцатого","одиннадцать минут"],
    12:["полдень","первого","двенадцать минут"],
    13:["один час","второго","тринадцать минут"],
    14:["два часа","третьего","четырнадцать минут"],
    15:["три часа","четвертого","пятдадцать минут"],
    16:["четыре часа","пятого","шестнадцать минут"],
    17:["пять часов","шестого","семнадцать минут"],
    18:["шесть часов","седьмого","восемнадцать минут"],
    19:["семь часов","восьмого","девятнадцать минут"],
    20:["восемь часов","девятого","двадцать минут"],
    21:["девять часов","десятого","двадцать одна минута"],
    22:["десять часов","одинадцатого","двадцать две минуты"],
    23:["одиннадцать часов","двенадцатого","двадцать три минуты"],
    24:["двадцать четыре минуты"],
    25:["двадцать пять минут"],
    26:["двадцать шесть минут"],
    27:["двадцать семь минут"],
    28:["двадцать восемь минут"],
    29:["двадцать девять минут"],
    30:["половина"],
    31:["тридцать одна минута"],
    32:["тридцать две минуты"],
    33:["тридцать три минуты"],
    34:["тридцать четыре минуты"],
    35:["тридцать пять минут"],
    36:["тридцать шесть минут"],
    37:["тридцать семь минут"],
    38:["тридцать восемь минут"],
    39:["тридцать девять минут"],
    40:["сорок минут"],
    41:["сорок одна минута"],
    42:["сорок две минуты"],
    43:["сорок три минуты"],
    44:["сорок четыре минуты"],
    45:["без пятнадцати минут"],
    46:["без четырнадцати минут"],
    47:["без тринадцати минут"],
    48:["без двенадцати минут"],
    49:["без одинадцати минут"],
    50:["без десяти минут"],
    51:["без девяти минут"],
    52:["без восьми минут"],
    53:["без семи минут"],
    54:["без шести минут"],
    55:["без пяти минут"],
    56:["без четырех минут"],
    57:["без трех минут"],
    58:["без двух минут"],
    59:["без одной минуты"],}
current_time = datetime.datetime.today().strftime("%H:%M")
user_choice = int(input("Please choice:\n 1 - current time \n 2 - your time\n"))
if user_choice in range(1, 3):
    if user_choice == 1:
        values_1 = current_time.split(':')
        hours_1, minutes_1 = values_1[0], values_1[1]
        hours_1 = int(hours_1)
        minutes_1 = int(minutes_1)
        if minutes_1 == 0:
            print(f"{dict[hours_1][0]} ровно")
        elif minutes_1 < 24:
            print(f"{dict[minutes_1][2]} {dict[hours_1][1]}")
        elif minutes_1 < 30 and minutes_1 > 23:
            print(f"{dict[minutes_1][0]} {dict[hours_1][1]}")
        elif minutes_1 == 30:
            print(f"половина {dict[hours_1][1]}")   
        elif minutes_1 > 30 and minutes_1 <45:
            print(f"{dict[minutes_1][0]} {dict[hours_1][1]}")   
        elif minutes_1 >= 45:
            print(f"{dict[minutes_1][0]} {dict[hours_1][1]}")
    elif user_choice == 2:
        while True:
            user_input = input("Please enter your time (hh:mm): ")
            if len(user_input) != 5:
                print("Incorrect input, it has wrong length")
                continue
            if user_input[2] != ':':
                print("Incorrect input, it has no : symbol")
                continue
            values_2 = user_input.split(':')
            hours_2, minutes_2 = values_2[0], values_2[1]
            if not (hours_2.isdigit() and minutes_2.isdigit()):
                print("Incorrect input, the hours and minutes must be digit format")
                continue
            hours_2 = int(hours_2)
            minutes_2 = int(minutes_2)
            if hours_2 > 23:
                print("Incorrect input, the hours value must be less than 24")
                continue
            if minutes_2 > 59:
                print("Incorrect input, the minutes must be less than 60")
                continue
            break
        if minutes_2 == 0:
            print(f"{dict[hours_2][0]} ровно")
        elif minutes_2 < 24:
            print(f"{dict[minutes_2][2]} {dict[hours_2][1]}")
        elif minutes_2 < 30 and minutes_2 > 23:
            print(f"{dict[minutes_2][0]} {dict[hours_2][1]}")
        elif minutes_2 == 30:
            print(f"половина {dict[hours_2][1]}")   
        elif minutes_2 > 30 and minutes_2 <45:
            print(f"{dict[minutes_2][0]} {dict[hours_2][1]}")   
        elif minutes_2 >= 45:
            print(f"{dict[minutes_2][0]} {dict[hours_2][1]}")
else:
    print ("Incorrect choise")
