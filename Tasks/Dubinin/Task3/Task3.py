import math

while True:
       L = input('Please enter maximum number symbol in the string (more than 35):')
       if not L.isdigit():
           print ('Incorrect input, please enter number')
           continue

       L = int(L)

       if L<36:
           print ('Incorrect input, please enter number more than 35')
           continue
       break


with open("ftext.txt", 'w'): pass   #clean file

with open("text.txt", 'r') as f:
     Line_text = f.readlines()
Number_lines= len(Line_text)

for i in range(Number_lines):
    Length_modif = L 
    Pozition = 0
    Text_i = Line_text[i]
  
    while True:
     x = Text_i[Pozition:Pozition+L+1]   
     if x == '':
       break

     s = (x[::-1]) 
     Length_modif = L - s.find(' ') #Length modifided string by space and length
     
     x = Text_i[Pozition:Pozition+Length_modif] #text for spacing
     
     Pozition += Length_modif+1
   
     N_add_sp = L - Length_modif #Number additional spaces for string with right width
     Str1 = x.split(' ')
     L_Str1 = len(Str1)
     n_sp_all = N_add_sp // (L_Str1) #Number spaces between all words
     n_sp_s = N_add_sp % (L_Str1) #Number additional spaces 
     for i in range(n_sp_s):
            Str1[i] += " "
     A = " "*(n_sp_all+1)
     Str_f = A.join(Str1) 
         
     with open("ftext.txt", 'a') as f:
          f.write(Str_f+'\n')
   
print('The new formated file - ftext.txt has been written')
#with open("ftext.txt", 'r') as f:
#    print(f.read())

