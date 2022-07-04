import decimal
repo = {100: ["bread", 2], 101: ["bakery products", 3], 102: ["cookie", 5], #{category: [product, price]}
        200: ["pork", 9.99], 201: ["beaf", 15], 202: ["chicken", 7],
        300: ["hake fish", 15], 301: ["cod", 25], 302: ["shrimps", 35]}

shoping_cart_final = {}
total_price = 0

def get_bakery():
    bakery_repo = {}
    bakery_repo.update([v for k,v in repo.items() if k in range(100,199,1)])
    return bakery_repo.items()       

def get_meat():
    meat_repo = {}
    meat_repo.update([v for k,v in repo.items() if k in range(200,299,1)])
    return meat_repo.items()

def get_fish():
    fish_repo = {}
    fish_repo.update([v for k,v in repo.items() if k in range(300,399,1)])
    return fish_repo.items()   

def add_to_cart(product, quantity):
    for v in repo.values():
        if product == v[0]:
            price = round(decimal.Decimal(quantity*v[1]),2)
            global total_price
            total_price = round(decimal.Decimal(total_price + price),2)
            cost = [v[1], quantity, price]
            shoping_cart= dict.fromkeys([v[0]], cost)
            shoping_cart_final.update(shoping_cart)
            return True
    else:
        return False

def remove_cart(product, quantity):
    for k, v in shoping_cart_final.items():
        if (product == k and quantity == v[1]):
            global total_price
            total_price = round((total_price - decimal.Decimal(quantity*v[0])),2)
            shoping_cart_final.pop(k)
            return True
        elif (product == k and quantity < v[1]):
            price = round(decimal.Decimal(v[2]) - decimal.Decimal(quantity*v[0]),2)
            cost = [v[0], v[1] - quantity, price]
            total_price = round((decimal.Decimal(total_price) - decimal.Decimal(quantity*v[0])),2)
            edit_cart= dict.fromkeys([k], cost)
            shoping_cart_final.update(edit_cart)
            return True
    return False            

def confirm_order():
    global total_price
    total_price = 0
    shoping_cart_final.clear()
    return "Order accepted for work"           

    
        


