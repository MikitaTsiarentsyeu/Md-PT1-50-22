import Business_logic as bl

def get_snowboards():
    res = bl.get_snowboards()
    print(res)

def get_ski():
    res = bl.get_ski()
    print(res)

def get_skates():
    res = bl.get_skates()
    print(res)

def cart_snowboards():
    code = int(input('Enter a product code:\n'))
    res = bl.cart_snawboards(code)
    res_add = bl.price_snawboards(code)
    return cart_full(res, int(res_add))

def cart_ski():
    code = int(input('Enter a product code:\n'))
    res = bl.cart_ski(code)
    res_add = bl.price_ski(code)
    return cart_full(res, int(res_add))

def cart_skates():
    code = int(input('Enter a product code\n'))
    res = bl.cart_skates(code)
    res_add = bl.price_skates(code)
    return cart_full (res, int(res_add))

cart=[]
item_common = []
def cart_full(res, res_add):
    cart.append(res)
    item_common.append(res_add)
    print(f"Your choice is:\n{', '.join(map(str,cart))}")
    des = input("Enter 1 to continue cart filling or 2 to checkout:\n")
    if des == '2':
        final_order = (', '.join(map(str,cart)))
        print (f"Your order is:\n{final_order}")
        final_sum = sum (item_common)
        print (f'The total price is: {final_sum} USD')

        input ('Your order is confirmed. Thank you!\nPress enter to continue')

def main_flow():
    while True:
        section = input('Choose category:\n1.Snowboards\n2.Ski\n3.Skates\n')
        if section == '1':
            get_snowboards()
            cart_snowboards()
        elif section == '2':
            get_ski()
            cart_ski()
        elif section == '3':
            get_skates()
            cart_skates()
        else:
            break