import json
mark = "Mercedes-Benz"
clas = ['A', 'B', 'C', 'E', 'S', 'GLC', 'GLE', 'GLS', 'G'] 
body = ["Sedan", "Saloon", "Pickup", "2/3 doors"]        
fuel = ["Diesel", "Petrol", "Electro"]                           
getribe = ["Automatic", "Manual"]                              
drive = ["RWD", "AWD", "FWD"]
header = "    Mark         Class  Boby type   Fuel  Getribe   Drive\n"
cart = []                                  
oder= {}

car =  {
        0: (mark, clas[0], body[3], fuel[2], getribe[0], drive[2]),
        1: (mark, clas[1], body[0], fuel[0], getribe[1], drive[2]),
        2: (mark, clas[2], body[0], fuel[0], getribe[0], drive[0]),
        3: (mark, clas[3], body[0], fuel[0], getribe[0], drive[0]),
        4: (mark, clas[4], body[0], fuel[0], getribe[0], drive[0]),
        6: (mark, clas[6], body[0], fuel[1], getribe[0], drive[1]),
        7: (mark, clas[7], body[2], fuel[1], getribe[0], drive[1]),
        8: (mark, clas[8], body[2], fuel[0], getribe[0], drive[1]),
        9: (mark, clas[8], body[2], fuel[1], getribe[0], drive[1]),
        
        }


def get_car_sel(param):
    return {key: val for key, val in car.items() if param in val}.items()

def get_all_cars():
    return car.items()

def check_in_catalog(num):
    if num in car.keys():
        return True
    else: return False

def add_to_cart(num):
    try:    
        if num not in cart:
            cart.append(num)
            return True
    except: return False


def show_cart():
    return {key: val for key, val in car.items() if key in cart}.items()

def remove_from_cart(num):
    if num in cart:
        cart.remove(num)

# cart.append(1)  
# cart.append(2) 
  

def create_oder():
    res = {key: val for key, val in car.items() if key in cart}
    with open ("oder.json", 'w') as f:
        json.dump(res, f)
    global cart
    cart = []
    return True
    
   

# print(create_oder())
# print(cart)




