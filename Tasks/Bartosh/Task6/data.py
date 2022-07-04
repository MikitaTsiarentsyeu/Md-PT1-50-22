import json

# My repo has next format:
# ID - number for row,
# Date (0) - date of transaction,	
# Hour (1) - hour of transaction,	
# Place (2) - from which place you spend money or in which place you bring your earn. For example it can be wallet, card, safe and etc,	
# Envelop(3) - the main idea of app is separate money by virtual envelopes and through this get control by money,
# Spent or earned(4) - '+' or '-' count for envelop
# Amount(5) - amount of money which you spent or got on your account
# Envelop balance(6) - amount of money in the envelope after transaction 

#----------------------- reading and storing in json --------------------------------------
def read_repo_from_json():
    with open("repo.json", 'r') as f:
        repo = json.load(f)
    return repo

def store_repo_in_json():
    with open("repo.json", 'w') as f:
        json.dump(repo, f)

def read_places_from_json():
    with open("places.json", 'r') as f:
        places = json.load(f)
    return places

def store_places_in_json():
    with open("places.json", 'w') as f:
        json.dump(places, f)

def read_envelopes_from_json():
    with open("envelopes.json", 'r') as f:
        envelopes = json.load(f)
    return envelopes

def store_envelopes_in_json():
    with open("envelopes.json", 'w') as f:
        json.dump(envelopes, f)

repo = read_repo_from_json()
places = read_places_from_json()
envelopes = read_envelopes_from_json()

#----------------------- places ------------------------------------------------------------
def get_place_balance(name, last_row=None):
    if last_row==0:
        res = f"No balance for {name}"
        return res 
    if not last_row:
        last_row = str(len(repo)) 
    if repo[str(last_row)][2] == name:
        return repo[str(last_row)][6]
    else:
        last_row = int(last_row)-1
        return get_place_balance(name, last_row)

def add_place_name(name):
    places[len(places)+1]=name
    return places

def change_place_name(place, k, last_row=None):
    old_place = places[k]
    if last_row==0:
        places[k]=place
        return 
    if not last_row:
        last_row = str(len(repo))
    if repo[str(last_row)][2] == old_place:
        repo[str(last_row)][2] = place
        return change_place_name (place, k, int(last_row)-1)
    else:
        return change_place_name (place, k, int(last_row)-1)

def delete_place_name(k):
    places.pop(k)
    return (places)

def count_expenses_by_place(name,last_row=None):
    if last_row==0:
        return 0
    if not last_row:
        last_row = str(len(repo))
    if repo[str(last_row)][2]==name and repo[str(last_row)][4]=='-':
        expenses = repo[str(last_row)][5]
        return expenses+count_expenses_by_place(name, int(last_row)-1)
    else:
        return count_expenses_by_place(name, int(last_row)-1)        

def count_income_by_place(name,last_row=None):
    if last_row==0:
        return 0
    if not last_row:
        last_row = str(len(repo))
    if repo[str(last_row)][2]==name and repo[str(last_row)][4]=='+':
        income = repo[str(last_row)][5]
        return income+count_income_by_place(name, int(last_row)-1)
    else:
        return count_income_by_place(name, int(last_row)-1)

def show_places():
    return places

def get_places_len():
    res = len(places)
    return res 

#----------------------- envelopes ------------------------------------------------------------
def count_expenses_by_envelope(name,last_row=None):
    if last_row==0:
        return 0
    if not last_row:
        last_row = str(len(repo))
    if repo[str(last_row)][3]==name and repo[str(last_row)][4]=='-':
        expenses = repo[str(last_row)][5]
        return expenses+count_expenses_by_envelope(name, int(last_row)-1)
    else:
        return count_expenses_by_envelope(name, int(last_row)-1)               

def add_envelopes_limit(k, limit):
    envelopes[k][1]=limit
    return envelopes

def add_envelope_name(name):
    envelopes[len(envelopes)+1]=[name,'None']
    return envelopes

def change_envelope_name(envelope, k, last_row=None):
    old_envelope = envelopes[k][0]
    if last_row==0:
        envelopes[k][0]=envelope
        return 
    if not last_row:
        last_row = str(len(repo))
    if repo[str(last_row)][3] == old_envelope:
        repo[str(last_row)][3] = envelope
        return change_envelope_name (envelope, k, int(last_row)-1)
    else:
        return change_envelope_name (envelope, k, int(last_row)-1)

def delete_envelope_name(k):
    envelopes.pop(k)
    return (envelopes)

def count_income_by_envelope(name,last_row=None):
    if last_row==0:
        return 0
    if not last_row:
        last_row = str(len(repo))
    if repo[str(last_row)][3]==name and repo[str(last_row)][4]=='+':
        income = repo[str(last_row)][5]
        return income+count_income_by_envelope(name, int(last_row)-1)
    else:
        return count_income_by_envelope(name, int(last_row)-1)

def show_envelopes():
    return envelopes

def get_envelopes_len():
    res = len(envelopes)
    return res 


#----------------------- rows ------------------------------------------------------------
def add_row(date, hour, place,envelop, spent_or_earned, amount, balance):
    new_row = [date, hour, place, envelop, spent_or_earned, amount, balance]
    repo[str(len(repo)+1)] = new_row
    res = [str(len(repo))]
    res.append(new_row)
    return res

def get_row(n):
    res = repo[n]
    return res

def get_repo_len():
    res = len(repo)
    return res  