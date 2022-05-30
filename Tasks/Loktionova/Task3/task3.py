with open ('text.txt', 'r', encoding='utf-8') as file, open('new_text.txt', 'w') as new:

    line = file.read().replace('\n', ' ')
            
    while True:
        length = int(input('Enter the number of characters per line between 35 and 100: ' ))

        if length < 35 or length > 100:
            print ('Entered data is incorrect')
            continue
        break

    i = 0
    while i < len(line) - 1:
        
        if line[i+length] == ' ':
            ind = length
        else:
            ind = line[i:i+length-1].rfind(' ')
            
        new_line = line[i:i + ind]
        if len (new_line) == length - 1:
            print(new_line, file=new)        
        else:
           new_string = list(new_line)           

        last_index = -1            
        while len(new_string) < length:
            last_index +=1
            if last_index + 1 > len(new_string):
                last_index = 0

            x = new_string[last_index]
            if x == ' ' and (last_index == 0 or new_string[last_index-1] != ' '):
                new_string.insert(last_index, ' ')
                last_index+=1           
                        
        print(''.join(new_string), file=new)
        
        i += ind + 1
        
        if  i + length >= len(line) -1:
            print(line[i:], file=new)
            break
print('New file was created')        