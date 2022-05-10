initial_amount = 20000
term = 5
percent = 15
total_amount = initial_amount * (1 + ((percent / 100) / 12)) ** (term * 12)
print("Total amount after 5 years", round(total_amount, 2), "BYN")
