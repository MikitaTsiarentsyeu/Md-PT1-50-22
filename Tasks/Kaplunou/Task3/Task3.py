filename = 'text.txt'

try:
    with open(filename, 'r') as f:
        lines=f.readlines()
    file = ''
    for l in lines:
        file += l.strip()
        
except FileNotFoundError:
    print(f'Sorry, the file {filename} does not exist')
else:
    while True: 
        length=input('Enter a string length greater than 35 characters: ')     
        if length.isalpha() == True or float(length)%1 != 0 or int(length) <= 35:
            print('invalid values! Enter correct values!')            
        else:
            break
    
    length=int(length)
    file = file.split()
    array = []   
    
    def lin(file):
        
        if len(' '.join(file)) <= length:
            line = ' '.join(file)
            array.append(line)
            return line

        line = ''
        i = 0

        while len(line) <= length:
            if len(' '.join(file[0:i]))>length:
                break
            line = ' '.join(file[0:i])
            i += 1
            
        line=line.split(' ')
        
        while True:
            for j in range(len(line) - 1):
                if len(' '.join(line)) >= length:
                    break
                line[j] += ' '
            if len(' '.join(line)) == length:
                break

        line = ' '.join(line)  
        array.append(line)
        file = file[i-1:]
        return lin(file)
    lin(file)

    with open("editet_text.txt", 'a') as object:
        for b in range(len(array)):
            object.write(f"{array[b]}\n")
    print(f'The file {filename} has been edited and saved as "editet_text.txt"')
