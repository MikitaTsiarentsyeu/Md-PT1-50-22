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

with open('text.txt','r', encoding= 'utf-8') as t:
    input_string = t.read()
    lim = num
    for s in input_string.split("\n"):
        if s == "": print
        w=0 
        l = []
    
        for d in s.split():
            if w + len(d) + 1 <= lim:
                l.append(d)
                w += len(d) + 1 
            else:
                print (" ".join(l))
                l = [d] 
                w = len(d)
        if (len(l)): print (" ".join(l) )

        with open("newtext.txt","w") as r:
            for l in input_string.split():
                r.write(" ".join(l))
                r.write("\n")
        


    print(f"The new file successfully created  with {num} characters")