"""This is main logic."""

from second_logic import userDisplayMenuWindow, userWindow, catalogView, shopping, temp


def user_id():
    """This function works with the entered id.
    """
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))


def removeCart():
    """This function is responsible for removing an item from the shopping cart.
    """
    try:
        if temp == []:
            print("\n====================")
            print("\"Cart is empty\"")
        if temp != []:
            order_del = input("To remove the entire order, enter - \"d\": ")
        if order_del == "d":
            temp.clear()
            for i in shopping:
                if i["Available"] < c:
                    i["Available"] += 1
                    print("=========================")
                    print("\"Cart has been emptied\"")
                    print("=========================")
        else:
            print("\n\"The items in the cart have not been removed\"")
            print("\"Please select Cancel order and press - \"d\":\n")
            
    except UnboundLocalError:
        print("\"Please add an item\"")
        print("======================\n")


def payOrder(temp):
    """This function is responsible for the purchase of goods.
    """
    sumTotal = 0
    if temp == []:
        print("\n=================================")
        print("Select a product and add to cart")
        print("=================================\n")
        userDisplayMenuWindow()
        userWindow()
        userChoiceOptions()
    else:
        for i in temp:
            for key, value in i.items():
                if key == "Available":
                    continue
                print(key, value)
                if key == "Price":
                    sumTotal += i.get("Price")
            print('==============')
        print(f"Total cost: {sumTotal}", "\n")
        print("\"Thanks for shopping\"\n")


def placeOrder():
    """This function is responsible for adding the product to the cart.
    """
    order_number = 0
    userDisplayMenuWindow()
    p_id = int(input("\nEnter the id : "))

    for d in shopping:
        if d["id"] == p_id:
            print("\nId\tName\tAvailable\tPrice")
            print("=============================================================")
            print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")
            
            if d["Available"] == 0:
                print("\n""===============================")
                print("\"This position is not available\"")
                userWindow()
                userChoiceOptions()
                break
            
            if conform == 'Y' or conform == 'y':
                print("\nSuccessfully placed the order on the product {} {}".format(d["id"], d["Name"]))
                order_number += 1
                print("Your order number is : ", order_number, "\n")
                global c
                c = d["Available"]
                d["Available"] -= 1
                temp.append(d)
                print("=============")
                print("Shopping cart")
                print("=============")
                catalogView(temp)
                break

            elif conform == 'N' or conform == 'n':
                print("\"The order is not placed. You can carry on with you purchase. To add an order choose \"Place order.\"\n\"Happy shopping!!!!\"")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                print("\"Please - enter the id :\"\n")
                placeOrder()
                break

    if d["id"] != p_id:
        print("\n\"You have entered invalid id. Please enter valid id\"\n")
        user_id()


def userChoiceOptions():
    """This function is responsible for the choice of the user.
    """
    try:
        choice = int(input("Please enter user choice : "))
        if choice == 1:
            userDisplayMenuWindow()
            print("\n===================================================\n")
            userWindow()
            print("\n===================================================\n")
            userChoiceOptions()
        elif choice == 2:
            placeOrder()
            print("\n===================================================\n")
            userWindow()
            print("\n===================================================\n")
            userChoiceOptions()
        elif choice == 3:
            payOrder(temp)
        elif choice == 4:
            removeCart()
            userDisplayMenuWindow()
            userWindow()
            userChoiceOptions()
        elif choice == 5:
            print("\n\"Thank you for visiting our shop.\"\n")
            exit()
        else:
            print("\n\"Please enter valid choice\"\n")
            userWindow()
            userChoiceOptions()
    except ValueError:
        print("\n\"Invalid Choice. Please enter valid choice\"")
        userWindow()
        userChoiceOptions()
