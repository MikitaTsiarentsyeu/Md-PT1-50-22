import pandas as pd
import sys
from datetime import date





try:
    df = pd.read_csv('data.csv')
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
            print(e)
            print('data not found (please recheck init data or send a message to administrator)')
            with open('error.txt', 'a') as errors:
                errors.write(f'{date.today()} - {e}')
            sys.exit()
        except KeyError as e:
            print('do not have a column (please recheck all key values or send a message to administrator)')
            with open('error.txt', 'a') as errors:
                errors.write(f'{date.today()} - {e}')
            sys.exit()
                
    return wrapper
    
        




@attrib_not_found
def range_of_price( start, end, category, *args):
    return df[(df.price.between(start,end)) & (df[category].isin(args))][['id','category','name', 'price']].to_string(index = False)
 


@attrib_not_found
def add_items(cls, id):
        df.at[cls.df[cls.df["id"] == int(id)].index[0],'quantity'] += 1
        df.to_csv('data.csv', index=False)


 

@attrib_not_found
def del_item(id):
    return df.drop(df[df["name"] == id].index, inplace= True)


 
@attrib_not_found
def get_items( key, *args):
    return df.loc[df[key].isin(args)]

   

@attrib_not_found
def search_items(key,*args):
    return df.loc[df[key].isin(args)][['id','category','name','price']].to_string(index=False)

    

@attrib_not_found
def show_all_data():
    return df[['id', 'category', 'name', 'price']].to_string(index=False)
    
   

@attrib_not_found
def is_in_df( category, item):
    return df[category].isin([item]).any()


@attrib_not_found
def show_all_names():
    return df.name.unique()

   

@attrib_not_found
def show_all_id():
    return df.id.values.tolist()


@attrib_not_found
def show_all_categories_str():
    [print(f'{i}', sep=', ') for i in df['category'].unique()]
    return len(df['category'].unique())
   

@attrib_not_found
def return_all_categories():
    return df['category'].unique().tolist()

 
@attrib_not_found
def delete_some_items( cart): 
        for i in cart:
            df.loc[df['id'] == i['id'], 'quantity'] -= 1
            if df.loc[(df['id'] == i['id']) & (df['quantity'] == 0)].empty:
                del_item(i["id"])
            df.to_csv('data.csv', index=False)

 
        


   
                





            
           
        
    

    
    



            
        

