from datetime import datetime
hh1 =["первого", "второго", "третьего", "четвертого", "пятого", "шестого", "седьмого", "восьмого", "девятого", "десятого", "одинадцатого", "двенадцатого", "первого", "второго", "третьего", "четвертого", "пятого", "шестого", "седьмого", "восьмого", "девятого", "десятого", "одинадцатого", "двенадцатого"]
hh2 =["полночь", "час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать", "полдень", "час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать", "полночь"]
mm1 = ["", "одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать", "двадцать одна", "двадцать две", "двадцать три", "двадцать четыре", "двадцать пять", "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять", "половина", "тридцать одна", "тридцать две", "тридцать три", "тридцать четыре", "тридцать пять",  "тридцать шесть", "тридцать семь", "тридцать восемь",  "тридцать девять", "сорок", "сорок одна", "сорок две", "сорок три", "сорок четыре", "пятнадцати", "четырнадцати", "тринадцати", "двенадцати", "одинадцати", "десяти", "девяти", "восьми", "семи", "шести", "пяти", "четырех", "трех", "двух", "одной"]

time_mode = input("Пожалуйста, выберите формат вывода времени (введите 1 или 2):\n 1.Текущее время\n 2.Ввод времени с клавиатуры\n")
if int(time_mode) == 1:
    current_time = datetime.now().time()
    current_time = current_time.strftime("%H-%M")
    x_hh, x_mm = map(int, current_time.split("-", 1))
elif int(time_mode) == 2:
    time_input = (input("Пожалуйста, введите время в формате hh:mm\n"))
    x_hh, x_mm = map(int, time_input.split(":", 1))
else:
    print("Некорректный ввод")
    quit()

if x_hh < 0 or x_hh > 24:
     print("Некорректный ввод")
elif x_mm == 00:
    if x_hh == 0 or x_hh == 12 or x_hh == 24:
        print(hh2[x_hh])
    else:
        print(hh2[x_hh] + " ровно")
elif 2 <= x_mm <= 4 or 22 <= x_mm <= 24 or 32 <= x_mm <= 34 or 42 <= x_mm <= 44:
    print(mm1[x_mm] + " минуты " + hh1[x_hh])
elif 5 <= x_mm <= 20 or 25 <= x_mm < 30 or 35 <= x_mm <= 40:
    print(mm1[x_mm] + " минут " + hh1[x_hh])
elif x_mm == 30:
    print(mm1[x_mm] + " " + hh1[x_hh])
elif 45 <= x_mm < 59:
    print("без " + mm1[x_mm] + " минут " + hh2[x_hh+1])
elif x_mm == 59:
    print("без " + mm1[x_mm] + " минуты " + hh2[x_hh+1])
elif  x_mm == 1 or x_mm == 21 or x_mm == 31 or x_mm == 41:
    print(mm1[x_mm] + " минута " + hh1[x_hh])
else:
    print("Некорректный ввод")