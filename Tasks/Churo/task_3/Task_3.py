import re

while True:
    line_length = (input('input line length would you want, but more then 35 elements : \n'))
    if not re.findall(r'^\d+$', line_length):
        continue
    line_length = int(line_length)

    if line_length <= 35:
        print(f"Incorrect input! The value 'line_length' does not match the condition. Please, try again \n")
        continue
    else:
        break

with open('text.txt', 'r+') as source_file:
    content = source_file.readlines()
result = []
for line in content:
    matches = re.findall(f'(.{{1,{line_length}}})(?: |$)', line)
    for match in matches:
        diff_spaces = (line_length - len(match))
        total_spaces = match.count(' ')
        lst = match.split(' ')

        for i in range(diff_spaces % total_spaces if total_spaces != 0 else 0):
            lst[i] += ' '
        result.append((' '*(diff_spaces // total_spaces + 1 if total_spaces != 0 else 0)).join(lst) + '\n')


with open('new_text.txt', 'w') as f:
    f.writelines(result)



