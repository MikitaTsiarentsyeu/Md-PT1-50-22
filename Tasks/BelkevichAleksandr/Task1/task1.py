deposit = int(input("Input your deposit: "))
tern = int(input("Input deposit terns: ")) * 12
persentage = int(input("Input annual percentage: ")) / 100

count_mouth = 0

while count_mouth < tern:
    month_capital = deposit * (persentage) / 12
    deposit += month_capital
    count_mouth += 1
    print(f"Interest on deposit for {count_mouth} mouth = {month_capital}")

print(f"Amount at the end of the deposit {round(deposit, 2)}")