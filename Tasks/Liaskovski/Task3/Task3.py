while True:
    try:
        num = int(input("Please write your number from 36 till 70:\n "))
        if 36 > num:
            print("It should be more than 36")
        elif 70 >= num > 35:
            print(f"Thank you, your choice is {num}")
            break
        elif num > 70:
            print("Out of the range, please try again")
    except ValueError:
        print("Please, use numbers")
lim = num
with open('text.txt', 'r', encoding= 'utf-8') as old:
    s = old.read() 

s=s.replace("\n", "")
last_position=len(s)-1
 
split_len= num
list_of_records=[]
start=0
 
while True:
    end=start+split_len+1 # +1=allow for space=next character
    rec=s[start:end].strip()
    ctr = -1       
    if end < last_position:
        ## look for space from right to left
        while rec[ctr] != " ":     ## assumes space, or more than one word here
            ctr -= 1
 
        list_of_records.append(rec[:ctr].strip())
        start += len(rec[:ctr])+1     ## +1 = skip space
    else:   ## end of file reached
        list_of_records.append(s[start:].strip())
        break
with open('newtext.txt', 'w', encoding='utf-8') as new:
    new.write("\n".join(list_of_records))
    
print(f"The new file successfully created  with {num} characters")