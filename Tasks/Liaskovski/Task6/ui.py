import bl

def show_data(data):
    print(data)

def show_query(message):
    return input(f"{message}:\n")



def remove_item():
    name = show_query("Enter product id to remove from your cart:")
    res = bl.remove_item(name)  
    show_data(res)  
    print("the item was removed")
    
def show_all():                        #to see the entire catalog
    res = bl.get_all_items()
    return res

def add_my_basket():
    
    res = bl.add_my_basket()
    # show_data(res)
    # print("the item was added")


def show_all_in_basket():                            #items in my cart
    res = bl.get_all_items_in_basket()
    show_data(res)



def main_flow():

    while True:
        action = input("Choose some action:\n1.Add item to my shopping cart\n2.Remove item from my cart\n3.Show the entire catalog\n4.My shopping cart\n5.Exit\n")
        if not action.isdigit():
            print("Incorrect symbols")
            continue
        
        if len(action) !=1:
            print("Incorrect input")
            continue
        
        if action == '1':
            add_my_basket()
        elif action == '2':
            remove_item()
        elif action == '3':
            show_all()
        elif action == '4':
            show_all_in_basket()
        
        elif action == '5':
            break
        elif action not in range(1,6):
            print("Incorrect numbers")
            continue
        

