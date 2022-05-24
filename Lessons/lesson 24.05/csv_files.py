import csv

headline = ['animal', 'name', 'color']
values = []

with open('test.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, headline)
    is_first = True
    for line in reader:
        if is_first:
            is_first = False
            continue
        values.append(list(line.values()))
        for hd_item in headline:
            print(f"{hd_item} - {line[hd_item]}", end=";")
        print('')

# headline = []
# values = []

# with open('test.csv', 'r', newline='') as f:
#     reader = csv.reader(f)
#     is_first = True
#     for line in reader:
#         if is_first:
#             headline.extend(line)
#             is_first = False
#             continue
#         values.append(line)

# headline = []
# values = []

# with open('test.csv', 'r', newline='') as f:
#     is_first = True
#     for line in f:
#         cells = line.replace('\r\n', '').split(',')
#         if is_first:
#             headline.extend(cells)
#             is_first = False
#             continue
#         values.append(cells)

# print(headline)
# print(values)

# for line in values:
#     for i in range(3):
#         print(f"{headline[i]} - {line[i]}", end=";")
#     print("")

print(headline)
print(values)

# with open("new_test.csv", 'w', newline='') as f:
#     f.write(','.join(headline) + "\r\n")
#     for value in values:
#         f.write(','.join(value) + "\r\n")

with open("new_test.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    # writer.writerow(["cell 1", "cell 2", "cell 3"])
    # writer.writerow(["cell 4"])
    # writer.writerow(["cell 5", "cell 6"])
    writer.writerow(headline)
    # for line in values:
    #     writer.writerow(line)
    writer.writerows(values)

with open("new_test.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    d = {}
    for value in values:
        for i in range(3):
            d[headline[i]] = value[i]
        writer.writerow(d)