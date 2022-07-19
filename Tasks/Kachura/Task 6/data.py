

repo = {1: ('item', ('rods', 'carp fishing'), 130, [5]), 2: ('item', ('hooks', 'carp fishing'), 5, [150])}


repo_cart = {}


def change_stock_bal(id, num):
    repo[id][3][0] = repo[id][3][0] - num


def get_category_list():
    cat_list = []
    for i in repo.values():
        for j in i[1]:
            cat_list.append(j)
    cat_list = set(cat_list)
    return cat_list


def search_by_category(request):
    res = {}
    for k, v in repo.items():
        if request in v[1]:
            res[k] = v
    return res


def add_to_cart(id, num):
    repo_cart[id] = num


def go_to_cart():
    return repo_cart


def set_delivery_address(del_address):
    res = {}
    for k, v in repo_cart.items():
        res[k] = (v, del_address)
    return res

