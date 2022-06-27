from logic_user import User
import sys

class UI:
    def __init__(self):
        self.user = self.create_profile()

    def create_profile(self):
        name = self.check_main_input('name')()
        phone = self.check_main_input('phone')()
        user = User(name, phone)
        user.hello()
        return user

    def main(self):
        inp = self.answer('string','Do you need to help of our bot')()
        if inp == 'yes':
            self.bot_help()
        elif inp == 'no':
            inp = self.answer('string','Do you want to continue continue in default mode')()
            if inp == 'yes':
                self.default_show()
            else:
                print('we very sad that we can\'t to help you')
                self.goodbye()

    def default_show(self):
        inp = self.check_main_choice()
        if inp == 1:
            self.user.show_all_data()
            self.is_continue()
        elif inp == 2:
            self.user.show_all_categories()
            self.is_continue()
        elif inp == 3:
            items = self.search_item('category')
            self.range_price('category', *items)
            self.add_item_to_cart()
            self.is_continue()
        elif inp == 4:
            self.user.show_all_names()
            items = self.search_item('name')
            self.range_price('name', *items)
            self.add_item_to_cart()
            self.is_continue()
        elif inp == 5:
            self.watch_cart()
            if self.user.db.cart:
                self.finish_order()
            else:
                print('you cart is empty')
                self.is_continue()
        elif inp == 6:
            self.user.buy_items()
            self.is_continue()
        elif inp == 7:
            self.goodbye()

    def bot_help(self):
        print(f'Ok, {self.user.show_name()}, what you search?')
        category = self.choose_category_bot()
        self.range_price('category', *category)
        print('Ok, at last you can shoose product what you want and add in to cart =)')
        id = self.split_array_of_items("id's", 'id')
        self.user.add_item_to_cart(*id)
        self.user.show_cart()
        self.finish_order()

    def split_array_of_items(self, cat_str, category):
        try:
            inp = self.small_input(f'please enter interesting {cat_str} (separator ",")').split(',')
            if category == 'id':
                in_inp = [int(i) for i in inp if self.user.is_in_data(category, int(i))]
                not_inp = [i.strip() for i in inp if not self.user.is_in_data(category, int(i))]
            else:
                in_inp = [i.strip() for i in inp if self.user.is_in_data(category, i.strip())]
                not_inp = [i.strip() for i in inp if not self.user.is_in_data(category, i.strip())]
            if not_inp:
                print(f'sorry, but we cannot find this items: {" ".join(not_inp)}')
            return in_inp
        except ValueError:
            print('sorry you enter invalid value for category')
            return self.split_array_of_items(cat_str, category)


    def small_input(self, mes):
        return input(f'{mes}:\n')


    def check_number(self, str):
        try:
            return int(self.small_input(f'Your choice: {str}'))
        except:
            print('Sorry, number is incorrect, please try again')
            return self.check_number(str)

    def check_main_choice(self):
        try:
            print(
                'please choose:\n1:show all items\n2:show all categories\n3:search by category\n4:search by item name\n5:watch a cart\n6:finished buy\n7:exit')
            inp = self.check_number('')
            if inp in range(1, 9):
                return inp
            else:
                raise ValueError
        except ValueError:
            print('Sorry, your input is invalid')
            self.default_show()


    def check_main_input(self, toggle):
        if toggle == 'phone':
            def check_input():
                inp = (self.small_input('please enter your phone (xxxxx-xx-xx)')).split('-')
                check = all(i.isdigit() for i in inp) and len(inp) == 3 and len(inp[0]) == 4 and len(inp[1]) == len(inp[2]) == 2
                try:
                    if check:
                        return '-'.join(inp)
                    else: raise ValueError
                except ValueError:
                    print('sorry invalid phone')
                    return check_input()

        elif toggle == 'name':
            def check_input():
                try:
                    name = self.small_input('please, enter your name')
                    if name.strip():
                        return name
                    else: raise ValueError
                except ValueError:
                    print('your name is empty')
                    return check_input()
        return check_input


    def range_price(self, category, *args):
        check = self.answer('string', 'do you want to search items in some range of price')()
        if check == 'yes':
            start = self.check_number(' start of range of price')
            end = self.check_number(' end of range of price')
            print(self.user.range_of_price(start, end, category, *args))
        else:
            return



    def answer(self, toggle,string):
        if toggle == 'string':
            def simple_answer():
                try:
                    inp = input(f'{string}? (yes, no):\n')
                    if inp in ['yes', 'no']: return inp
                    else: raise ValueError
                except ValueError:
                   print('Sorry, cannot understand answer')
                   return simple_answer()

        elif toggle == 'number':
            def simple_answer():
                try:
                    inp = input(f'{string}:\n')
                    if int(inp) in [1,2,3]: return inp
                    else: raise ValueError
                except ValueError:
                   print('Sorry, cannot understand answer')
                   return simple_answer()
        return simple_answer

    def is_continue(self):
        inp = self.answer('string', 'Do you want to continue?')()
        if inp == 'yes':
            self.default_show()
        elif inp == "no":
            if self.user.db.cart:
                self.user.db.cart = []
            self.goodbye()

    def watch_cart(self):
        self.user.show_cart()

    def show_all_names(self):
        print('we have:\n')
        self.user.show_all_names()

    def search_item(self, category,):
        try:
            if category == 'category':
                self.user.show_all_categories()
                inp = self.split_array_of_items('categories',category)
                self.user.search_items(category, *inp)
                return inp
            elif category == 'name':
                it = self.split_array_of_items('items', category)
                self.user.search_items(category, *it)
                return it
        except ValueError:
            print('Sorry, we cannot find that item, maybe you want to find something else?')
            return self.search_item(category)

    def add_item_to_cart(self):
        check = self.answer('string', 'Do you want to add some item to the cart?')()
        if check == 'yes':
            inp = self.split_array_of_items('id\'s', 'id')
            self.user.add_item_to_cart(*inp)
            self.finish_order()
        else:
            self.is_continue()
            
    def delete_some_item_from_cart(self): 
        self.watch_cart()
        try: 
            inp = int(self.small_input('please enter id of item to delete'))
            self.user.delete_from_cart(inp)
            self.is_continue()
        except ValueError: 
            print('Sorry, we cannot find that item, maybe you want to find something else?')
            self.delete_some_item_from_cart()
        
    def finish_order(self):
        check = self.answer('string','do you want to finish order')()
        if check == 'yes':
            self.user.buy_items()
            self.is_continue()
        elif check == 'no':
            check = self.answer('number','do you want to:\n 1:delete some item from cart\n 2:clear cart\n 3:continue')()
            if check == '1': 
                self.delete_some_item_from_cart()
                self.is_continue()
            elif check == '2':
                self.user.clear_cart()
                self.is_continue()
            elif check == '3':
                self.default_show()

    def choose_category_bot(self):
        self.user.show_all_categories()
        try:
            category = self.split_array_of_items('categories', 'category')
            if category:
                print(f'Great job, {self.user.show_name()}, this is all products of category(ies): {" ".join(category)}:')
                self.user.search_items('category', *category)
                return category
            raise ValueError
        except ValueError:
            print('sorry, we can not find any category')
            return self.choose_category_bot()

    def goodbye(self):
        print("Thank you for your time! come back again")
        sys.exit()

        
        
        
        
        

   


if __name__ == '__main__':

    user = UI()
    user.main()

