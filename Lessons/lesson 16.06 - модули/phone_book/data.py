repo = {1: ("name", ["1234567", "7654321"])}

def get_all_contacts():
    return repo.values()

def add_contact(name, *phones):
    try:
        new_contact = (name, list(phones))
        for i in range(1, len(repo)+2):
            if i not in repo:
                repo[i] = new_contact
        return True
    except:
        return False

def add_phone(name, phone): pass

def remove_contact(name):
    for k, v in repo.items():
        if v[0] == name:
            del repo[k]
            return True
    return False

def remove_phone(name, phone): pass

def search(name): pass

