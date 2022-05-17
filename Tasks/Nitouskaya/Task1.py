#deposit:
#Start = 20000
#Term = 5 years
#Percent = 15%
# monthly capitalization

Start = 20000
Term = 5
Percent = 15

monthly_capitalization = Start * (1 + ((Percent / 100) / 12)) ** (Term * 12)
print(monthly_capitalization)
 