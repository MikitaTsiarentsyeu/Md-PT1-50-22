import car_data

def f_data(res):
    return car_data.header + '\n'.join([f"{c[0]}: {',   '.join(c[1])}" for c in res])

def get_all_cars():
    res = car_data.get_all_cars()
    return f_data(res)

def get_car_select(param):
    res = car_data.get_car_sel(param)
    return f_data(res)

def check_choice(num):
    num = int(num)
    return car_data.check_in_catalog(num)

def add_to_cart(num):
    num = int(num)
    if car_data.add_to_cart(num) == True:
        return f"Addedd to cart: {num}"
    else: return f"Car alredy in cart"
    

def show_cart():
    res = car_data.show_cart()
    if  res.isdisjoint(car_data.get_all_cars()) == True:
        return False
    else: return f_data(res)

def remove_from_cart(num):  #in progress
    num = int(num)
    print(f"remove  {num}")

def new_oder():
    print("This fuction make oder")



# f = show_cart()
# print(f)
