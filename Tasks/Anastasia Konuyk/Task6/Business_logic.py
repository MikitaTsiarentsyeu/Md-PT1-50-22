import Database as db

def get_snowboards():
    res = db.get_snowboards()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def get_ski():
    res = db.get_ski()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def get_skates():
    res = db.get_skates()
    return '\n'.join([f"{c[0]}: {', '.join(c[1])}" for c in res])

def cart_snawboards(code):
    res = db.cart_snowboards(code)
    return res

def cart_ski(code):
    res = db.cart_ski(code)
    return res

def cart_skates(code):
    res = db.cart_skates(code)
    return res

def price_snawboards(code):
    res = db.price_snowboards(code)
    return res

def price_ski(code):
    res = db.price_ski(code)
    return res

def price_skates(code):
    res = db.price_skates(code)
    return res