import os

#input and validation block
while True:
    try:
        max_len_str = int(input('Please enter the maximum number of characters per line:'))
    except ValueError:
       print("Please, write down integer number")
       continue

    if max_len_str >= 35 and max_len_str <=100:
        break
    
    elif max_len_str < 35:
       print('The number must be greater than 35')
    elif max_len_str > 100:    
       print('The number must be less than 100')

#open the file, read, #insert \n every max_len_str index, but if in this index isn't ' ' find previous ' ' and store it
with open ("text.txt",'r', encoding='utf_8' ) as donor:
    with open ("file1.txt",'w', encoding='utf_8') as receiver:
        row = donor.read()
        row = list (row)
        i = max_len_str
        while i < len (row):
            while row[i] != ' ':
                i = i-1
            else:
                i=i
                row[i] = '\n'
                i +=max_len_str+1
            
        receiver.writelines(row)
            
#insert many spaces
with open ("file1.txt",'r', encoding='utf_8' ) as donor:
    with open ("file2.txt",'w', encoding='utf_8') as receiver: 
        for x in donor:
            row=list(x)
            #count ' '. How many ' ' we have 
            spaces = 0
            for i in row:
                if i == ' ':
                    spaces +=1
            need = max_len_str - len(row)
            #indexes with ' '
            indexes = []
            ind = 0
            for i in row:
                if i == ' ':
                    indexes.append(ind)
                ind +=1
            #count how many spaces we need insert
            if spaces>0:
                count_spaces = need//spaces
            else:    
                count_spaces = need

            #insert spaces
            if need<= spaces:
                receiver.writelines(row)
            else:    
                indexes_new = []

                y= 0

                for i in indexes:
                    indexes_new.append(i+y)
                    y+=count_spaces

                for i in indexes_new:
                    y=0
                    while y < count_spaces:
                        row.insert (i, ' ')
                        y+=1
                receiver.writelines(row)

#insert additional spaces          
with open ("file2.txt",'r', encoding='utf_8' ) as donor:
    with open ("converted_text.txt",'w', encoding='utf_8') as receiver: 
        for x in donor:
            row=list(x)
            if len(x)==max_len_str+1:
                receiver.writelines(row)
            else:    
                #count ' '. How many ' ' we have 
                spaces = 0
                for i in row:
                    if i == ' ':
                        spaces +=1
                
                #how many ' ' we need
                need = max_len_str - len(row) +1

                #indexes with ' '
                indexes = []
                ind = 0
                for i in row:
                    if i == ' ':
                        indexes.append(ind)
                    ind +=1 

                #calculate new indexes for insert
                indexes_new = [] 
                y= 0
                for i in indexes:
                    indexes_new.append(i+y)
                    y+=1
                
                #leave only the necessary spaces
                indexes_new = indexes_new[0:(need)]
                for i in indexes_new:
                    y=0
                    row.insert (i, ' ')
                    y+=1
                receiver.writelines(row)
          
              
# remove additional files
os.remove ("file1.txt")
os.remove ("file2.txt")
# tell users when they can find file 
print (f"We successfully have written new file. You can find it in {os.getcwd()}{os.sep}converted_text.txt")