import bl


def show_message(message):
    print(message + ".")


def get_value(message, end=":\n"):
    return input(message + end)


def show_categories():
    print(bl.get_categories())


def show_products():
    choose_category = get_value("Enter the category you are interested in")
    print(bl.get_products(choose_category))


def show_basket():
    print(bl.get_basket())


def add_to_basket():
    print(bl.get_categories())
    choose_category = get_value("Enter the category you are interested in")
    print(bl.get_products(choose_category))
    choose_product = get_value("Enter the product you want to add to basket")
    choose_quantity = get_value("Enter the quantity of products you want to add to basket")
    res = bl.add_to_basket(choose_category, choose_product, choose_quantity)
    show_message(res)


def remove_from_basket():
    print(bl.get_basket())
    choose_product = get_value("Enter the product you want to remove from basket")
    choose_quantity = get_value("Enter the quantity of products you want to remove from basket")
    res = bl.remove_from_basket(choose_product, choose_quantity)
    show_message(res)


def final_buy():
    res = bl.final_buy()
    show_message(res)


def main_flow():
    while True:
        choose_value = get_value("Choose your action:\n0. Exit\n1. Show categories\n"
                                 "2. Show products from category\n3. Make an order\n", end="")
        if choose_value == "0":
            break
        elif choose_value == "1":
            show_categories()
        elif choose_value == "2":
            show_products()
        elif choose_value == "3":
            while True:
                choose_value = get_value("Choose your action:\n0. Exit\n1. Add to basket\n"
                                         "2. Remove from basket\n3. Show basket\n4. Buy\n", end="")
                if choose_value == "0":
                    break
                elif choose_value == "1":
                    add_to_basket()
                elif choose_value == "2":
                    remove_from_basket()
                elif choose_value == "3":
                    show_basket()
                elif choose_value == "4":
                    final_buy()