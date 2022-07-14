import bl

def show_data(data):
    print(data)

def show_query(message):
    return input(f"{message}:\n")

def get_category_list():
    res = bl.get_category_list()
    show_data(res)

def search_by_category():
    result = show_query("Enter category")
    res = bl.search_by_category(result)
    show_data(res)

def add_to_cart():
    res = show_query('Enter item id and number of items separated by comma')
    bl.add_to_cart(res)
    show_data('item is in cart')

def go_to_cart():
    res = bl.go_to_cart()
    show_data(res)
    show_data(bl.set_delivery_address(show_query('Enter delivery address and tel number')))
    show_data('We will call you soon')

def main_flow():

    while True:
        action = input('Choose some action:\n1.show all categories\n2.search by category\n3.add to the cart by id\n4.go to the cart\n')
        if action == '1':
            get_category_list()
        elif action == '2':
            search_by_category()
        elif action == '3':
            add_to_cart()
        elif action == '4':
            go_to_cart()
        elif action == 'exit':
            break