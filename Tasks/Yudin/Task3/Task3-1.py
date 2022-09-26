while True:
    s_long = input ("Please, enter value from 36 to 50:\n ")
    if not s_long.isdigit():
        print ('Incorrect value, must be digit')
        continue
    s_long = int(s_long)
    if s_long < 35 or s_long > 50:
        print ('Incorrect value')
        continue
    break

form_srt = ""
f_name="correctedtext.txt"

f = open (f_name, 'w')
f.close()

def white_formated_file(some_str):
    with open (f_name, 'a+', encoding='utf8') as f:
        f.write(f"{some_str}\n")

def str_format(some_str):
    j=1
    i=0
    some_str=some_str.strip(" ")
    while  i <= s_long:
        if len(some_str) == i:
            i = -1
            j +=1
        elif some_str[i] == " ":
            some_str = some_str[:i]+" "+some_str[i:]
            i +=j
        elif len(some_str) == s_long:
            break
        elif j > s_long:
            break
        i +=1
    return some_str

with open ("text.txt", 'r', encoding='utf8') as f:
     for line in f:
        s_new = line.split()
        x = len(s_new)

        for i in range(x):
            s2_long = form_srt + s_new[i] + ' '
            if len(s2_long) <= s_long:
                form_srt=s2_long
            else:
                white_formated_file(str_format(form_srt))
                form_srt = s_new[i]+' '
     
     white_formated_file(str_format(form_srt))

print("Created new file as name is \"correctedtext.txt\"")     
    



