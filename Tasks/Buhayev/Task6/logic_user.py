
import db as base


class Storage_user_logic():

    db = base  
    
    @classmethod
    def show_all_data(cls):
        print('all items')
        print(cls.db.show_all_data())
        
    @classmethod    
    def show_all_categories(cls): 
        print('all categories')
        cls.db.show_all_categories_str()
        
    @classmethod
    def is_in_data(cls, cat, item):
        return cls.db.is_in_df(cat, item)
    
    @classmethod
    def return_all_categories(cls):
        return cls.db.return_all_categories()
    
    @classmethod
    def show_all_names(cls):
        print('we have:')
        print(*cls.db.show_all_names(), sep=', ')
        
    
    @classmethod
    def search_items(cls, key, *args):
        if not cls.db.get_items(key,*args).empty:
            print(cls.db.search_items(key, *args))
        else:
            raise ValueError
        
    @classmethod
    def range_of_price(cls, start, end, category, *args):
        print(cls.db.range_of_price(start, end,category, *args))
        
    @classmethod
    def show_all_id(cls):
         return cls.db.show_all_id()
     
    @classmethod
    def show_all_id(cls):
         return cls.db.show_all_id()
                
    
            
            
            
class User(Storage_user_logic):
    
    
    def __init__(self,name, phone):
        self.phone = phone
        self.name = name
        self.cart = []
        self.order = []
        
        
    def write_order(self):
        with open('orders.txt', 'a') as orders:
                orders.write(f'{self.get_name()} (phone - {self.get_phone()}) - {[i for i in self.get_cart()]}\n')
        
    def hello(self):
        print(f'Hello, {self.name}!\nWelcome to our shop')
    
    def get_phone(self):
        return self.phone
    
    def get_name(self):
        return self.name
    
    def show_name(self):
        try:
            if self.name:
                return self.name
            else: raise ValueError
        except ValueError:
            print('name is empty')
    
    def delete_from_cart(self, id): 
        for en,i in enumerate(self.cart):
            if i['id'] == id:
                self.db.add_items(id)
                self.cart.pop(en)
                Storage_user_logic.db.add_items(id)
                self.show_cart()
                return ''
            else: raise ValueError
            
    def buy_items_logic(self):
        if self.cart:
            self.db.delete_some_items(self.cart)
            self.order = self.get_cart()
            self.cart = []
            return True
            
    def buy_items(self):
        if self.cart:
            self.buy_items_logic()
            print(f'Your order:\n{self.order}')
        else:
            print('sorry, your cart is empty')
    
       
    def clear_cart(self):
        self.cart = []
        
    def show_cart(self):
        print('in cart:\n')
        [print(f'id - {i["id"]}; name - {i["name"]}; price-{i["price"]}\n') for i in self.get_cart]
        
    def show_cart(self): 
        print(self.cart)
        
    def get_cart(self): 
        return self.cart
    
    def choose_item(self, *id):
        items = self.db.get_items('id', *id).values.tolist()
        [self.cart.append({'id':i[0], 'category':i[1], 'name':i[2], 'price':i[3] }) for i in items]
        
        
    def add_item_to_cart(self,*id):
        print(f'item with id {id} adding to cart')
        self.choose_item(*id)
        self.show_cart()
              
    

   
    
    
if __name__ == '__main__':
    
    test = User('name', 'phone')
    print(test.show_all_data())
    print(base.df)
        
  
              
    
                
                

    
    
        
        
        
