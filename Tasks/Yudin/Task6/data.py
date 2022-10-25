dodge = {"d1":("d1", "Dodge Caravan 4", "For famaly", "15000"),
        "d2":("d2", "Dodge RAM IV", "Pickup", "25000"),
        "d3":("d3", "Dodge Challenger", "muscle car", "27000")}
cadillac = {"c1":("c1", "Cadillac Escalade 3", "Ofroad", "30000"),
        "c2":("c2", "Cadillac SRX 2", "Ofroad", "22000"),}
bentley = {"b1": ("b1", "Bentley Continental GT 2", "Premium Class", "145000"),
        "b2": ("b2", "Bentley Bentayga", "Premium Class", "120000")}
renault = {"r1": ("r1","Reault Logan 2 ", "For taxi", "8000")}

cart = []

def show_dodge(): 
    return dodge.values()

def show_cadillac(): 
    return cadillac.values()

def show_bentley(): 
    return bentley.values()

def show_renault(): 
    return renault.values()

def add_item(code): 
    if code in dodge.keys():
        res = [', '.join(dodge[code])]
        cart.append(res)
    elif code in cadillac.keys():
        res = [', '.join(cadillac[code])]
        cart.append(res)
    elif code in bentley.keys():
        res = [', '.join(bentley[code])]
        cart.append(res)
    elif code in renault.keys():
        res = [', '.join(renault[code])]
        cart.append(res)
    else:  
        return False

def remove_item(code):
    i=0
    while i <= len(cart):
        for item in cart:
            if cart[i][0].replace(',', '').split()[0] == code:
                del cart[i]
            i+=1
        return True
    return False

def check_cart(): 
    return cart



