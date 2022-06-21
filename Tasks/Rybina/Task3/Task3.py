while True:
    try:
        str_length = int(input("Please enter a number of symbols from 30 to 50: "))
        if str_length > 50:
            print("The number is more than 50")
        elif str_length < 30:
            print("The number is less than 30")
        else:
            print("The entered length of line is ", str_length)
            break
    except ValueError:
        print("Please enter only numbers")

with open("text.txt", 'r') as origin:
    with open("new_text.txt", 'w') as new_file:
        text_lines = origin.readlines()
        for s in text_lines:
            s = s.replace('\n', ' ')
            words = s.split(' ')
            auxiliary_list = []
            i = 0
            for w in words:
                if len(w) + 1 + i <= str_length-1:
                    auxiliary_list.append(w)
                    if i == 0:
                        i += len(w)
                    else:
                        i += len(w) + 1
                else:
                    adding_spaces = str_length-1 - i
                    space_quantity = adding_spaces * " "
                    auxiliary_list.append(space_quantity)

                    new_line = ' '.join(auxiliary_list) + '\n'
                    new_file.writelines(new_line)
                    auxiliary_list = []
                    i = len(w)
                    auxiliary_list.append(w)
            new_line = ' '.join(auxiliary_list) + '\n'
            new_file.writelines(new_line)

print(f"A new text file was created with line length of {str_length} characters")