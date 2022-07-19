import moduleBD
    
def category():
    list_cat = []
    for i in range(len(moduleBD.items['parts'])):
        list_cat.append((moduleBD.items['parts'][i]['catrgory']))
    list_cat = set(list_cat)
    list_cat = list(list_cat)
    list_cat.sort()
    return list_cat

def choose_category(cat):
    list_sp = []
    for i in range(len(moduleBD.items['parts'])):
        if cat == moduleBD.items['parts'][i]['catrgory']:
            list_sp.append(moduleBD.items['parts'][i])
    return list_sp

def cart(part):
    moduleBD.items['cart'].append(part)
    return moduleBD.items
    
    
def quantity(quantity):    
    moduleBD.items['cart'][-1]['quantity to order'] = quantity
    print('cart', moduleBD.items['cart'])
    

def quantity_in_order(quantity):
    if quantity>int(moduleBD.items['cart'][-1]['quantity in stock']) and int(moduleBD.items['cart'][-1]['quantity in stock'])!=0:
        return False
    else:
        return True  

def change_quantity_order(quantity):
    moduleBD.items['cart'][-1]['quantity to order'] = moduleBD.items['cart'][-1]['quantity in stock']
    return moduleBD.items

def order():
    total = 0
    for i in range(len(moduleBD.items['cart'])):
        total += int(moduleBD.items['cart'][i]['quantity to order'])*int(moduleBD.items['cart'][i]['price'])
    return total

def confirm_order(name, mobile_phone):
    moduleBD.items['order'].append([name, mobile_phone, moduleBD.items['cart']])
    print(moduleBD.items['order'])
    return moduleBD.items

def quantity_in_stock():
    for i in range (len(moduleBD.items['parts'])):
        for j in range (len(moduleBD.items['cart'])):
            if moduleBD.items['parts'][i]['part'] == moduleBD.items['cart'][j]['part'] and moduleBD.items['parts'][i]['quantity in stock']!=0:
                moduleBD.items['parts'][i]['quantity in stock'] = int(moduleBD.items['parts'][i]['quantity in stock']) - int(moduleBD.items['cart'][j]['quantity to order']) 
    moduleBD.items['cart'].clear()
    return moduleBD.items