import bl
from decimal import Decimal

def show_query(message):
    return input(f"{message}:\n")

def show_data(data):
    print(data)


#------------------------- places -------------------------
def get_places_balance():
    res = bl.get_places_balance()
    show_data(res)

def add_place():
    place = show_query("Enter the new place")
    res = bl.add_place(place)
    show_data(res)

def edit_place_name():
    get_places_balance()
    k = place_number_input('press number which place do you want to change:\n')
    place = input("press new name for place\n")
    bl.change_place_name(place, k)
    get_places_balance()

def delete_place_name():
    get_places_balance()
    k = place_number_input('press number which place do you want to delete:\n')
    res = bl.delete_place_name(k)
    print ('Only the following places are left on the list:')
    show_data(res)

def get_places_expenses():
    res = bl.get_places_expenses
    show_data(res) 

def get_places_income():  
    res = bl.get_places_income
    show_data(res)


#------------------------- envelopes -------------------------
def get_expenses_by_envelopes():
    res = bl.get_expenses_by_envelopes()
    show_data(res)

def add_envelopes_limit(): 
    get_expenses_by_envelopes()
    k = envelope_number_input('enter the number of the envelope for which you want to change the limit:\n') 
    limit = get_non_negative_int('enter the new limit:\n')  
    res = bl.add_envelopes_limit(k,limit)  
    show_data(res)

def add_envelop_name():
    envelop = show_query("Enter the new envelopes name:\n")
    res = bl.add_envelop_name(envelop)
    show_data(res)

def edit_envelope_name():
    get_expenses_by_envelopes()
    k = envelope_number_input('enter the number of the envelope for which you want to change the name:\n')
    envelope = input('press new name for envelope:\n')
    bl.change_envelope_name(envelope, k)
    get_expenses_by_envelopes()

def delete_envelope_name():
    get_expenses_by_envelopes()
    k = envelope_number_input('press the number of the envelope which you want to delete:\n')
    res = bl.delete_envelope_name(k)
    print ('Only the following envelopes are left on the list:')
    show_data(res)

def get_income_by_envelopes():
    res = bl.get_income_by_envelopes
    show_data(res)


#------------------------- rows -------------------------

#validation and inputs
def get_plus_or_minus():
    while True:
        val = input("did you earned or spent? + or -:\n")
        if val not in ('+', '-'):
            print("Please choose only + or -")
        else:
            break
    return val

def get_non_negative_value(value):
    if value < 0:
        print("Please, write down positive number")
        return True
    else: 
        return False

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

def check_range(n, min, max):
    if n < min or n > max:
        print (f"Please, enter number beetwin {min} and {max}")
        return True
    else:
        return False

def hour_input():
    while True:
        try:
            value = int(input("Enter the hour:\n"))
        except ValueError:
            print("Please, write down integer number:\n")
            continue
        if get_non_negative_value(value):
            continue
        if check_range(value, 0, 23):
            continue
        else:
            break
    return value

def place_number_input(text):
    while True:
        try:
            place = int(input(text))
        except ValueError:
            print("Please, write down integer number:\n")
            continue
        if get_non_negative_value(place):
            continue
        max = bl.get_places_len()
        if check_range(place, 1, max):
            continue
        else:
            break
    return place

def choose_place():
    get_places_balance()
    d = bl.show_places()
    val = place_number_input("enter number of the place from which did you spent money or earned it:\n")
    place = d[val]
    return place

def envelope_number_input(text):
    while True:
        try:
            place = int(input(text))
        except ValueError:
            print("Please, write down integer number:\n")
            continue
        if get_non_negative_value(place):
            continue
        max = bl.get_envelopes_len()
        if check_range(place, 1, max):
            continue
        else:
            break
    return place

def choose_envelopes():
    get_expenses_by_envelopes()
    d = bl.show_envelopes()
    val = envelope_number_input('enter number of the envelopes from which did you spent money or earned it:\n')
    envelopes = d[val]
    return envelopes

