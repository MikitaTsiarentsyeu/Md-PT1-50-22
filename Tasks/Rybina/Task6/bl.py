import data

def show_dog():
    res = data.show_dog()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def show_cat():
    res = data.show_cat()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def show_bird():
    res = data.show_bird()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def show_rodent():
    res = data.show_rodent()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def add_item(code):
    res = data.add_item(code)
    if res == False:
        print("No item found.\n")
    else:
        print("The item was added to the cart.")
        return res

def remove_item(code): 
    res = data.remove_item(code)
    if res == True:
        print("The item was removed\n")
        return data.check_cart()      
    else:
        print("There's no such item in the cart")
        
def check_cart():
    res = data.check_cart()
    if res == []:
        return []
    else:
        return ' USD\n'.join(', '.join(sub_list) for sub_list in res)+' USD'

def order_sum():
    res = data.check_cart()
    i = 0
    l_sub = [0]
    while i < len(res):
        for x in res:
            l_sub.append(int(res[i][0].split()[-1]))
            i+=1
        sum_order = sum(l_sub)
    return sum_order
    

