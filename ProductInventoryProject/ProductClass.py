class Product:

    def __init__(self, type, price, is_organic):
        self.type = type
        self.price = price
        self.is_organic = is_organic

    def get_type(self):
        return self.type

    def get_price(self):
        return self.price

    def is_organic(self):
        return self.is_organic
