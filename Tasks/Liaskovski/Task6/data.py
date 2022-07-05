
repo =     [{"id": 1,"Category":"Food",   "Name": "Ice cream", "Available": 54, "Price": 250},
            {"id": 2,"Category":"Food",   "Name": "Bread", "Available": 99, "Price": 323},
            {"id": 3,"Category":"Food",   "Name": "Apples", "Available": 100, "Price": 4764},
            {"id": 4,"Category":"Clothes","Name": "T-shirt", "Available": 20, "Price": 6043},
            {"id": 5,"Category":"Clothes","Name": "Cap", "Available": 15, "Price": 242},
            {"id": 6,"Category":"Clothes","Name": "Pants", "Available": 1, "Price": 3503},
            {"id": 7,"Category":"Drinks", "Name": "Water", "Available": 9, "Price": 99},
            {"id": 8,"Category":"Drinks", "Name": "Lemonade", "Available": 4, "Price": 4501},
            {"id": 9,"Category":"Drinks", "Name": "Juice", "Available": 40, "Price": 20011},
            {"id": 10,"Category":"Drinks","Name": "Kvass", "Available": 30, "Price": 12000}]

repo1 = []

def get_all_items():
    return repo


def get_all_items_in_basket():
    return repo1


def add_my_basket():
    order_number = 10
    p_id = int(input("\nEnter the id : "))
    for d in repo:
        try:
            if d["id"] == p_id:
                print("\nId\tName\tAvailable\tPrice")
                print("=============================================================")
                print(f'{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}')
                order = '{d["id"]}\t{d["Name"]}\t{d["Available"]}\t\t{d["Price"]}'
                conform = input("\nDo you want to place this order to your cart : Y/N ")
                if conform == 'Y' or conform == 'y':
                    print("\nThe order successfully placed to your shopping cart: {}-id, {}-name {}-price".format(d["id"], d["Name"],d["Price"]))
                    repo1.append([d["id"], d["Name"],d["Price"]])
                    order_number += 1
                    print("Your order number is : ", order_number)
                    d["Available"] -= 1
                    break
                elif conform == 'N' or conform == 'n':
                    print("The order is not placed. You can carry on with you purchase. Happy shopping!!!!")
                    break
                else:
                    print("\nYou have entered wrong option. Please enter again\n")
                    conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                    break
        except SyntaxError:
            print("Uncorrect")

def remove_item(name):
    for i in range(len(repo1)):
       
        if not name in repo1[i]:
            del repo1[i]
            break
        