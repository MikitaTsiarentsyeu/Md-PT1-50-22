all_goods = {1:'Electronics', 2:'Computers', 3:'Smart Home'}
electro = {101:('HP Photo Printer', '150', 'USD'), 102:('Canon Document Scanner', '300', 'USD'), 
103:('Xerox DocuMate Scanner', '320', 'USD')}
computers = {201:('Lenovo Chromebook S330 Laptop', '450', 'USD'), 202:('Samsung Chromebook Plus V2', '530', 'USD'), 
203:('Acer Chromebook 314', '350', 'USD')}
smart_home = {301:('Blink Video Doorbell', '59', 'USD'), 302:('Honeywell Home Thermostat', '159', 'USD'), 
303:('TP-Link WiFi Router', '68', 'USD')}

def get_all_goods():
    return all_goods.values()

def get_electro():
    return electro.items()

def get_computers():
    return computers.items() 

def get_smart_home():
    return smart_home.items() 

def cart_electro (code):
    for k, v in electro.items():
        if k == code:
           return v[0]     

def cart_computers (code):
    for k, v in computers.items():
        if k == code:
           return v[0]       

def cart_sh (code):
    for k, v in smart_home.items():
        if k == code:
           return v[0]
              
def price_electro (code):
    for k, v in electro.items():
        if k == code:
           return v[1]  

def price_computers (code):
    for k, v in computers.items():
        if k == code:
           return v[1] 

def price_sh (code):
    for k, v in smart_home.items():
        if k == code:
           return v[1]          


    
              