import datetime

choice=int(input('Please choose 1 - computer time, 2 - user time: '))

if choice==1:
   dt_n = datetime.datetime.now()
   t_n = dt_n.time()
   t_n = t_n.strftime('%H:%M')
else:
    t_n = input("Please enter your time in HH:MM format: ")

l = t_n.split(':')

M = int(l[1])
H = int(l[0])

if H>24 or M>59:
    print("Время введено в некорректном формате") 

if H>12:
    H=H-12

M_skl_a = [1,21,31,41]
M_skl_i = [2,3,4,22,23,24,32,33,34,42,43,44,59]

if M in M_skl_a:
    Skl = "минута"
elif M in M_skl_i:
    Skl = "минуты"
else:
    Skl = "минут"

Mi = {0:"ровно", 1:"одна",2:"две", 3:"три", 4:"четыре", 5:"пять",
6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять",
11:"одиннадцать", 12:"двенадцать", 13:"тринадцать", 14:"четырнадцать", 15:"пятнадцать",
16:"шестнадцать", 17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать", 20:"двадцать",    
21:"двадцать одна", 22:"двадцать две", 23:"двадцать три", 24:"двадцать четыре", 25:"двадцать пять",
26:"двадцать шесть", 27:"двадцать семь", 28:"двадцать восемь", 29:"двадцать девять", 30:"половина", 
31:"тридцать одна", 32:"тридцать две", 33:"тридцать три", 34:"тридцать четыре", 35:"тридцать пять",
36:"тридцать шесть", 37:"тридцать семь", 38:"тридцать восемь", 39:"тридцать девять", 40:"сорок", 
41:"сорок одна", 42:"сорок две", 43:"сорок три", 44:"сорок четыре", 45:"пятнадцати", 
46:"четырнадцати", 47:"тринадцати", 48:"двенадати", 49:"одинадцати", 50:"десяти", 
51:"девяти", 52:"восьми", 53:"семи", 54:"шести", 55:"пяти", 56:"четырех", 57:"трех", 58:"двух", 59:"одной"}

H_0 = {0:"ноль", 1:"один",2:"два", 3:"три", 4:"четыре", 5:"пять",
6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять",
11:"одиннадцать", 12:"двенадцать"}

H_1 = {0:"первого", 1:"второго",2:"третьего", 3:"четвертого", 4:"пятого", 5:"шестого",
6:"седьмого", 7:"восьмого", 8:"девятого", 9:"десятого", 10:"одинадцатого",
11:"двенадцатого"}

if M==0:
   print(Mi[M],H_0[H],"часов")
elif M<30:
   print(Mi[M],Skl, H_1[H])
elif M==30:
   print(Mi[M],H_1[H])
elif M<45:
   print(Mi[M],Skl, H_1[H]) 
else:
   print("без", Mi[M],Skl, H_0[H+1])  