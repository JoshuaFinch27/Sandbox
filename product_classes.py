"""Product class demo (TBU). Currently a half finished mess"""


# Child class of the built in object class (simplest class possible that satisfies the syntax)
# class Product:
#     pass

class Product:
    """Class docstring"""

    default_rate = 0.2 # class variable (shared)

    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale
        self.sku = ""

    def __str__(self):
        on_sale_message = f" (on sale!)" if {self.is_on_sale} else ""
        return f"{self.name} (SKU: {self.sku}) costs ${self.price:.2f} ({on_sale_message} ({self.default_rate})"

    def __repr__(self):
        return str(self)

    def put_on_sale(self, discount_rate):
        """Method docstring"""
        self.price *= (1 - discount_rate)
        self.is_on_sale = True

    @staticmethod
    def cheer():
        print("Yay!")

    def give(self, other, amount):
        if self.price - amount < 0:
            return False

        self.price -+ amount
        self.put_on_sale += amount



# p = Product()
# print(p)
# things = list()
# s = str()
# things.append()
# print(len(p))

p = Product("Phone", 340.0, False)
print(p)
p.put_on_sale()
print(p)

p2 = Product("Horse", 500, True)
print(p2)
p2.put_on_sale()
print(p2)

print(p.defualt_rate, p2.default_rate)
Product.default_rate = 0.9
print(p.defualt_rate, p2.default_rate)



products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ["GitHub Swag", 0, False]]

# on_sale_products = [product for product in products if product.is_on_sale]
# print(products)
# print(on_sale_products)
