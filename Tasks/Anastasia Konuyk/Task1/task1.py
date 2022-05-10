deposit = 20000
percent = 15/100
years = 5
print(f'Deposit at the beginning of the period is {deposit} BYN, procent is {percent * 100}%')

for month in range(years * 12):
    income = deposit * percent / 12
    deposit += income

print(f'Deposit at the end of the period will be {deposit:.2f} BYN')
