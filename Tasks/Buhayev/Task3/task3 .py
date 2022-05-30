import time
def check_input(func):
    def wrapper():
        while True:
            try:
                string_width = func()
                time.sleep(.2)
                try:
                    assert string_width > 34
                except:
                    
                    print('\nSorry string width is to small\n')
                    time.sleep(.2)
                    continue

                try:
                    assert string_width < 51
                except:
                    print('\nSorry string width is to big\n')
                    time.sleep(.2)
                    continue
                return string_width
            except:
                print('\nSorry invalid input, width must be digit\n')
                time.sleep(.2)
                continue
    return wrapper

@check_input
def input_string_width():
    return int(input('Please enter a string width (a digit between 35 and 55)\n:   '))

def split_line(line, width):
    workline, check = line[0:width], line[width]
    workline_arr = workline.split()
    return workline, check, workline_arr


def check_integrity_last_word(workline, check_next_char, workline_arr):
    if check_next_char != ' ' and workline[-1] != ' ':
        len_last_word_of_line = len(workline_arr.pop())
    else:
        len_last_word_of_line = 0
    return len_last_word_of_line


def adding_spaces(workline_arr, width):
    while True:
        for i in range(len(workline_arr) - 1):
            if len(' '.join(workline_arr)) >= width:
                return ' '.join(workline_arr) + '\n'
            workline_arr[i] += ' '


def main():
    width = input_string_width()
    residual_line = ''
    formatted_lines_list = []

    with open('text.txt', 'r') as inp, open('format.txt', 'w') as out:

        for line in inp:

            while True:
                if len(line) <= width:
                    residual_line = line
                    break

                workline, next_char_after_workline, workline_arr = split_line(line, width)

                len_last_word_of_line = check_integrity_last_word(workline, next_char_after_workline, workline_arr)

                formatted_line = adding_spaces(workline_arr, width)

                line = line[(width - len_last_word_of_line):len(line)]

                formatted_lines_list.append(formatted_line)

            formatted_lines_list.append(residual_line)

        out.writelines(formatted_lines_list)
        print('formatted document created')


if __name__ == '__main__':
    main()
