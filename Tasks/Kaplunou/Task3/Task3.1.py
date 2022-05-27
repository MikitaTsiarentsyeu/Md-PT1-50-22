while True: 
    length=input('Enter a string length greater than 35 characters: ')     
    if length.isalpha() == True or float(length)%1 != 0 or int(length) <= 35:
        print('invalid values! Enter correct values!')            
    else:
        break

length=int(length)
array = []

def lin(l):
        
    line = ''
    i = 0

    while len(line) <= length:
        if len(' '.join(l[0:i])) > length:
            break
        line = l[0:i]
        i += 1
        
    while True:
        for j in range(len(line) - 1):
            if len(' '.join(line)) >= length:
                break
            line[j] += ' '
        if len(' '.join(line)) == length:
            break

    line = ' '.join(line)  
    array.append(line)
    l = l[i-1:]

    if len(' '.join(l)) <= length:
        line = ' '.join(l)
        array.append(line)
        l = []
        return array
       
    return lin(l)  

try:
    with open('text.txt', 'r') as f:
        lines=f.readlines()
        for l in lines:
            l = l.split(' ')
            lin(l)
        
except FileNotFoundError:
        print(f'Sorry, the file "text.txt" does not exist')

with open("editet_text.txt", 'a') as object:
        for b in range(len(array)):
            object.write(f"{array[b]}\n")
print(f'The file has been edited and saved as "editet_text.txt"')