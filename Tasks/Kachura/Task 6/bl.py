import data

def get_category_list():
    res = data.get_category_list()
    return '\n'.join(res)

def search_by_category(request):
    res = data.search_by_category(request)
    print('Total items found: ', len(res))
    print('id, item, category, price, stock_bal')
    return res

def add_to_cart(res):
    id, num = res.split(',')
    data.add_to_cart(id, num)


def go_to_cart():
    res = data.go_to_cart()
    print('Total items in cart: ', len(res))
    print('item id, qty')
    return res

def set_delivery_address(del_address):
    res = data.set_delivery_address(del_address)
    print('item id, qty, delivery address')
    return res