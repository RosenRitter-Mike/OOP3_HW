import program as prog
from foodprod import FoodProduct
from datetime import datetime, timedelta
from pprint import pprint

cheddar = FoodProduct('Cheddar', 13, 'dairy', '07-12-2024', '15-02-2025')
tenderloin = FoodProduct('Tenderloin', 50, 'meat', '15-01-2025', '28-02-2025')
bok_choy = FoodProduct('Bok choy', 6, 'parve', '17-01-2025', '27-01-2025')
peanut_butter = FoodProduct('JIF peanut butter', 13, 'parve', '17-12-2024', '17-02-2025')

print(cheddar)
# print(f"Remaining days: {cheddar.remaining}")

prog.insert_product(cheddar)
prog.insert_product(tenderloin)
prog.insert_product(bok_choy)
prog.insert_product(peanut_butter)

pprint(prog.get_products())
