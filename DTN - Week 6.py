"""
Lecture 6 DTN

Write a list comprehension to produce a new list containing only the products that are on sale (True means its on sale)

"""

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ["GitHub Swag", 0, False]]

on_sale_products = [product for product in products if product[2]]
print(products)
print(on_sale_products)
