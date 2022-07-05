import locale

print(locale.getpreferredencoding()) # to delete

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

n = 0

while True:
    print(f'''{'' if n > 0 else 'Dear User,'}
{'P' if n > 0 else 'p'}lease, enter the maximal quantity of symbols in the line (more than 35) {'again' if n > 0 else ''}
in order to justify the text and to make it more beautiful:''')

    n += 1

    width = input()

    if not is_number(width):
        print('\nPlease, type only integer.')
        continue


    if int(width) <= 35:
        print('\nPlease, type the amount of symbols more than 35.')
        continue
    
    break
    
width = int(width)

# The concept relized is:
# 1) Load the chunk and define the last whole word in the line
# 2) Clear all spaces in the beggining and in the end of the line
# 3) Make the line justified along the width desired by user (excl. the piece with '\n' in the end)
# 4) Record into the new file



with open('text.txt', 'r', encoding= 'utf-8') as f:
    
    line = ''

    with open('text2.txt', 'w', encoding= 'utf-8') as f_new:

        while True:

            chunk = f.readline(width)


            if not chunk:
                break

            if not '\n' in chunk:
                
                p_i = ''
                n = 0
                for i in chunk[::-1]:
                                
                    if (p_i == ' ' or p_i == '\t') and (i != ' ' and i != '\t'):
                        line = chunk[0:len(chunk)-n] # 
                        f.seek(f.tell() -n)
                        
                        break
                    
                    p_i = i
                    n += len(i.encode('utf-8'))
                else:
                    
                    line = chunk + '\n' # if there is only one word in the chunk

                

            else:
                line = chunk # if there is the line with '\n' in the chunk


        
            while '  ' in line:
                line = line.replace('  ', ' ')


            
            t_just_l = line.split(' ')

            i = 0
            for i in range(len(t_just_l)):
                if i == len(t_just_l): # I'm trying to understand the error: in some cases range generated the figure equal of function range arguement.
                    break
                if t_just_l[i] == '':
                    t_just_l.pop(i)
                else:
                    break

                
            for i in range(1 if not '\n' in line else 2, len(t_just_l)+1):
                if t_just_l[i*(-1)] == '':
                    t_just_l.pop(i*(-1))
                else:
                    break


            line = ' '.join(t_just_l)


            if not '\n' in line: # Due to the piece of text with paragraph in the end is left
                                 #without justification in MS Word, the decision is to do the same.
            
                
                if ' ' in line:
                    q_sp_wid = width - len(line)

                    tj_list = line.split(' ')
                    q_sp_cur = len(tj_list) - 1

                
                if q_sp_wid % q_sp_cur > 0:
                    n_i = 0
                    for i in range(len(tj_list)):
                        n_i += 1
                        tj_list[i] = tj_list[i] + ' '

                        if q_sp_wid % q_sp_cur == n_i:
                            break

            
                res_sp = ' '*((q_sp_wid // q_sp_cur) + 1)

                line = res_sp.join(tj_list) + '\n' 

            
            f_new.write(line)

    

print('The file with text justified is recorded. Please, enjoy:)')


