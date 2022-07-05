from db import Base

class User():
    def __init__(self,name, phone):
        self.db = Base(name, phone)
        
        
    def print_message(self, message): 
        print(f'{message}\n----------')
        
    def hello(self):
        print(f'Hello, {self.db.name}!\nWelcome to our shop')
    
    def show_name(self):
        try:
            if self.db.name:
                return self.db.name
            else: raise ValueError
        except ValueError:
            print('name is empty')
    
    def show_all_data(self):
        self.print_message('all items')
        print(self.db.show_all_data())
        
    def show_all_categories(self): 
        self.print_message('all categories')
        self.db.show_all_categories_str()


    def is_in_data(self, cat, item):
        return self.db.is_in_df(cat, item)

    def return_all_categories(self):
        return self.db.return_all_categories()

    def show_all_names(self):
        print('we have:')
        print(*self.db.show_all_names(), sep=', ')
            
    def search_items(self, key, *args):
        if not self.db.get_items(key,*args).empty:
            print(self.db.search_items(key, *args))
        else:
            raise ValueError

    def range_of_price(self, start, end, category, *args):
        print(self.db.range_of_price(start, end,category, *args))

    def show_cart(self): 
        return self.db.show_cart()
        
    def add_item_to_cart(self,*id):
        print(f'item with id {id} adding to cart')
        self.db.choose_item(*id)

    def show_all_id(self):
         return self.db.show_all_id()
                
    def delete_from_cart(self, id): 
        for i in self.db.cart:
            if i['id'] == id:
                self.db.delete_from_cart(id)
                self.db.add_items(id)
                self.show_cart()
                return ''
            else: raise ValueError
            
    def show_cart(self):
        print('in cart:\n')
        [print(f'id - {i["id"]}; name - {i["name"]}; price-{i["price"]}\n') for i in self.db.cart]

    def buy_items(self):
        
        if self.db.cart:
            self.db.buy_items()
            print(f'Your order, {self.db.name}:\n{self.db.order}')
        else:
            print('sorry, your cart is empty')
        
    def clear_cart(self):
        self.db.cart = []
        
        
        
