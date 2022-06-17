import data

def get_all_contacts():
    res = data.get_all_contacts()
    return '\n'.join([f"{c[0]}: {','.join(c[1])}" for c in res])

def add_contact(name, *phones):
    res = data.add_contact(name, *phones)
    return format_response(res, "The contact was added")

def remove_contact(name):
    res = data.remove_contact(name)
    return format_response(res, "The contact was removed")

def format_response(res, message):
    if res:
        contacts = get_all_contacts()
        return f"{message}:\n{contacts}"
    else:
        return "Something went wrong"