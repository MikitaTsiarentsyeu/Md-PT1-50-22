"""Task1."""

import decimal

init_dep = decimal.Decimal(20000)
print(init_dep)
ann_rate = decimal.Decimal(15)
print(ann_rate)
term_contr = decimal.Decimal(5)
print(term_contr)
fin_inc = init_dep * (1 + ann_rate / 100 / 12)**(12 * term_contr)
print('Amount in the account after 5 years:', round(fin_inc, 2), 'BYN')
