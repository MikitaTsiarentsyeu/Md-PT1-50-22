#variant1

deposit = 20000
period = 60
rate = 15/12/100
x = deposit*(rate + 1)**period
print(x)

#variant2

deposit = 20000
period = 1
rate = 15/12/100
for period in range(60):
    deposit = deposit*(rate+1)
print(deposit)
    
