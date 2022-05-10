deposit = int(input('enter the deposit amount at BYN: '))
term = int(input('enter the term of the deposit in months: '))
percent = int(input('enter annual percentage: '))
n = percent / 100
amount_on_account = deposit * ((1 + n / 12 )**term)
print (int(amount_on_account))
