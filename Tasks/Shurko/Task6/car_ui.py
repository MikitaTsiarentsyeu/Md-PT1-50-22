import car_bl

cart_not_empty = False

def print_all():
    print(car_bl.get_all_cars())

def print_sel(param):
    print(car_bl.get_car_select(param))

def check_choice(num):
    return car_bl.check_choice(num)

def add_to_cart(num):
    print(car_bl.add_to_cart(num))

def in_cart(): # in progress
    while True:
        action = input("To make oder tap O OR number for remove OR any key to continue ")
        if action == 'O':
            car_bl.new_oder()
            break
        elif action.isdigit() == True:              #in progress
                car_bl.remove_from_cart(action) 
        else: break

def show_cart():
    if car_bl.show_cart() == False:
        print("cart is empty")
    else: print(car_bl.show_cart()), in_cart()

def main_flow():
    while True:
            print("\nA: Will show all car in store; exit: to exit; cart to see cart")
            print("Select fuel: D for diesel, P for petrol, E for electro OR Select getribe: A for automatic or M for manual")
            action = input("Numbers for selection in the catalog \n")
            if action.isdigit() == True:
                if check_choice(action) == True:
                    add_to_cart(action)
                else: print("Sorry no car in catalog")
            else:
                if action == 'A':
                    print_all()
                elif action == 'D':
                    print_sel("Diesel")
                elif action == 'P':
                    print_sel("Petrol")
                elif action == 'E':
                    print_sel("Electro")
                elif action == 'A':
                    print_sel("Automatic")
                elif action == 'M':
                    print_sel("Manual")
                elif action == "cart":
                    show_cart()    
                elif action == "exit":
                    break