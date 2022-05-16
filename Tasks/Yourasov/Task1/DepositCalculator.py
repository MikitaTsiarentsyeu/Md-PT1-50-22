import decimal

amount = decimal.Decimal(input('Enter deposit amount: '))
term = decimal.Decimal(input('Enter deposit term, years: '))
rate = decimal.Decimal(input('Enter deposit interest rate in %: '))
total_sum = amount * (1 + rate / 100 / 12)**(term * 12)
total_rate_sum = total_sum - amount
print('Total deposit amount =', '{:,.2f}'.format(total_sum).replace(',', ' '), end=', ')
print('included amount of interest =', '{:,.2f}'.format(total_rate_sum).replace(',', ' '))