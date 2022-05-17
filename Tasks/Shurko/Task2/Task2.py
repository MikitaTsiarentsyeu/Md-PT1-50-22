from datetime import datetime

minut_word = {0: 'ноль', 1 : 'одна', 2 : 'две', 3 : 'три', 4 : 'четыре', 5 : 'пять',    6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять',
                10 : 'десять', 20 : 'двадцать', 30 : 'тридцать', 40 : 'сорок',   50 : 'пятьдесят',
                11 : 'одиннадцать', 12 : 'двенадцать', 13 : 'тринадцать',    14 : 'четырнадцать', 15 : 'пятнадцать', 16 : 'шестнадцать',    17 : 'семнадцать', 18 : 'восемнадцать', 19 : 'девятнадцать'}

half_hour = {0: 'первого', 1: 'второго', 2: 'третьего', 3: 'четвертого', 4: 'пятого', 5: 'шестого', 6: 'седьмого', 7: 'восьмого', 8: 'девятого', 9: 'десятого',  10: 'одинадцатого', 11: 'двенадцатого'}



def minutes_in_words (my_time):
    
    my_time = int(my_time)

    def minut_ends(var):
        s = minut_word.get(var)
        s = s[len(s)-1]
        if s == "е" or s == "и":
            return(" минуты")
        elif s== "а":
            return(" минута")
        else:
            return(" минут")
    
    if my_time>=0 and my_time<=59:
        if my_time <20:
            return (minut_word[my_time] + minut_ends(my_time))
        elif my_time%10 == 0:
            return (minut_word[my_time] + minut_ends(my_time))
        elif my_time < 60:
            x = my_time//10*10
            y = my_time%10
            return (minut_word[x]+minut_word[y] + minut_ends(y))
    else: print ('Out of range!!!!')

def hour_in_words (h_time):
    h2w = minut_word
    
    dif_dict = {1: 'один', 2: 'два'}  # need another solution
    
    h2w.update(dif_dict)
    h_time = int(h_time)
        

    def hour_ends(var):
            s = h2w.get(var)
            s = s[len(s)-1]
            if s == "ь": 
                return(" часов")
            elif s == "н":
                return(" час")
            else:
                return(" часа")

    if h_time >=0 and h_time < 13:
        return (minut_word[h_time] + hour_ends(h_time))
    elif h_time < 24:
        h_time = h_time%12
        return (minut_word[h_time] + hour_ends(h_time))

user_choice = int(input ('1 = current time, 2 = input your time '))
if user_choice == 1:
    current_t = datetime.now()
    print (current_t.time().strftime('%H:%M'))
elif user_choice == 2:
    user_time = str(input("Inter time in format hh:mm  "))
    if len(user_time) != 5:
        print ("wrong format time")
    elif user_time[2] != ':': 
        print ('wrong format time')
    elif int(user_time[0:2]) > 24:
        print ('param to much')
    elif int(user_time[0:2]) < 0:
        print ('param to low')
    elif int(user_time[3:6]) < 0:
        print ('param to low')
    elif int(user_time[3:6]) > 59:
        print ('param to much')
    else: 
        user_time = user_time.split(':')
        m = int(user_time[1])
        h = int(user_time[0])
        #print (f"{hour_in_words(h)} {minutes_in_words(m)}")
        hh = h%12
        if m == 0:
            if m == h:
                print('полночь')
            elif h ==12 and m == 0:
                print('полдень')
            else:
                print (f"{hour_in_words(h)} ровно")
           
        elif m == 30:
            print (f"половина {half_hour[hh]}")
        elif m > 0 and m < 45:
            print (f"{minutes_in_words(m)} {half_hour[hh]}")
        elif m >= 45:
            m = 60 - m
            st = minutes_in_words(m)
            if m >= 5 and m<=15:
                st = st.replace('ь', 'и')
            elif m == 1:
                st = st.replace('один', 'одной')
            elif m == 2:
                st = st.replace('два', 'двух')
            elif m == 3:
                st = st.replace('три', 'трех')
            elif m == 4:
                st = st.replace('четыре', 'четырех')


            print (f'без {st} {half_hour[hh]}')
         
            

else:
    print ('Incorect choice')



        



#minutes_in_words(input ('input number 0-59 ',))

