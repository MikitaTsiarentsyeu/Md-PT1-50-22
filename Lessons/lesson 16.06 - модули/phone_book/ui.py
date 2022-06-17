import bl

def show_data(data):
    print(data)

def show_query(message):
    return input(f"{message}:\n")

def add_contact():
    name = show_query("Enter new name")
    phones = show_query("Enter phones separated by ,").split(',')

    res = bl.add_contact(name, *phones)
    show_data(res)

def remove_contact():
    name = show_query("Enter new name")

    res = bl.remove_contact(name)
    show_data(res)

def show_all():
    res = bl.get_all_contacts()
    show_data(res)

def main_flow():

    while True:
        action = input("Choose some action:\n1.add contact\n2.remove contact\n3.show all\n")
        if action == '1':
            add_contact()
        elif action == '2':
            remove_contact()
        elif action == '3':
            show_all()
        elif action == "exit":
            break
