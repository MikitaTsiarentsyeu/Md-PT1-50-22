import adapter_db

catalogue = adapter_db.return_data_from_database()
basket = {}


def get_categories():
    return catalogue.keys()


def get_products(choose_category):
    for category in catalogue.keys():
        if category == choose_category:
            return catalogue.get(choose_category)
    raise NameError("There is no such category in our catalogue")


def get_basket():
    return basket


def add_to_basket(choose_category, choose_product, choose_quantity):
    if choose_category in catalogue.keys():
        if choose_product in catalogue.get(choose_category):
            if catalogue.get(choose_category).get(choose_product)[2] >= int(choose_quantity):
                price = catalogue.get(choose_category).get(choose_product)[1]
                if choose_product not in basket:
                    basket[choose_product] = [price*int(choose_quantity), int(choose_quantity)]
                else:
                    basket[choose_product][0] += price
                    basket[choose_product][1] += int(choose_quantity)
                print(basket)
                return True
            else:
                raise RuntimeError(f"Only {catalogue.get(choose_category).get(choose_product)[2]} products left")
        else:
            raise NameError("There is no such product in our catalogue")
    else:
        raise NameError("There is no such category in our catalogue")


def remove_from_basket(choose_product, choose_quantity):
    if not basket:
        raise RuntimeError("Your basket is empty")
    else:
        if choose_product in basket:
            if int(choose_quantity) <= basket[choose_product][1]:
                if int(choose_quantity) == basket[choose_product][1]:
                    del basket[choose_product]
                else:
                    price = basket[choose_product][0]-basket[choose_product][0]/basket[choose_product][1]*int(choose_quantity)
                    basket[choose_product] = [price, int(choose_quantity)]
                return True
            else:
                raise RuntimeError("You cannot remove more products than you have in your basket")
        else:
            raise NameError("There is no such product in your basket")


def final_buy():
    global basket
    if not basket:
        raise RuntimeError("Your basket is empty")
    else:
        for product in basket.keys():
            for value in catalogue.values():
                if product in value:
                    value[product][2] -= basket[product][1]
        basket.clear()
        return True