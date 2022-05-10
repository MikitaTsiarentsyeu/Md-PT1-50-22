initial_amount = 20000
duration = 5
months = 12
for i in range(duration*months):
    initial_amount += (initial_amount * 0.15) / months
print(int(initial_amount),"BYN")
 
