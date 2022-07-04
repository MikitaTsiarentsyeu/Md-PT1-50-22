import shop_data


def get_bakery_products():
    bakery = shop_data.get_bakery()
    return str("\n" .join([f"{c[0]} cost = {c[1]} BYR " for c in bakery]))

def get_meat_products():
    meat = shop_data.get_meat()
    return str("\n" .join([f"{c[0]} cost = {c[1]} BYR " for c in meat]))

def get_fish_products():
    fish = shop_data.get_fish()
    return str("\n" .join([f"{c[0]} cost = {c[1]} BYR " for c in fish]))    

def show_shopping_cart():
    cart = shop_data.shoping_cart_final.items()       
    return str("\n" .join([f"{c[0]} cost = {c[1][0]} BYR: quantity = {c[1][1]}: in total = {c[1][2]} BYR " for c in cart]))
        

def add_shopping_cart(product, quantity):
    try:
        validation_quantity(quantity)
    except ValueError:
        return "Wrong type for quantity, please enter a number"
    if  product in shop_data.shoping_cart_final.keys():
        return str("\n" .join([f"{product} is alredy in cart, please change the quantity via remove, item ""7"" "]))             
    res = shop_data.add_to_cart(product, int(quantity))   
    if res:
        return "Success! Product is adding to cart"
    else: 
        return "This product is not in the shop"

def remove_cart(product, quantity):
    try:
        validation_quantity(quantity)
    except ValueError:
        return "Wrong type for quantity, please enter a number"
    res = shop_data.remove_cart(product, int(quantity))
    if res:
        return "Success! Product is removing from cart"
    else: 
        return "This product is not in the cart or quantity does not match"

def validation_quantity(quantity):
    if quantity.isdigit() :
        return True
    raise ValueError     

    

    


