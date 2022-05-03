initial_amount = 20000
time = 5
percent = 15
number_of_months = 5 * 12

total_amount = initial_amount * (1 + (percent / 100 / 12)) ** number_of_months
print(f"Total amount after {time} years of deposit - {round(total_amount, 1)} BYN")