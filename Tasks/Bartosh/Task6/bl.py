import data
#----------------------- storing --------------------------------------
def store_repo():
    data.store_repo_in_json()

def store_places():
    data.store_places_in_json()

def store_envelopes():
    data.store_envelopes_in_json()


#----------------------- places --------------------------------------
def get_places_balance():
    res = '\n'.join([f"{i}. {data.places[i]} - {data.get_place_balance(data.places[i])}" for i in data.places])
    return res    

def add_place(name):
    data.add_place_name(name)
    res = '\n'.join([f"{i} - {data.places[i]}" for i in data.places])
    return res

def change_place_name(place, k):
    data.change_place_name(place,k)
    res = get_places_balance()
    return res

def delete_place_name(k):
    res = data.delete_place_name(k)
    return '\n'.join([f"{i} - {res[i]}" for i in res])

def get_places_expenses():
    res = '\n'.join([f"{i}. {data.places[i]} - {data.count_expenses_by_place(data.places[i])}" for i in data.places])
    return res    

def get_places_income():
    res = '\n'.join([f"{i}. {data.places[i]} - {data.count_income_by_place(data.places[i])}" for i in data.places])
    return res 

def show_places():
    res = data.show_places()
    return res

def get_places_len():
    res = data.get_places_len()
    return res 

#----------------------- envelopes --------------------------------------
def get_expenses_by_envelopes():
    res = '\n'.join([f"{i}. {data.envelopes[i][0]} ({data.envelopes[i][1]}) - {data.count_expenses_by_envelope(data.envelopes[i][0])}" for i in data.envelopes])
    return res

def add_envelopes_limit(k, limit):
    data.add_envelopes_limit(k, limit)
    res = '\n'.join([f"{i}. {data.envelopes[i][0]} ({data.envelopes[i][1]})"for i in data.envelopes])
    return res

def add_envelope_name(name):
    data.add_envelope_name(name)
    res = '\n'.join([f"{i}. {data.envelopes[i][0]} ({data.envelopes[i][1]}) - {data.count_expenses_by_envelope(data.envelopes[i][0])}" for i in data.envelopes])
    return res

def change_envelope_name(envelope,k):
    data.change_envelope_name(envelope,k)
    res = get_expenses_by_envelopes()
    return res

def delete_envelope_name(k):
    res = data.delete_envelope_name(k)
    return '\n'.join([f"{i}. {res[i][0]} ({res[i][1]})"for i in res])

def get_income_by_envelopes():
    res = '\n'.join([f"{i}. {data.envelopes[i][0]} ({data.envelopes[i][1]}) - {data.count_income_by_envelope(data.envelopes[i][0])}" for i in data.envelopes])
    return res

def show_envelopes():
    res = data.show_envelopes()
    return res

def get_envelopes_len():
    res = data.get_envelopes_len()
    return res 


#----------------------- rows --------------------------------------
def add_row(date, hour, place, envelop, spent_or_earned, amount):
    if spent_or_earned == '+':
        balance = data.get_place_balance(place)+int(amount)
    else:
         balance = data.get_place_balance(place)-int(amount)
    res = data.add_row(date, hour, place,envelop, spent_or_earned, amount, balance)

    res = f"{res[0]}. {res[1][0]} in {res[1][1]} hours you {'spent' if res[1][4]== '-' else 'earned'} {res[1][5]} {'from' if res[1][4]== '-' else 'in'} {res[1][2]} {'from' if res[1][4]== '-' else 'in'} {res[1][3][0]}. Now in {res[1][2]} {res[1][6]} "
    return res 

def get_row (n):
    res = data.get_row (n)
    res = f"{n}. {res[0]} in {res[1]} hours you {'spent' if res[4]== '-' else 'earned'} {res[5]} {'from' if res[4]== '-' else 'in'} {res[2]} {'from' if res[4]== '-' else 'in'} {res[3]} envelope. In {res[2]} was {res[6]}"
    return res 

def get_repo_len():
    res = data.get_repo_len()
    return res
#print(get_row('5'))