from logging.config import valid_ident


while True:
    try:
        val = int(input("Please, enter value from 36 to 70:\n "))
        if 36 > val:
            print("Incorrect value")
        elif 70 >= val > 35:
            print(f"accepted value {val}")
            break
        elif val > 70:
            print("Incorrect value")
    except ValueError:
        print("Please, use value")
lim = val
with open('text.txt', 'r', encoding= 'utf-8') as old:
    s = old.read() 

s=s.replace("\n", "")
last_position=len(s)-1
 
split_len= val
list_of_records=[]
start=0
 
while True:
    end=start+split_len+1 
    rec=s[start:end].strip()
    ctr = -1       
    if end < last_position:
        
        while rec[ctr] != " ":     
            ctr -= 1
 
        list_of_records.append(rec[:ctr].strip())
        start += len(rec[:ctr])+1     
    else:   
        list_of_records.append(s[start:].strip())
        break
with open('correctedtext.txt', 'w', encoding='utf-8') as new:
    new.write("\n".join(list_of_records))
    
print(f"The new file successfully created  with {val} characters")