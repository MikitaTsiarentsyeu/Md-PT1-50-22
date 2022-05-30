from ast import Break, Continue


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


    
while True:
    
    str_length = input('Enter target string length (number 36+): ')

    if not str_length.isdigit():
        print ('enter digit please')
        continue
    
    str_length = int(str_length)
        
    if str_length <=35:
        print('string length is less than minimum (36 symbols)')
        continue
        
    break


with open('new_text.txt', 'w') as f_new:
    with open('text.txt', 'r') as f:
        
        y = f.read(1)
        temp_x = ''

        while True:
            
            
            x = temp_x + y + f.read(str_length - 1 - len(temp_x))
            y = f.read(1)
            temp_x = ''
            
            if not x:
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