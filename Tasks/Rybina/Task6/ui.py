import bl

def show_data(data): 
    print(data)

def show_categories():
    action = input("Choose a category of pet food (enter a number of category):\n1. Dog\n2. Cat\n3. Bird\n4. Rodent\n")
    if action == '1':
        show_dog()
    elif action == '2':
        show_cat()
    elif action == '3':
        show_bird()
    elif action == '4':
        show_rodent()
    else:
        print("Incorrect input. Try again")
        show_categories()
    choose_action()

def show_dog(): 
    res = bl.show_dog()
    show_data(res)

def show_cat(): 
    res = bl.show_cat()
    show_data(res)

def show_bird(): 
    res = bl.show_bird()
    show_data(res)

def show_rodent(): 
    res = bl.show_rodent()
    show_data(res)

def choose_action():
    action = (input("\nIf you want to order goods from chosen category, enter 1.\nIf you want to check items in the cart, enter 2.\nIf you want to go back to menu, enter 3.\n"))
    if action == '1':
        add_item()
    if action == '2':
        check_cart()
    elif action == '3':
        show_categories()
    else:
        print("Incorrect input. Try again")
        choose_action()

def add_item(): 
    code = input("To add item to the cart enter the code of product\n")
    res = bl.add_item(code)
    choose_action()

def check_cart(): 
    res = bl.check_cart()
    if res == []:
        print("The cart is empty\n")
        show_categories()
    else:
        print("Items in the cart: ")
        show_data(res)
        order_sum()
        action = input("\nIf you want to order these items, enter 1.\nIf you want to remove item, enter 2.\nIf you want to go back to main menu, enter 3.\n")
        if action == '1':
            make_order()
        elif action == '2':
            remove_item()
        elif action == '3':
            show_categories()
        else:
            print("Incorrect input. Try again")
            check_cart()
        
def order_sum():
    res = bl.order_sum()
    print(f"Total sum is {res} USD")

def remove_item(): 
    code = input("To remove item from the cart enter the code of product\n")
    res = bl.remove_item(code)
    check_cart()
    

def make_order():
    print("Items in the order: ")
    res = bl.check_cart()
    show_data(res)
    order_sum()
    action = input("\nTo confirm the order enter 1.\nTo check cart enter 2.\nTo go back to main menu enter 3.\n")
    if action == '1':
        print("Your order is confirmed. Thank you!")
    elif action == '2':
        check_cart()
    elif action == '3':
        show_categories()
    else:
        print("Incorrect input. Try again")
        make_order()

def main_flow():
    print("Welcome to our shop.")
    show_categories()

main_flow()