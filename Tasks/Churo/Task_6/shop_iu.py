import shop_bl
import shop_data

def show_data(data):
    print(data)

def show_query(message):
    return input(message)

def show_bakery():
    data = shop_bl.get_bakery_products()
    show_data(data)

def show_meat():
    data = shop_bl.get_meat_products()
    show_data(data)

def show_fish():
    data = shop_bl.get_fish_products()
    show_data(data)          

def ask_for_product():
    return show_query("Enter a product \n")

def ask_for_quantity():
    return show_query("Enter a quantity \n")

def show_shopping_cart():
    data = shop_bl.show_shopping_cart()
    total_price = shop_data.total_price
    print(data)
    print(f"total_price =  {total_price} BYR")

def add_shopping_cart():
     product = ask_for_product()
     quantity = ask_for_quantity()
     res = shop_bl.add_shopping_cart(product, quantity)
     show_data(res)

def remove_cart():
    product = ask_for_product()
    quantity = ask_for_quantity()
    res = shop_bl.remove_cart(product, quantity)
    show_data(res)     

def confirm_order():
    data = shop_bl.show_shopping_cart()
    total_price = shop_data.total_price
    print(data)
    print(f"total_price =  {total_price} BYR")
    confirm = shop_data.confirm_order()
    show_data(confirm) 


def main_flow():
    while True:
        chosed_action = show_query("""Enter the number of your operation:
        0. Exit
        1. Show bakery products
        2. Show meat products
        3. Show fish products
        4. Add to shopping cart
        5. Show shopping cart
        6. Confirm the order
        7. Remove from shoping cart
        """)
        if chosed_action == '0':
            break
        elif chosed_action == '1':
            show_bakery()
        elif chosed_action == '2':
            show_meat()
        elif chosed_action == '3':
            show_fish()        
        elif chosed_action == '4':
            add_shopping_cart()
        elif chosed_action == '5':
            show_shopping_cart() 
        elif chosed_action == '6':
            confirm_order()
        elif chosed_action == '7':
            remove_cart()                   
       