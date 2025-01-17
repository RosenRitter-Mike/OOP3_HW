from datetime import datetime, timedelta


class FoodProduct:
    def __init__(self, name, price, category, production_date, expiration_date):
        self.__name = name
        self.__price = price
        self.__category = category
        self.production_date = production_date
        self.expiration_date = expiration_date

    def __str__(self):
        return (f"product name: {self.name}\nprice: {self.price}\ncategory: {self.category}\n"
                f"production date: {self.production_date}\nexpiration date: {self.expiration_date}\n"
                f"days until expiration: {self.remaining}")

    def __repr__(self):
        return (f"FoodProduct('{self.name}', '{self.price}', '{self.category}',"
                f" '{self.production_date}', '{self.expiration_date}')")

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.price == other
        elif isinstance(other, FoodProduct):
            return self.price == other.price
        else:
            raise TypeError(f"Unsupported type: {type(other)}")

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.price > other
        elif isinstance(FoodProduct, other):
            return self.price > other.price
        else:
            raise TypeError(f"Type can not be- {type(other)}")

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.price < other
        elif isinstance(FoodProduct, other):
            return self.price < other.price
        else:
            raise TypeError(f"Type can not be- {type(other)}")

    def __le__(self, other):
        return not self > other

    def __len__(self):
        return (datetime.now() - self.production_date).days

    def __add__(self, other):
        if isinstance(other, int):
            return self.price + other
        raise TypeError(f"Type can not be- {type(other)}")

    def __sub__(self, other):
        if isinstance(other, int):
            return self.price - other
        raise TypeError(f"Type can not be- {type(other)}")

    def __mul__(self, other):
        if isinstance(other, int):
            return self.price * other
        raise TypeError(f"Type can not be- {type(other)}")

    def __hash__(self):
        # return hash((self.name, self.price, self.category, self.production_date, self.expiration_date))
        return hash(self.price)

    @property
    def name(self):
        return self.__name;

    @property
    def price(self):
        return self.__price;

    @property
    def category(self):
        return self.__category;

    @property
    def production_date(self):
        return self.__production_date;

    @property
    def expiration_date(self):
        return self.__expiration_date;

    @property
    def remaining(self):
        return (self.__expiration_date - datetime.now()).days;

    @name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str):
            if len(new_name) > 2 and new_name[0] != new_name[1]:
                self.__name = new_name;
            else:
                raise ValueError(f"age cannot be {new_name}")
        else:
            raise TypeError(f"name must be str. cannot be- {type(new_name)}")

    @price.setter
    def set_price(self, new_price):
        if isinstance(new_price, (int, float)):
            if 0.1 <= new_price <= 100:
                self.__price = new_price
            else:
                raise ValueError(f"price cannot be {new_price}")
        else:
            raise TypeError(f"age must be float. cannot be- {type(new_price)}")

    @category.setter
    def set_category(self, new_category):
        if isinstance(new_category, str):
            if new_category == "parve" or new_category == "dairy" or new_category == "meat":
                self.__category = new_category;
            else:
                raise ValueError(f"category cannot be {new_category}")
        else:
            raise TypeError(f"category must be str. cannot be- {type(new_category)}")

    @production_date.setter
    def production_date(self, new_prod_date):
        # print(f"Setting production_date: {new_prod_date} type:{type(new_prod_date)}")
        if isinstance(new_prod_date, str):
            new_prod_date = parse_date(new_prod_date)
        if isinstance(new_prod_date, datetime):
            if new_prod_date < datetime.now():
                self.__production_date = new_prod_date
            else:
                raise ValueError(f"Production date cannot be in the future: {new_prod_date}")
        else:
            raise TypeError(f"Production date must be a date, not {type(new_prod_date)}")

    @expiration_date.setter
    def expiration_date(self, new_exp_date):
        # print(f"Setting expiration_date: {new_exp_date} type:{type(new_exp_date)}")
        if isinstance(new_exp_date, str):
            new_exp_date = parse_date(new_exp_date)
        if isinstance(new_exp_date, datetime):
            if new_exp_date > self.production_date + timedelta(days=7):
                self.__expiration_date = new_exp_date
            else:
                raise ValueError(f"Expiration date must be after the production date: {new_exp_date}")
        else:
            raise TypeError(f"Expiration date must be a datetime object or valid string, not {type(new_exp_date)}")


def parse_date(date_str):
    # print("in parse date")
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d-%m-%Y", "%d.%m.%Y"]
    for fmt in formats:
        try:
            # print("out parse date")
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Date string {date_str} does not match any known formats.")

