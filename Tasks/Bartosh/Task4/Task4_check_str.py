def check_str (s):
    up = 0
    low = 0  
    for i in (''.join(x for x in s if x.isalpha())):
        if i.isupper():
            up +=1
        elif i.lower():
            low +=1
    res = (f"{up} upper case, {low} lower case")
    return res


