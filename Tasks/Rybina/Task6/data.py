dogs = {"d1":("d1", "Pedigree", "For puppies", "15"),
        "d2":("d2", "Hill's", "Perfomance", "25"),
        "d3":("d3", "Hill's", "Adult", "22")}
cats = {"c1":("c1", "Purina Pro Plan", "Original Kitten", "30"),
        "c2":("c2", "Purina Pro Plan", "Sterilised Adult", "35"),}
birds = {"b1": ("b1", "RIO", "For parrots", "2"),
        "b2": ("b2", "Versele-Laga", "For canaries", "7")}
rodents = {"r1": ("r1","Versele-Laga", "For mices", "8")}

cart = []

def show_dog(): 
    return dogs.values()

def show_cat(): 
    return cats.values()

def show_bird(): 
    return birds.values()

def show_rodent(): 
    return rodents.values()

def add_item(code): 
    if code in dogs.keys():
        res = [', '.join(dogs[code])]
        cart.append(res)
    elif code in cats.keys():
        res = [', '.join(cats[code])]
        cart.append(res)
    elif code in birds.keys():
        res = [', '.join(birds[code])]
        cart.append(res)
    elif code in rodents.keys():
        res = [', '.join(rodents[code])]
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



