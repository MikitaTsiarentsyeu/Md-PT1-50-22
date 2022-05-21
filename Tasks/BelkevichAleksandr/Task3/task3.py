def selection():
    '''
    Function for checking selection input from user.

    '''
    while True:
        try:
            number = int(input("Please enter length line (minimum 36 maximum 70 characters): "))

            # check if the entered number is correct
            if 36 <= number <= 70:
                return number

            # output for explanation
            print(f"Error, {number} isn't within the specified range")
            print("The specified range line = min 36 and max 70 characters")
        except ValueError:
            print("ValueError, not an integer entered")
            continue


def converter_text_in_lst(lst):
    '''
    Function to sort text from a file by a specified length of lines from the user in list for list.

    '''
    lst_lines = []

    # iterating lines from text
    for elem in lst:
        # splitting a string into words
        mas_line = elem.split(" ")

        lst_word = []
        sum_mas_string = 0
        count = 0

        # iterating word from lines
        for x in mas_line:
            # notation to check string length with word and space
            sum_mas_string += len(x) + 1
            # variable to check the last word in the line
            count += 1

            if sum_mas_string < string_len and count == len(mas_line):
                lst_word.append(x)
                lst_word.append("\n")
                lst_lines.append(lst_word)
                lst_word = []
            elif sum_mas_string < string_len:
                lst_word.append(x)
                lst_word.append(" ")
            else:
                del lst_word[-1::]
                sum_mas_string -= len(x) + 2 # 2 is the two spaces between the last word in the length list
                correct_line = correct_line_for_len_string(lst_word, sum_mas_string)
                lst_lines.append(correct_line)
                lst_word = []
                sum_mas_string = len(x) + 1
                lst_word.append(x)
                lst_word.append(" ")

        #Question? I can delete not needed variables here or not
        #del lst_word
        #del sum_mas_string
        #del count

    return lst_lines


def correct_line_for_len_string(line_from_the_top_function, sum_len):
    '''
    Function to align text in a string along the entire length.

    '''

    difference_len = string_len - sum_len
    count = 1

    # cycle to insert spaces
    while difference_len > 0:
        line_from_the_top_function.insert(count, " ")
        # increment count to insert space after next word
        count += 3
        # check count for not out of bounds line
        if count >= len(line_from_the_top_function) - 1:
            count = 2
        difference_len -= 1

    return line_from_the_top_function


lst_text = []
string_len = selection()

# reading from a file
with open(r"Tasks/!Tasks/Task3/text.txt", "r", encoding = "utf-8") as f:
    lst_text = f.read().split("\n")


lst_final = converter_text_in_lst(lst_text)

# writing to file
with open("Tasks/BelkevichAleksandr/Task3/correctedText.txt", "w", encoding="utf-8") as r:
    r.write(f"String length is {string_len} characters \n\n")

    for x in lst_final:
        r.write("".join(x))
        r.write("\n")

    print(f"The file is written correctly with the line length {string_len}")