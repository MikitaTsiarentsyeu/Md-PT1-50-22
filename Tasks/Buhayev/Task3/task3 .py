def input_width():
    while True:
        try:
            width = int(input('Please enter a string width (integer number between 35 and 55)\n:   '))
            try:
                assert width > 34
            except:
                print('Sorry string width is to small')
                continue

            try:
                assert width < 51
            except:
                print('Sorry string width is to big')
                continue

        except:
            print('Sorry invalid input')
            continue
        return width


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
    width = input_width()
    residual_line = ''
    formatted_lines_list = []

    with open('text.txt', 'r') as inp, open('format.txt', 'w') as out:

        for line in inp.readlines():

            while True:
                if len(line) < width:
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
