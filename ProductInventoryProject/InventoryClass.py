class Inventory:

    def __init__(self, store_type):
        self.store_type = store_type
        self.product_list = []
        self.inventory_count = {}

    def calculate_inventory(self):
        for item in self.product_list:
            if item.get_type() in self.inventory_count.keys():
                self.inventory_count[item.get_type()] +=1
            else:
                self.inventory_count[item.get_type()] = 1

    def make_product_list(self, product):
        self.product_list.append(product)

    def sell_product(self, product, number_sold):
        if product in self.product_list:
            self.inventory_count[item.get_type()] - number_sold



        # create sell_apple or something (keep track inventory)
