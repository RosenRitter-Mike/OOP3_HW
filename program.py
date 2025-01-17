import sqlite_lib as sl
from foodprod import FoodProduct
from datetime import datetime, timedelta

sl.connect('FoodProd.db')

print("Creating table if it does not exist...")
sl.run_query_update('''
CREATE TABLE IF NOT EXISTS FoodProducts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price FLOAT NOT NULL,
    category TEXT NOT NULL,
    production_date TEXT NOT NULL,
    expiration_date TEXT NOT NULL
);
''')
print("Table creation executed.")


def insert_product(insert_prod: FoodProduct) -> None:
    sl.connect('FoodProd.db')

    query = '''
    INSERT INTO FoodProducts (name, price, category, production_date, expiration_date)
    VALUES (?, ?, ?, ?, ?)
    '''
    sl.run_query_update(query, (
                                insert_prod.name,
                                insert_prod.price,
                                insert_prod.category,
                                insert_prod.production_date.strftime('%d-%m-%Y'),
                                insert_prod.expiration_date.strftime('%d-%m-%Y')
                                ))


def get_products() -> list[FoodProduct]:
    sl.connect('FoodProd.db');

    result = sl.run_query_select('''
                SELECT name, price, category, production_date, expiration_date FROM FoodProducts
            ''');
    return [FoodProduct(
        name=row[0],
        price=row[1],
        category=row[2],
        production_date=datetime.strptime(row[3], '%d-%m-%Y'),
        expiration_date=datetime.strptime(row[4], '%d-%m-%Y')
    ) for row in result]

