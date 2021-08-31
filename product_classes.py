"""Product class demo (TBU). Currently a half finished mess"""


# Child class of the built in object class (simplest class possible that satisfies the syntax)
# class Product:
#     pass

class Product:
    def __init__(self):
        # print("Hello")
        self.name = ""
        self.price = 0.0
        # self.is_on_sale = False  # Instance variable, persists outside(?) program
        self.is_on_sale = is_on_sale

    def __str__(self):
        return f"{self.name} costs ${self.price} ({self.is_on_sale})"


    def __len__(self):
        return 7

# p = Product()
# print(p)
# things = list()
# s = str()
# things.append()
# print(len(p))

p = Product("Phone", 340.0, False)





products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ["GitHub Swag", 0, False]]

on_sale_products = [product for product in products if product.is_on_sale]
print(products)
# print(on_sale_products)
















