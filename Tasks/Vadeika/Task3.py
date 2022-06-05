"""Task3."""

# User input. Validity check input.
while True:
    user_int = input("Enter the number of characters per line from 36 to 50:")
    if not user_int.isdigit():
        print("Incorrect input!")
        continue
    user_enter = int(user_int)
    if user_enter > 50:
        print("Incorrect input!")
        continue
    elif user_enter < 36:
        print("Incorrect input!")
        continue
    else:
        print(f'Successfully! You entered a number:{user_enter}')
    break

# Reading the file.
with open(r'D:\WORK\PY\Python_less\TEMP\temp_text.txt', 'r', encoding='utf-8') as f:
    file = f.read().split(' ')

# Splitting text into parts of a given length.
list_main = []
list_word = []
summ_char_count = 0
char_count = 0
rew_user_length = user_enter
for i in file:
    summ_char_count += len(i) + 1
    char_count += len(i) + 1
    rew_user_length -= char_count
    char_count = 0
    if rew_user_length > 0:
        list_word.append(i)
        list_word.append(' ')
    if summ_char_count > user_enter or rew_user_length == 0:
        summ_char_count = 0
        list_word.pop()
        list_word.append("\n")
        list_main.append(list_word)
        list_word = []
        list_word.append(i)
        list_word.append(' ')
        rew_user_length = user_enter - len(i)
list_word.pop()
list_word.append("\n")
list_main.append(list_word)
list_word = []

# Formatting lines of text.
box_1 = []
box_2 = []
box_3 = []
box_4 = []
end_up = 0
end_down = 0
letters = [letter for char in list_main for letter in char]
end_down = letters.count('\n')
for item in list_main:
    len_line = 0
    for j in item:
        box_1.append(j)
        len_line += len(j)
        space = item.count(' ')
    len_line = len_line - 1
    end_up += item.count('\n')
    if len_line < user_enter:
        n = 0
        space_box1 = 0
        space = user_enter - len_line
        while space_box1 < space and end_down > end_up:
            box_2 = box_1[n]
            n += 1
            if box_2 == ' ' or box_2 == '  ' or box_2 == '   ' or box_2 == '    ' or box_2 == '     ' or box_2 == '      ' or box_2 == '       ':
                space_box1 += 1
                box_2 = box_2 + ' '
                box_3.append(box_2)
            else:
                box_3.append(box_2)
            if space_box1 < space and end_down > end_up and box_2 == '\n':
                n = 0
                box_1 = []
                box_1.extend(box_3)
                box_3 = []
        while space_box1 == space:
            if box_2 == '\n':
                box_4.append(box_3)
                box_3 = []
                box_2 = []
                box_1 = []
                space = 0
                break
            box_2 = box_1[n]
            box_3.append(box_2)
            n += 1
        while end_down == end_up:
            box_2 = box_1[n]
            box_3.append(box_2)
            n += 1
            if box_2 == '\n':
                box_4.append(box_3)
                box_3 = []
                box_2 = []
                box_1 = []
                space = 0
                break

# Writing the result to a file.
with open("Text_write.txt", "w", encoding="utf-8") as rec:
    rec.write(f"String length is {user_enter} simbols \n\n")
    for item in box_4:
        rec.write("".join(item))
    print(f'Successfully! Line length - {user_enter}')
