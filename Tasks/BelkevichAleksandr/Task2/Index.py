import datetime

def time_selection():
    '''
    function for checking selection input from user
    '''
    while True:
        try:
            a = int(input("Please enter 1 for now time or 2 for enter your time: "))

            # check if the entered number is correct
            if a == 1 or a == 2:
                return a

            # output for explanation
            print(f"Error, {a} isn't 1 or 2")
        except:
            print("Error, not an integer entered")
            continue

def input_time_user():
    '''
    function for checking input time from user
    '''
    while True:
        try:
            a = input("Please enter time in this format (HH:MM): ")
            s = corrected_time(a)

            # check if the entered time is correct
            if 0 <= s[0] * 10 + s[1] < 24 and 0 <= s[2] * 10 + s[3] < 60 and len(s) == 4:
                return s

            # output for explanation
            print("There is no such time in nature, enter the time correctly")
        except:
            print("Error, not a correct enter format time")
            continue

def corrected_time(hour_minute):
    '''
    function to split and return integer list from input
    '''
    mas = hour_minute.replace("(", "").replace(":", "").replace(")", "")
    return [int(numb) for numb in mas]

def out_time(mas):
    '''
    function for output time 
    '''

    # created hours
    hour = mas[0] * 10 + mas[1]

    # output if minutes == 00
    if mas[2] == 0 and mas[3] == 0:
        print(f"{numbers_for_out.get(hour)} {declension_word_hours(hour)} ровно")

    # output minutes == 30
    elif mas[2] == 3 and mas[3] == 0:
        print(f"половина {time_line(hour)}")

    # output minutes if time from 01 to 44 not including 30
    elif 0 <= mas[2] < 4 and 0 <= mas[3] < 10 or mas[2] == 4 and 0 < mas[3] < 5:
        # output minutes if time from 01 to 09
        if mas[2] == 0:
            print(f"{numbers_minutes_start.get(mas[3])} {declision_word_minutes(mas[3])} {time_line(hour)}")
        # output minutes if time 10, 20, 40
        elif mas[3] == 0:
            print(f"{numbers_for_out.get(mas[2] * 10)} {declision_word_minutes(mas[3])} {time_line(hour)}")
        # output remaining time
        else:
            print(f"{numbers_for_out.get(mas[2] * 10)} {numbers_minutes_start.get(mas[3])} {declision_word_minutes(mas[3])} {time_line(hour)}")

    # output minutes if time from 45 to 59
    else:
        print(f"Без {numbers_minutes_end.get(60 - mas[2] * 10 - mas[3])} {declision_word_minutes(mas[3])} {time_line(hour)}")

def declension_word_hours(hour):
    '''
    function for correction word "hour" 
    '''
    if hour == 1 or hour == 21:
        return "час"
    elif 2 <= hour <= 4 or hour > 21:
        return "часа"
    else:
        return "часов"

def declision_word_minutes(minutes):
    '''
    function for correction word "minute" 
    '''
    if minutes == 1:
        return "минута"
    elif 1 < minutes < 5:
        return "минуты"
    else:
        return "минут"

def time_line(hour):
    '''
    function for setting time of day 
    '''
    if hour < 12:
        return f"{numbers_hours_declision.get(hour + 1)} до обеда"
    else:
        return f"{numbers_hours_declision.get(hour - 11)} после обеда"

numbers_for_out = {0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 
                7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одинадцать", 
                12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
                16: "шестнадцать", 17: "семьнадцать", 18: "восемнадцать", 19: "девятнадцать",
                20: "двадцать", 21: "двадцать один", 22: "двадцать два", 23: "двадцать три",
                24: "двадцать четыре", 30: "тридцать", 40: "сорок", 50: "пятьдесят"}
 
numbers_hours_declision = {1: "первого", 2: "второго", 3: "третьего", 4: "четвертого", 5: "пятого", 6: "шестого", 
                7: "седьмого", 8: "восьмого", 9: "девятого", 10: "десятого", 11: "одинадцатого", 
                12: "двенадцатого"}

numbers_minutes_start = {1: "одна", 2: "две", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 
                7: "семь", 8: "восемь", 9: "девять"}

numbers_minutes_end = {1: "одной", 2: "двух", 3: "трех", 4: "четырех", 5: "пяти", 6: "шести", 
                7: "семи", 8: "восеми", 9: "девяти", 10: "десяти", 11: "одинадцати", 
                12: "двенадцати", 13: "тринадцати", 14: "четырнадцати", 15: "пятнадцати"}

selection = time_selection()

if selection == 1:
    time_now = corrected_time(datetime.datetime.now().strftime("%H:%M"))
    out_time(time_now)
else:
    time_list = input_time_user()
    out_time(time_list)