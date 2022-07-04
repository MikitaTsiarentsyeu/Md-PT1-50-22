import data


def get_all_items():                    #to see the entire catalog
    res = data.get_all_items()
    Total = 0
    print("\n")
    for d in  res:
        print(f'id {d["id"]} category {d["Category"]}-- name {d["Name"]}--- available {d["Available"]} -- price {d["Price"]}')
        Total += (d["Available"])
    print("\nTotal available goods is : ", Total)




def get_all_items_in_basket():                          #to see all items in my cart
    res = data.get_all_items_in_basket()
    return '\n'.join([f"{c[0]}-id: {(c[1])}-name:{c[2]}-price" for c in res])


def remove_item(name):
    res = data.remove_item(name)
    return format_response(res, "Item has been removed from your cart")

def format_response(res, message):
    if res:
        items = get_all_items()
        return f"{message}:\n{items}"
    else:
        return "Something went wrong"


def add_my_basket():
    res = data.add_my_basket()
    return format_response(res, "The item has been added to your cart")