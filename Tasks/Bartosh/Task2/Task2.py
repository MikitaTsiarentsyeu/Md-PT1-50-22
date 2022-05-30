from datetime import datetime
#dictionaries 
digits = {1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 
7:'семь', 8:'восемь', 9:'девять', 10:'десять', 11:'одинадцать', 12:'двенадцать', 0:'двенадцать', 
13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семьнадцать', 18:'восемьнадцать', 19:'девятнадцать', 20:'двадцать'}

digits_2 = {2:'двух',  3:'трёх',  4:'четырёх',  5:'пяти',  
6:'шести',  7:'семи',  8:'восьми',  9:'девяти',  10:'десяти',  
11:'одинадцати',  12:'двенадцати',  13:'тринадцати',  14:'четырнадцати',  15:'пятнадцати', }

digits_3 = {1:'одна', 2:'две'}

digits_4 = {2:'двадцать', 3:'тридцать', 4:'сорок'}

hours_next = {0:'первого', 1:'второго', 2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 6:'седьмого', 
7:'восьмого', 8:'девятого', 9:'десятого', 10:'одинадцотого', 11:'двенадцотого'}

#input option selection
option = int(input('Hello! I can write time by words.\nPress 1, if you want to know current time\nor\npress 2 (or any key), if you want to enter time in hh:mm format\n1/2?:'))

# option 1 for current time
if option == 1:
    timestamp = datetime.now()
    t = str(timestamp.hour)+':'+str(timestamp.minute)
# 2 (or any key) for input from keyboard
else:
  t = input ('press time in hh:mm format:')
  while True:
  #find length
    t_len = len(t) 
    if (':' in t) ==True and t_len == 5 and int(t.split(':')[0])>=0 and int(t.split(':')[0])<=23 and int(t.split(':')[1])>=0 and int(t.split(':')[1])<=59: 
        break
    #no :
    elif (':' in t) == False:
        t = input('Your time should content sigh ":". Please enter time in hh:mm format:')
    # wrong lenght of string
    elif t_len != 5:
        t = input('Enter 5 signs including ":". Please enter time in hh:mm format:')
    # wrong hours
    elif int(t.split(':')[0])<0 or int(t.split(':')[0])>23:    
        t = input('Hours should be between 0 and 23. Please enter time again:')
    elif int(t.split(':')[1])<0 or int(t.split(':')[1])>59:    
        t = input('Minutes should be between 0 and 59. Please enter time again:')
    
hh = int(t.split(':')[0])
if hh>12:#change 24 format to 12 format
  hh = hh-12
else:
  hh = hh

mm = int(t.split(':')[1])

if len(str(mm)) == 1:
  mm1 = 0
  mm2 = mm
else:
  mm1 = int(list (t)[3])
  mm2 = int(list (t)[4])

#for the midnight
if hh == 0 and mm == 0:
    print ('полночь')

#for the midday
elif hh == 12 and mm == 0:
    print ('полдень')
#for the case 15:00
elif mm == 0:
  if hh==1:
    hour_word = 'час'
  elif hh >= 2 and hh < 5:
    hour_word = 'часа'
  else:
    hour_word = 'часов'

  print (digits[hh], hour_word, 'ровно')

#for the case 15:30 
elif mm==30:
  print ('половина', hours_next[hh])

#for the case when there are less than 15 minutes left before the end of the hour
elif mm >= 45:
  mm_end= 60-mm
  if mm_end == 1:
    print ('без одной минуты', digits[hh+1])
  else:
    print ('без', digits_2[mm_end], 'минут', digits[hh+1])

#for all other cases
else:
  #for the correct declension of the word 'minute'
  if mm1 != 1 and mm2 ==1:
    minute_word = 'минута'
  elif mm1 != 1 and mm2>=2 and mm2<=4:
    minute_word = 'минуты'
  else:
    minute_word = 'минут'

  if mm <= 2:
    minutes = digits_3[mm]
  elif mm > 2 and mm <20:
    minutes = digits[mm]
  elif mm >=20 and mm2!=0:
    minutes = digits_4[mm1] +' '+ digits[mm2]#from two numbers collect one
  else:
    minutes = digits_4[mm1]

  print (minutes, minute_word, hours_next[hh])