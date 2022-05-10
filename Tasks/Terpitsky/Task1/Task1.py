from decimal import Decimal

years = 5
months = years * 12
percent_year = 15
initial_summ = 20000
final_summ = Decimal(initial_summ) * Decimal((1+((percent_year/100) / 12))**months)
print('Your money after', years, 'years:', final_summ.quantize(Decimal('1.00')), 'Yippee!')