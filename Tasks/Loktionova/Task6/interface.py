import logic

def get_electro():
    res = logic.get_electro()
    print(res)    

def get_computers():
    res = logic.get_computers()
    print(res)    

def get_smart_home():
    res = logic.get_smart_home()
    print(res)    

def cart_electro():
    code = int(input('Please enter a product code to checkout:\n'))
    res = logic.cart_electro(code)
    res1 = logic.price_electro(code)
    return cart_filling (res, int(res1))

def cart_computers():
    code = int(input('Please enter a product code to checkout:\n'))
    res = logic.cart_computers(code)
    res1 = logic.price_computers(code)
    return cart_filling (res, int(res1))

def cart_sh():          
    code = int(input('Please enter a product code to checkout:\n'))
    res = logic.cart_sh(code)
    res1 = logic.price_sh(code)
    return cart_filling (res, int(res1))   

cart=[]
item_sum = []
def cart_filling(res, res1): 
    cart.append(res)
    item_sum.append(res1) 
    print(f"Your choice is:\n{', '.join(map(str,cart))}")
    des = input("Enter 1 to continue cart filling or 2 to checkout:\n")
    if des == '2':
        final_cart = (', '.join(map(str,cart)))
        print (f"Your order is:\n{final_cart}")
        final_sum = sum (item_sum)
        print (f'The final sum is: {final_sum} USD')
            
        input ('Thank you.\nPress enter to continue')  
    
def main_flow(): 
    while True:
        section = input('Choose category:\n1.Electronics\n2.Computers\n3.Smart home\n')
        if section == '1':
            get_electro()
            cart_electro()
        elif section == '2':
            get_computers()
            cart_computers()
        elif section == '3':
            get_smart_home()
            cart_sh()
        elif section == "exit":
            break