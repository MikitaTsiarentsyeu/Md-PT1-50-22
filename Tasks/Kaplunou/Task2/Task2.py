import time
Choice=input("do you want input time or use current time? Yes or No: ")
if Choice == "Yes":
    Time = input("Input time in format hh:mm: ")
    Time=Time.split(":")
    CurentHour = int(Time[0])
    CurentMinute = int(Time[1])
else:
    seconds = time.time()
    CurrentTime = time.localtime(seconds)
    CurentHour = int(CurrentTime.tm_hour)
    CurentMinute = int(CurrentTime.tm_min)
print(CurentHour,CurentMinute)
digits=[' ', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = [' twenty ', ' thirty ', ' forty ', ' fifty ']

if  CurentHour >= 12 and CurentMinute < 45:
    CurentHour = CurentHour - 12
    if CurentHour <= 9:
        CurentHour=digits[CurentHour]
        Ch = str(CurentHour) + ' p.m.'
    else:
        CurentHour=teens[CurentHour - 10]
        Ch = str(CurentHour) + ' p.m.'
elif CurentHour < 12 and CurentMinute < 45:
    if CurentHour <= 9:
        CurentHour = digits[CurentHour]
        Ch = str(CurentHour) + ' a.m.'
    else:
        CurentHour = teens[CurentHour-10]
        Ch = str(CurentHour) + ' a.m.'
elif  CurentHour >= 12 and CurentMinute >= 45:
    CurentHour=CurentHour - 12
    if CurentHour <= 8:
        CurentHour=digits[CurentHour + 1]
        Ch = str(CurentHour)+' p.m.'
    else:
        CurentHour=teens[CurentHour - 9]
        Ch = str(CurentHour)+' p.m.'
elif CurentHour < 12 and CurentMinute >= 45:
    if CurentHour <= 8:
        CurentHour = digits[CurentHour + 1]
        Ch = str(CurentHour) + ' a.m.'
    else:
        CurentHour = teens[CurentHour - 9]
        Ch = str(CurentHour) + ' a.m.'    

if 0 < CurentMinute < 30:
    if CurentMinute <= 9:
        CurentMinute=digits[CurentMinute]
        Cm = str(CurentMinute) + " minutes past "
    elif 9<CurentMinute<20:
        CurentMinute=teens[CurentMinute - 10]
        Cm = str(CurentMinute) + " minutes past "
    else:
        CurentMinute=tens[0]+digits[CurentMinute - 20]
        Cm = str(CurentMinute) + " minutes past " 

elif CurentMinute == 0:
    Cm = '' 

elif CurentMinute == 30:
     Cm = " half past "

elif 30 < CurentMinute < 45:
    if CurentMinute < 40:
        CurentMinute=tens[1] + digits[CurentMinute - 30]
        Cm = str(CurentMinute) + " minutes past "
    else:
        CurentMinute=tens[2] + digits[CurentMinute - 40]
        Cm = str(CurentMinute) + " minutes past "
else:
    CurentMinute = 60 - CurentMinute
    if CurentMinute <= 9:
        CurentMinute=digits[CurentMinute]
        Cm = str(CurentMinute) + " minutes to "
    elif 9 < CurentMinute < 20:
        CurentMinute=teens[CurentMinute - 10]
        Cm = str(CurentMinute) + " minutes to "

Ct=Cm+Ch
print(Ct)
