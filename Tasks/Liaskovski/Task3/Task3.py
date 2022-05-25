while True:
    try:
        num = int(input("Please write your number from 36 till 70:\n "))
        if 36 > num:
            print("It should be more than 36")
        elif 70 >= num > 35:
            print(f"Thank you, your choice is {num}")
            break
        elif num > 70:
            print("Out of the range, please try again")
    except ValueError:
        print("Please, use numbers")

path_to_file = 'text.txt'

with open("text.txt", "r", encoding= 'utf-8') as text:
    def read(text_file: str, line_length: int = num):
        with open(text_file, 'r', encoding= 'utf-8') as text:
            line = None
            while line != '':
                line = text.read(line_length)
                yield line

    def print_by_width(text_file, line_length):    
        for row in read(text_file, line_length):
            print(row)
        return
    print_by_width(path_to_file, num)

file1 = open("text.txt")
file2 = open("newtext.txt", "w")

file2.write(file1.read())
file1.close()
file2.close()

print(f"New file successfully created  with {num} characters")