def get_non_negative_decimal(text):
    while True:
        try:
            value = Decimal(input(text))
        except ValueError:
            print("Please, write down number")
            continue
        if get_non_negative_value(value):
            continue
        else:
            break
    value = value.quantize(Decimal("1.00"))
    return value

def date_input():
    date = input ('enter the date when you earned or spent money in dd.mm.yyyy format:\n')
    while True:
    #find length
        date_len = len(date) 
        if ('.' in date) ==True and date_len == 10 and int(date.split('.')[0])>=1 and int(date.split('.')[0])<=31 and int(date.split('.')[1])>=1 and int(date.split('.')[1])<=12: 
            break
        #no .
        elif ('.' in date) == False:
            date = input('Your time should content sigh ".". Please enter the date in dd.mm.yyyy format:\n')
        # wrong lenght of string
        elif date_len != 10:
            date = input('Enter 10 signs including ".". Please enter the date in dd.mm.yyyy format:\n')
        # wrong hours
        elif int(date.split('.')[0])<1 or int(date.split('.')[0])>31:    
            date = input('Days should be between 1 and 31. Please enter date again:')
        elif int(date.split('.')[1])<1 or int(date.split('.')[1])>12:    
            date = input('Month should be between 1 and 12. Please enter date again:') 
    return date

def add_row():
    date = date_input()
    hour = hour_input()
    place = choose_place()
    envelop = choose_envelopes() 
    spent_or_earned = get_plus_or_minus() 
    amount = get_non_negative_decimal('enter the amount of money:\n')
    res = bl.add_row(date, hour, place, envelop, spent_or_earned, amount)
    show_data(res)


def row_number_input(text):
    while True:
        try:
            row = int(input(text))
        except ValueError:
            print("Please, write down integer number:\n")
            continue
        if get_non_negative_value(row):
            continue
        max = bl.get_repo_len
        if check_range(row, 1, max):
            continue
        else:
            break
    return row

def show_row():
    n = row_number_input('enter the number of row:\n')
    res = bl.get_row(n)
    show_data(res)


#------------------------- menu -------------------------
def main_flow():
    while True:
        action = input("\nHello! What do you want to do with your money?\nEnter the number if you want:\n1. add spending or income\n2. do something with places\n3. do something with envelopes\n4. watch the summary\n0. quit the program\n")
        if action == '1':
            action_lvl_1 = input("press: \n1. add spending or income:\n2. see the row by number:\n")
            if action_lvl_1 == '1':
                add_row()
            elif action_lvl_1 == '2':
                show_row()    
        #places actions
        elif action == '2':
            action_lvl_2 = input("press: \n1. see the places balance\n2. add the place\n3. change the places name\n4. remove the place\n")
            if action_lvl_2 == '1':
                get_places_balance()
            elif action_lvl_2 == '2': 
                add_place()    
            elif action_lvl_2 == '3': 
                edit_place_name()
            elif action_lvl_2 == '4':  
                delete_place_name()   
        #envelopes actions                
        elif action == '3':
            action_lvl_3 = input("press: \n1. see expenses from envelopes\n2. add the limit to the envelop\n3. add the envelop\n4. change the envelop name\n5. remove the envelop\n")
            if action_lvl_3 == '1':
                get_expenses_by_envelopes()
            elif action_lvl_3 == '2': 
               add_envelopes_limit()    
            elif action_lvl_3 == '3': 
                add_envelop_name() 
            elif action_lvl_3 == '4':  
                edit_envelope_name()          
            elif action_lvl_3 == '5':  
                delete_envelope_name()
        elif action == '4':
            action_lvl_4 = input("press: \n1. see expenses by places\n2. see income by places\n3. see expenses by envelopes\n4. see income by envelopes\n")
            if action_lvl_4 == '1':
                get_places_expenses()
            elif action_lvl_4 == '2': 
                get_places_income
            elif action_lvl_4 == '3': 
                get_expenses_by_envelopes
            elif action_lvl_4 == '4': 
                get_income_by_envelopes
        elif action == "0":
            bl.store_repo()
            bl.store_places()
            bl.store_envelopes()
            break

