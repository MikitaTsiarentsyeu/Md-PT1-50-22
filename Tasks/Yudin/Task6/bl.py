import data

def show_dodge():
    res = data.show_dodge()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def show_cadillac():
    res = data.show_cadillac()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def show_bentley():
    res = data.show_bentley()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def show_renault():
    res = data.show_renault()
    return '\n'.join([f"{x[0]}: {', '.join(x[1:3])}, price is {x[3]} USD" for x in res])

def add_item(code):
    res = data.add_item(code)
    if res == False:
        print("No position found.\n")
    else:
        print("The position was added to the cart.")
        return res

def remove_item(code): 
    res = data.remove_item(code)
    if res == True:
        print("The position was removed\n")
        return data.check_cart()      
    else:
        print("There's no such position in the cart")
        
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
    

