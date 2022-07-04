import moduleBL as BL

def shop():
    a=BL.category()
    [print(f"{i+1} - {a[i]}") for i in range(len(a))]
    while True:
        cat = input('choose category:')
        if cat.isnumeric()!=1 or int(cat)>len(a) or int(cat)==0:
            print('Incorrect input. Try again')
        else:
            break
    cat = a[int(cat)-1]
    return choose_category(cat)

def choose_category(cat):
    a=BL.choose_category(cat)
    [print(f"{i+1} - {a[i]['part']}, part_number:{a[i]['part_number']}, price:{a[i]['price']}") for i in range(len(a))] 
    while True:
        spare_part = input('choose spare part:')
        if spare_part.isnumeric() != 1 or int(spare_part) > len(a) or int(spare_part) == 0: 
            print('Incorrect input. Try again')
        else:
            break    
    part = a[int(spare_part)-1]
    print(part)
    return add_to_cart(part)

def add_to_cart(spare_part):
        cart = BL.cart(spare_part)
        return quantity()

def quantity():
    while True:
        quantity = input('input quantity:')
        if quantity.isnumeric() != 1:
            print('Incorrect input. Try again')
        else:
            break
    a = BL.quantity(int(quantity))
    return quantity_in_order(int(quantity))

def quantity_in_order(quantity):
    a = BL.quantity_in_order(quantity)
    if a == False:
        print(f"Quantity in order more then quantity in stock ({BL.moduleBD.items['cart'][-1]['quantity in stock']}). Would you like to change quantity in order on value equal quantity in stock?\n1 - Yes\n2 - No (Discard order, and return to main menu)\n")
        choose = int(input(''))
        if choose == 1:
            a = BL.change_quantity_order(quantity)
            return order_or_continue()
        else:
            return main_flow()
    if a == True:
        return order_or_continue()

def order():
    while True:
        name = input('Enter your name: ')
        if name.isalpha()!=1:
            print('Incoorect input. Try again')
            continue
        else:
            break
    while True:
        mobile_phone = input('Enter your mobile phone number in format: 44xxxxxxx, 29xxxxxxx, 33xxxxxxx: ')
        if len(mobile_phone)!=9:
            print('Incoorect input. Try again')
            continue
        if mobile_phone.isnumeric()!=1:
            print('Incoorect input. Try again')
            continue
        else:
            break
    a = BL.confirm_order(name, mobile_phone)
    return quantity_in_stock()

def quantity_in_stock():
    a=BL.quantity_in_stock()
    return continue_or_exit()

def continue_or_exit():
    while True:
        choic = int(input('Would you like to back in menu or exit:\n1 - Back in menu\n2 - Exit\n'))   
        if choic == 1:
            return main_flow()
        else:
            return None

def order_or_continue():
    while True:
        c = int(input('Would you like to continue buying or confirm you order:\n1 - Continue buying\n2 - Confirm you order (Cart)\n3 - Bact to main menu\n')) 
        if c == 1:
            return shop()
        elif c == 2:
            return cart()
        elif c == 3:
            return main_flow()

def cart():
    if len(BL.moduleBD.items['cart']) == 0:
        print('Cart is empty')
        main_flow()
    else:
        [print(f"{BL.moduleBD.items['cart'][i]['part']}, price:{BL.moduleBD.items['cart'][i]['price']}, quantity: {BL.moduleBD.items['cart'][i]['quantity to order']}") for i in range(len(BL.moduleBD.items['cart']))]
        a = BL.order()
        print('Total', a)
        while True:
            choice = int(input('Would you like to continue buying or confirm you order:\n1 - Continue buying\n2 - Confirm you order\n3 - Remove items from the cart')) 
            if choice == 1:
                return shop()
            if choice == 2:
                return order()
            if choice == 3:
                return remove_from_cart()
            else:
                print('incorrect input, try again!')

def change_quantity_cart():
    if len(BL.moduleBD.items['cart']) == 0:
        print('Cart is empty')
        return main_flow()
    if len(BL.moduleBD.items['cart']) == 1:
        a = 0
    else:
        [print(f"{i+1} - {BL.moduleBD.items['cart'][i]['part']}, price:{BL.moduleBD.items['cart'][i]['price']}, quantity: {BL.moduleBD.items['cart'][i]['quantity to order']}") for i in range(len(BL.moduleBD.items['cart']))]
        while True:
            a = input('Choose item that should be changed')
            if a.isnumeric() != 1 or int(a)>len(BL.moduleBD.items['cart']):
                print('incorrect input, try again!')
            else:
                break
    a = int(a)
        
    while True:
        q = input('Input quantity: ')
        if  q.isnumeric() != 1:
            print('incorrect input, try again!')
        else:
            break
    quantity = int(q)
    BL.quantity(quantity)
    print(f"Quantity of {BL.moduleBD.items['cart'][a-1]['part']} was changed to {quantity}")
    return quantity_in_order(quantity)


def remove_from_cart():  
    [print(f"{i+1} - {BL.moduleBD.items['cart'][i]['part']}, price:{BL.moduleBD.items['cart'][i]['price']}, quantity: {BL.moduleBD.items['cart'][i]['quantity to order']}") for i in range(len(BL.moduleBD.items['cart']))]
    a = BL.order()
    print('Total', a)
    while True:
        c = input('Do you want clear cart or change quantity of items:\n1 - Delete all items\n2 - Change quantity\n3 - Back to main menu')
        if c.isnumeric() != 1 or int(c)>3 or int(c)<1:
            print('incorrect input, try again!')
        else:
            break
    c = int(c)
    if c == 1:
        BL.moduleBD.items['cart'].clear()
        print('All items from cart was deleted')
        return main_flow()
    if c == 2:
        return change_quantity_cart()
    if c == 3:
        return main_flow()
        
def main_flow():
    while True:
        customer_choice = input("Choose action:\n1 - Buying spare parts for maintanance\n2 - Show cart\n3 - Remove a product from cart\n4 - Exit\n ")
        if customer_choice.isnumeric() != 1 or int(customer_choice)>4 or int(customer_choice)<1:
            print('incorrect input, try again!')
        else: 
            break
    customer_choice = int(customer_choice)
    if customer_choice == 1:
        return shop()
    elif customer_choice == 2:
        return cart()
    elif customer_choice == 3:
        return remove_from_cart()
    elif customer_choice == 4:
        return None