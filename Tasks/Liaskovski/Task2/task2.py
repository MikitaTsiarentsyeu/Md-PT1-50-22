import datetime 
Current_time  = datetime.datetime.now().strftime('%H:%M') 

def answer(hours, min):
   text=["один", "два", "три", "четыре", "пять(ого)", "шесть(ого)",
    "семь", "восемь","девять(ого)","десять(ого)", "одинадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шеснадцать",
    "семнадцать", "восемнадцать", "девятнадцать", "двадцать(ого)", "двадцать один","двадцать два", "двадцать три", "двадцать четыре", "двадцать пять",
    "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять", "половина","полночь"]

   res=""
   if (min == 0):
      res = text[hours - 1] + " час(а)"
   elif (min == 30):
      res = text[min - 1]+ "  " + text[hours - 0]
   elif (min == 1):
      res = text[min - 1] + " минута " + text[hours - 0]
   elif (min == 15):
      res = text[min - 1]+ "  минут  " + text[hours - 0]
   elif (min < 30):
      res = text[min - 1] + " минут(ы) " + text[hours - 0]
   elif (min==45):
      res = "без пятнадцати " + text[hours]
   elif (min == 00) :
      res = "полночь " + text[hours + 31]
   else:
      res = text[(60 - min)-1] + " минут до " + text[hours]
   return res

Choice = input("Current or input time, press 1 or 2 : ")

if Choice =="1":
   hours = int(datetime.datetime.now().strftime('%H'))
   min= int(datetime.datetime.now().strftime('%M'))
   print(answer(hours, min))
elif Choice =="2":
    hours = int(input("Enter hours hh: "))
    min=int(input("Enter minutes mm: "))
    print(answer(hours, min))
else:
    print("error")

