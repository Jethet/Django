from ProductClass import Product
from InventoryClass import Inventory

apple1 = Product('apple', 0.3, True)
apple2 = Product('apple', 0.3, True)
apple3 = Product('apple', 0.3, True)
apple4 = Product('apple', 0.3, True)
apple5 = Product('apple', 0.3, True)

banana1 = Product('banana', 0.2, True)

inv_fruit = Inventory('Veritas')

inv_fruit.make_product_list(apple1)
inv_fruit.make_product_list(apple2)
inv_fruit.make_product_list(apple3)
inv_fruit.make_product_list(apple4)
inv_fruit.make_product_list(apple5)
inv_fruit.make_product_list(banana1)

inv_fruit.calculate_inventory()
print(inv_fruit.inventory_count)

inv_fruit.inventory_count.sell_product('apple1',1)
print(inv_fruit)
