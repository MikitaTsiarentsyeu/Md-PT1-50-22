import info

def get_electro():
    res = info.get_electro()    
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def get_computers():
    res = info.get_computers()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])
       

def get_smart_home():
    res = info.get_smart_home()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res]) 

def cart_electro(code):
    res = info.cart_electro(code)
    return res    

def cart_computers(code):
    res = info.cart_computers(code)
    return res    

def cart_sh(code):
    res = info.cart_sh(code)
    return res  

def price_electro(code):
    res = info.price_electro(code)
    return res

def price_computers(code):
    res = info.price_computers(code)
    return res   

def price_sh(code):
    res = info.price_sh(code)
    return res    


