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
def just(input_string: str, lim: int):
    
    s = input_string       
    l = []
    w=0             
    for d in s.split():
        if w + len(d) + 1 <= lim:
            l.append(d)
            w += len(d) + 1  
                                             
        else:
            print (" ".join(l))
            l = [d] 
            w = len(d)

    if (len(l)): print (" ".join(l))    
    return " ".join(l)
   # I have a question. How can I return the entire function in my result, not just the last iteration (the last line of text) and write it in the new file?
with open('text.txt', 'r', encoding= 'utf-8') as old:
    input_string = old.read() 
    n = just(input_string, lim)

with open('newtext.txt', 'a') as new:
    new.write(n)

print(f"The new file successfully created  with {lim} characters")