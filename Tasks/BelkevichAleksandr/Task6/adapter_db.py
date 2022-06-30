import psycopg2
from psycopg2 import Error


def __creat_table_in_database():
    try:
        conn = psycopg2.connect(dbname="testdb", 
                                user="postgres", 
                                password="postgres", 
                                port=5433)

        cur = conn.cursor()

        cur.execute('''CREATE TABLE cars  
                    (car_id serial PRIMARY KEY,
                    car_name TEXT NOT NULL,
                    products_code INT NOT NULL,
                    price INT,
                    in_stock int);''')

        cur.execute('''INSERT INTO cars (car_name, products_code, price, in_stock) VALUES
                    ('BMW', 11, 55000, 250),
                    ('Audi', 12, 10, 4800),
                    ('Tesla', 13, 500, 9420),
                    ('Fiat', 14, 6099, 670)''')


        cur.execute('''CREATE TABLE computers  
                    (computer_id serial PRIMARY KEY,
                    computer_name TEXT NOT NULL,
                    products_code INT NOT NULL,
                    price INT,
                    in_stock int);''')

        cur.execute('''INSERT INTO computers (computer_name, products_code, price, in_stock) VALUES
                    ('Lenovo', 21, 100, 2533330),
                    ('Asus', 22, 10000, 32999),
                    ('Apple', 23, 50, 12200),
                    ('LG', 24, 60, 5150)''')


        cur.execute('''CREATE TABLE phones  
                    (phone_id serial PRIMARY KEY,
                    phone_name TEXT NOT NULL,
                    products_code INT NOT NULL,
                    price INT,
                    in_stock int);''')

        cur.execute('''INSERT INTO phones (phone_name, products_code, price, in_stock) VALUES
                    ('IPhone', 31, 1200, 25),
                    ('Nokia 3310', 32, 1500000, 999),
                    ('Samsung Galaxy', 33, 850, 200),
                    ('Xaiomi P40', 34, 600, 450)''')

        conn.commit()
    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Connection closed with PostgreSQL")


def __database_date(name_table):
    try:
        conn = psycopg2.connect(dbname="testdb", 
                                user="postgres", 
                                password="postgres", 
                                port=5433)

        cur = conn.cursor()
        postgreSQL_select_Query = f"select * from {name_table}"

        cur.execute(postgreSQL_select_Query)
        mobile_records = cur.fetchall()
        
        products_category = {}

        for row in mobile_records:
            products_category[row[1]] = list(row[2::])

    except (Exception, Error) as error:
        print("Error while working with PostgreSQL", error)
    finally:
        if conn:
            cur.close()
            conn.close()
            print("Connection closed with PostgreSQL")
            return products_category


def return_data_from_database():
    categories = ['cars', 'computers', 'phones']
    products = {}
    __creat_table_in_database()

    for name_categories in categories:
        products[name_categories] = __database_date(name_categories)

    return products        