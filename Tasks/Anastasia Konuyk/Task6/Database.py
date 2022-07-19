category = {1:'Snowboards', 2:'Ski', 3:'Skates'}

snowboards = {101:('CAPITA Mercury', '600', 'USD'),
              102:('Nitro Ripper', '400', 'USD'),
              103:('Salomon Assassin', '540', 'USD')}
ski = {201:('Nordica Santa', '440', 'USD'),
       202:('Blizzard Rustler', '580', 'USD'),
       203:('Armada Bantam', '630', 'USD')}
skates = {301:('Jackson', '70', 'USD'),
          302:('Riedell', '65', 'USD'),
          303:('Lake Placid', '50', 'USD')}

def get_category():
    return category.values()

def get_snowboards():
    return snowboards.items()

def get_ski():
    return ski.items()

def get_skates():
    return skates.items()

def cart_snowboards(code):
    for k, v in snowboards.items():
        if k == code:
           return v[0]

def cart_ski(code):
    for k, v in ski.items():
        if k == code:
           return v[0]

def cart_skates(code):
    for k, v in skates.items():
        if k == code:
           return v[0]

def price_snowboards(code):
    for k, v in snowboards.items():
        if k == code:
           return v[1]

def price_ski(code):
    for k, v in ski.items():
        if k == code:
           return v[1]

def price_skates(code):
    for k, v in skates.items():
        if k == code:
           return v[1]