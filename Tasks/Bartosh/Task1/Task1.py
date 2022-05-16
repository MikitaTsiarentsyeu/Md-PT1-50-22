from decimal import Decimal

def get_non_negative_value(param):
    if param < 0:
        print("Please, write down positive number")
        return True
    else: 
        return False

def get_non_negative_decimal(prompt):
    while True:
        try:
            value = Decimal(input(prompt))
        except ValueError:
            print("Please, write down number")
            continue
        if get_non_negative_value(value):
            continue
        else:
            break
    return value

def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please, write down integer number")
            continue
        if get_non_negative_value(value):
            continue
        else:
            break
    return value

print('Hello, let me calculate how much money you will have in your account at the end of the deposit. For the calculation, I need some data from you.')

initial_deposit = get_non_negative_decimal ('1. How much money will you put into the account at the beginning?\nwrite down numbers and press enter, please:')

initial_deposit = initial_deposit.quantize(Decimal("1.00"))

print("I understand",initial_deposit,"BYN")

years = get_non_negative_int ('2. what is the term of the deposit in years?\nwrite down numbers of years and press enter, please:')

print(years, "years, I see")

interest = get_non_negative_decimal ('3. What interest did they promise you?\nwrite down numbers of interest and press enter, please:')

interest = interest.quantize(Decimal("1.00"))

print (interest, "%, \nlet me calculate how much money you will have in your account at the end of the deposit")

total_amount_row = initial_deposit*((1+((interest/100)/12))**(years*12))
total_amount = total_amount_row.quantize(Decimal("1.00"))

print (total_amount, "BYN, total amount on the account with monthly capitalization")

input ('fine?')