"""This is second logic."""

from warehouse import shopping


temp = []


def userWindow():
    """This function displays the menu.
    """
    print("=====================\n")
    print("1.\"Browse List\"")
    print("2.\"Place order\"")
    print("3.\"Pay order\"")
    print("4.\"Cancel order\"")
    print("5.\"Exit\"")
    print("\n===================")


def userDisplayMenuWindow():
    """This function displays the item in stock.
    """
    print("\nId\tName\tAvailable\tPrice")
    print("===================================================")
    for d in shopping:
        print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')


def catalogView(temp):
    """This function displays the item added to the shopping cart.
    """
    sumTotal = 0
    for i in temp:
        for key, value in i.items():
            if key == "Available":
                continue
            print(key, value)
            if key == "Price":
                sumTotal += i.get("Price")
        print('==============')
        print(f"Cost: {sumTotal}")
