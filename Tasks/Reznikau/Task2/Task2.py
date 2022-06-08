
from datetime import datetime

def is_str_digit(n: str) -> bool:
     try:
         int(n)
         return True
     except ValueError:
         return False


print("""Hi there!
I can show you the current time in russian words or time you desire to see.
Please, just press the button "ENTER" if you would like to see the current time.

If you would like to see your own time, please, type the time you desire to see in russian words.
But I have one kind request for you, please, use the format: hh:mm.""")

Time_got = input("Let's go: ").replace(' ','')

# This conditions are used to provide to User an opportunity to do some mistakes which are not important in terms of value validation,
# in particular extra symbols before / after data in the right format.
# I believe it increases the level of usability and Users satisfaction:)

if not Time_got == '':

    if Time_got.find(":") >= 2 and len(Time_got) - Time_got.find(":") >= 3:
        Hour = Time_got[Time_got.find(":")-2:Time_got.find(":")]
        Min = Time_got[Time_got.find(":")+1:Time_got.find(":")+3]

        if is_str_digit(Hour) and is_str_digit(Min):
            Hour = int(Hour)
            Min = int(Min)

        else:
            print("""Data was entered wrong: the pairs of symbols before and right after ':' are not figures.
    Please, reboot the script and enter data in the following format: hh:mm, where 'hh' and 'mm' are pairs of figures.""")
            input()
            exit()
        
    else:
        print("The time value entered is wrong, please, reboot the script and enter data in the following format: hh:mm")
        input()
        exit()

    if Hour < 0 or Hour > 24:
        print("Data was entered wrong: the hours are unreal.\nPlease, reboot the script and enter the value of hour in the range from 0 by 24.")
        input()
        exit()

    elif Hour == 24:
        Hour = 0

    elif Min < 0 or Min > 59:
        print("Data was entered wrong: the minutes are unreal.\nPlease, reboot the script and enter the value of minutes in the range from 0 by 59.")
        input()
        exit()

else:
    Hour = int(datetime.now().strftime('%H'))
    Min = int(datetime.now().strftime('%M'))
    

# There are two groups of values to describe hours: "Coming hour" ('пятый', 'шестой', etc.) and "Hour Come" ('пять', 'шесть', etc.)

# Necessary collections (massives) and varaibles
h_coming_dict = {0:'первого', 1:'второго', 2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 6:'седьмого', 7:'восьмого', 8:'девятого', 9:'десятого', 10:'одиннадцатого', 11:'двенадцатого'}
h_time_of_day_list = ['ночи', 'утра', 'дня', 'вечера']
h_word = ['час', 'часа', 'часов']

m_units_dict = {0:'', 1:'одна', 2:'две', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать', 12:'двенадцать', 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семнадцать', 18:'восемнадцать', 19:'девятнадцать'}
m_dozens_dict = {2:'двадцать', 3:'тридцать', 4:'сорок', 5:'пятьдесят'}

h_come_dict = m_units_dict.copy()
h_come_dict[0], h_come_dict[1], h_come_dict[2] = 'двенадцать', '', 'два'

Hour = Hour + 1 if Min >= 45 else Hour
index_hour = Hour - 12 if Hour >= 12 else Hour

# COMING HOUR:
if Hour == 23:
    h_result_coming = ' '.join([h_coming_dict[index_hour], h_time_of_day_list[0]])

elif Hour >= 17:
    h_result_coming = ' '.join([h_coming_dict[index_hour], h_time_of_day_list[3]])

# the word "часа" is added, because the numeral in conjunction with the word "дня" can create confusion on number of day, but not the hour.
# f.e. "половина первого дня", "половина второго дня", etc.

elif Hour >= 11:
    h_result_coming = ' '.join([h_coming_dict[index_hour], h_word[1], h_time_of_day_list[2]])

elif Hour >= 3:
    h_result_coming = ' '.join([h_coming_dict[index_hour], h_time_of_day_list[1]])

else:
    h_result_coming = ' '.join([h_coming_dict[index_hour], h_time_of_day_list[0]])

#HOUR COME:

if Hour >= 18:
    h_result_come = ' '.join([h_come_dict[index_hour], h_word[2], h_time_of_day_list[3]])

elif Hour == 17 or Hour == 12:
    h_result_come = ' '.join([h_come_dict[index_hour], h_word[2], h_time_of_day_list[2]])

elif Hour >= 14:
    h_result_come = ' '.join([h_come_dict[index_hour], h_word[1], h_time_of_day_list[2]])

elif Hour == 13:
    h_result_come = ' '.join([h_word[0], h_time_of_day_list[2]])

elif Hour >= 5:
    h_result_come = ' '.join([h_come_dict[index_hour], h_word[2], h_time_of_day_list[1]])

elif Hour == 4:
    h_result_come = ' '.join([h_come_dict[index_hour], h_word[1], h_time_of_day_list[1]])

elif Hour >= 2:
    h_result_come = ' '.join([h_come_dict[index_hour], h_word[1], h_time_of_day_list[0]])

elif Hour == 1:
    h_result_come = ' '.join([h_word[0], h_time_of_day_list[0]])

else:
    h_result_come = ' '.join([h_come_dict[index_hour], h_word[2], h_time_of_day_list[0]])


# Minutes

Result = 'NONE'
m_word = 'минут'
Min_doz = int(Min / 10)
Min_unit = Min - (Min_doz*10)

if Min_unit == 1 and Min_doz != 1:
    m_word = m_word + 'а'

elif Min_unit >= 2 and Min_unit <= 4 and Min_doz != 1:
    m_word = m_word + 'ы'


if Min == 0:
    Result = h_result_come + ' ровно'

elif Min == 30:
    Result = 'половина ' + h_result_coming

elif Min >=1 and Min <=19:
    Result = ' '.join([m_units_dict[Min], m_word, h_result_coming])

elif Min >= 20 and Min <= 44:
    Result = ' '.join([m_dozens_dict[Min_doz], m_units_dict[Min_unit], m_word, h_result_coming])

elif Min >= 45 and Min <= 59:
    m_neg = 60 - Min

    if m_neg >= 5:
        m_neg_str = m_units_dict[m_neg].replace('ь', 'и')

    elif m_neg == 4:
        m_neg_str = m_units_dict[m_neg].replace('ре', 'рёх')

    elif m_neg == 3:
        m_neg_str = m_units_dict[m_neg].replace('и', 'ёх')

    elif m_neg == 2:
        m_neg_str = m_units_dict[m_neg].replace('е', 'ух')

    elif m_neg == 1:
        m_neg_str = m_units_dict[m_neg].replace('на', 'ной')
        m_word = m_word + 'ы'


    Result = ' '.join(['без', m_neg_str, m_word, h_result_come])


if '  ' in Result:
    Result = Result.replace('  ',' ')

print(Result)
#Cur_time = datetime.now().strftime('%H:%M')
#print(Cur_time)

