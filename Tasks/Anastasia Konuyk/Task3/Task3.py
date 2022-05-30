def lenline():
    while True:
        try:
            lenght = int(input("Please enter length line (more than 35 characters): "))
            if lenght > 35:
                return lenght
            print(f"The {lenght} isn't correct, try again")
        except ValueError:
            print("ValueError")
        continue

wight = lenline()

def justify(text_from_file):
    words = list(reversed(text_from_file.split()))
    result = []
    while words:
        line = [words.pop()]
        count = len(line[0])
        while words and count + len(words[-1]) + 1 <= wight:
            line.append(words.pop())
            count += len(line[-1]) + 1
        if len(line) == 1 or not words:
            result.extend(' '.join(line))
        else:
            num_spaces = wight - sum(len(word) for word in line)
            q, r = divmod(num_spaces, len(line) - 1)
            pads = [0 if indx == 0 else q if indx > r else q + 1 for indx in range(len(line))]
            result.extend(' ' * pad + word for pad, word in zip(pads, line))
        result.append('\n')
    return ''.join(result)


with open("text.txt", "r", encoding = "utf-8") as old:
    text_from_file = old.read()
    lst_final = justify(text_from_file)

with open("tmp.txt", "w", encoding="utf-8") as new:
    new.write(f"The text was written to a new file with {wight} characters in line\n\n")
    new.write(str(lst_final))
