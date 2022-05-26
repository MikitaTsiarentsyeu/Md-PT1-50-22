def spaces (x):
    if len(x) <= str_length:
        x = x.replace(' ', '  ', str_length - len(x))
    if len(x) <= str_length:
        x = x.replace('  ', '   ', str_length - len(x))
    if len(x) <= str_length:
        x = x.replace('   ', '    ', str_length - len(x))
    if len(x) <= str_length:
        x = x.replace('    ', '     ', str_length - len(x))
    if len(x) <= str_length:
        x = x.replace('     ', '      ', str_length - len(x))
    return x


str_length = input('Enter target string length (number 36+): ')
input_check = 0
while input_check == 0:
    try:
        int(str_length)
        input_check = 1
    except ValueError:
        str_length = input('enter digit, please ')
        input_check = 0
    else:
        str_length = int(str_length)

if str_length <=35:
    print('string length set to minimum (36 symbols)')
    str_length = 36
    

with open('new_text.txt', 'w') as f_new:
    with open('text.txt', 'r') as f:
        
        y = f.read(1)
        temp_x = ''

        while True:
            
            
            x = temp_x + y + f.read(str_length - 1 - len(temp_x))
            y = f.read(1)
            temp_x = ''
            
            if x == '':
                break
            
            if x.find('\n') != -1:
                x, temp_x = x.split('\n')
                x += '\n'
                x = x.lstrip()
                f_new.write(x)
            
            elif x[-1] in ('!', ',', '.', '?', '-'):
                x = x.lstrip()
                x = spaces (x)
                x += '\n'
                f_new.write(x)
                
            elif x[-1] == ' ':
                x = x.strip()
                x = spaces (x)
                x += '\n'
                f_new.write(x)
                
            elif x[-1] == '\n':
                x = x.lstrip()
                x = spaces (x)
                f_new.write(x)
                
            
                
            else:
                if y.isalpha() or y.isdigit() or y in ('!', ',', '.', '?', '-', '’', '“', '”', "'"):
                    x = list(x)
                    while x[-1] != ' ':
                        temp_x += x.pop(-1)
                    x = ''.join(x)
                    x = x.strip()
                    temp_x = temp_x[::-1]
                    x = spaces (x)
                    x += '\n'
                    f_new.write(x)
                                        
                elif y == ' ':
                    x = x.lstrip()
                    x = spaces (x)
                    x += '\n'
                    f_new.write(x)
                    
print('file with new string length was created\nnew file name is - new_text.txt')