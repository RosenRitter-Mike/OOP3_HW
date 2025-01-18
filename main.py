import program as prog
from foodprod import FoodProduct
from datetime import datetime, timedelta
from pprint import pprint

cheddar = FoodProduct('Cheddar', 13, 'dairy', '07-12-2024', '15-02-2025')
tenderloin = FoodProduct('Tenderloin', 50, 'meat', '15.01.2025', '28.02.2025')
bok_choy = FoodProduct('Bok choy', 6, 'parve', '17/01/2025', '27/01/2025')
peanut_butter = FoodProduct('JIF peanut butter', 13, 'parve', '12-17-2024', '02-17-2025')
matsoni = FoodProduct('Matsoni caspian sea yogurt ', 10, 'dairy', datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=30))
char_siu = FoodProduct('Cantonese smoked duck', 40, 'meat', '2025-01-15', '2025-02-28')

print(cheddar)

prog.insert_product(cheddar)
prog.insert_product(tenderloin)
prog.insert_product(bok_choy)
prog.insert_product(peanut_butter)
prog.insert_product(matsoni)
prog.insert_product(char_siu)

pprint(prog.get_products())
