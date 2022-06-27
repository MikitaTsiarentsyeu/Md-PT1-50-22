import pandas as pd
import sys
from datetime import date

class Base():
    def __init__(self, name, phone):
        try:
            self.df = pd.read_csv('data.csv')
            self.phone = phone
            self.name = name
            self.cart = []
            self.order = []
        except FileNotFoundError as e:
            print('data not found')
            with open('error.txt', 'a') as errors:
                errors.write(f'{date.today()} - {e}')
            sys.exit()



    def attrib_not_found(func):
        def wrapper(*args):
            try:
                return func(*args)
            except (AttributeError, TypeError) as e:
                print('data not found (please recheck init data or send a message to administrator)')
                with open('error.txt', 'a') as errors:
                    errors.write(f'{date.today()} - {e}')
                sys.exit()
            except KeyError as e:
                with open('error.txt', 'a') as errors:
                    errors.write(f'{date.today()} - {e}')
                sys.exit()
                print('do not have a column (please recheck all key values or send a message to administrator)')
        return wrapper


    @attrib_not_found
    def range_of_price(self, start, end, category, *args):
        return self.df[(self.df.price.between(start,end)) & (self.df[category].isin(args))][['id','category','name', 'price']].to_string(index = False)

    @attrib_not_found
    def add_items(self, id):
            self.df.at[self.df[self.df["id"] == int(id)].index[0],'quantity'] += 1
            self.df.to_csv('data.csv', index=False)

    @attrib_not_found
    def del_item(self, id):
       return self.df.drop(self.df[self.df["name"] == id].index, inplace= True)

    @attrib_not_found
    def get_items(self, key, *args):
        return self.df.loc[self.df[key].isin(args)]

    @attrib_not_found
    def search_items(self,key,*args):
        return self.df.loc[self.df[key].isin(args)][['id','category','name','price']].to_string(index=False)

    

    @attrib_not_found
    def show_all_data(self):
        return self.df[['id', 'category', 'name', 'price']].to_string(index=False)
    @attrib_not_found
    def is_in_df(self,category, item):
        return self.df[category].isin([item]).any()

    @attrib_not_found
    def show_all_names(self):
        return self.df.name.unique()

    @attrib_not_found
    def show_all_id(self):
        return self.df.id.values.tolist()

    @attrib_not_found
    def show_all_categories_str(self):
        [print(f'{i}', sep=', ') for i in self.df['category'].unique()]
        return len(self.df['category'].unique())

    @attrib_not_found
    def return_all_categories(self):
        return self.df['category'].unique().tolist()

    @attrib_not_found
    def choose_item(self, *id):
        items = self.get_items('id', *id).values.tolist()
        [self.cart.append({'id':i[0], 'category':i[1], 'name':i[2], 'price':i[3] }) for i in items]
        

    @attrib_not_found
    def buy_items(self):
        if self.cart:
            for i in self.cart:
                self.df.loc[self.df['id'] == i['id'], 'quantity'] -= 1
                if self.df.loc[(self.df['id'] == i['id']) & (self.df['quantity'] == 0)].empty:
                    self.del_item(i["id"])
            self.df.to_csv('data.csv', index=False)   #update information of data if order access
            
            with open('orders.txt', 'a') as orders:
                orders.write(f'{self.name} (phone - {self.phone}) - {[i for i in self.cart]}\n')

            self.order = self.cart
            self.cart = []
             
    def delete_from_cart(self, id):
        for en,i in enumerate(self.cart):
            if i['id'] == id:
                self.add_items(id)
                self.cart.pop(en)
                
        
        
        
if __name__ == '__main__':
    db = Base('qweqwe', '123123')
   




            
           
        
    

    
    



            
        

