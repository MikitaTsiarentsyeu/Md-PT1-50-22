def user_selection():
    while True:
        try:
            num = int(input("Please enter the number of characters in each line.\n"
                            "String length must be between 36 and 100 characters.\n"
                            ": "))
            if 35 < num < 101:
                return num

            else:
                print("The entered number of characters is out of range")
        except ValueError:
            print("The entered value is not a numeric value. Try again\n\n\n")


def to_correct_list(line_in_list, num_of_characters):
    """formats into inserted list. Each of which contains a string in the correct form"""
    formatted_list = []
    len_of_elements = 0
    one_line = []
    for word in line_in_list:
        index = 1
        if len_of_elements + len(word) > num_of_characters:
            del (one_line[-1]) # del last space from list
            whole_len = len(''.join(one_line))
            spaces_left = num_of_characters - whole_len
            while spaces_left != 0:
                one_line.insert(index, ' ')
                index += 3
                if index >= len(one_line):
                    index = 2
                spaces_left -= 1

            formatted_list.append(one_line)
            len_of_elements = len(word) + 1
            one_line = [word, ' ']
        else:
            one_line.append(word)
            one_line.append(' ')
            len_of_elements += len(word) + 1  # plus one space for each word
    else:   # If the cycle ends - add the remaining words
        formatted_list.append(one_line)
    return formatted_list


def to_correct_string(num: int):
    with open("text.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line_in_list = line.split()
            correct_list = to_correct_list(line_in_list, num)

            with open('correct_text_with_60_symbols', 'a', encoding='utf-8') as file:
                for string in correct_list:
                    string.append('\n')
                    file.write(''.join(string))


num_of_characters = user_selection()    # input user selection
to_correct_string(num_of_characters)
