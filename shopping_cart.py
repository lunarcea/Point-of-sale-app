#shopping_cart.py
#Author: Eunah Cho(ID: lunarcea)
#Reference: https://github.com/alpineghost/Python_Practice

import code
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#Checkpoint 1

product_ids = []

while True:
    product_id = input("Hey please input a product identifier: ")
    if product_id == "DONE":
        break
    else:
        product_ids.append(int(product_id))


#Checkpoint 2

def matching_product(product_identifier):
    products_list = [p for p in products if p["id"] == product_identifier]
    return products_list[0]

raw_total = 0

print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:" + format(product_ids))

for pid in product_ids:
    product = matching_product(int(pid))
    # raw_total = raw_total + product["price"]
    raw_total += product["price"]
    price_usd = '${0:.2f}'.format(product["price"])
    print(" + " + product["name"] + " " + str(price_usd))

print("-------------------------")
print("THE TOTAL PRICE IS" + " " + '${0:.2f}'.format(raw_total))

#Checkpoint 3

running_total = 0

def lookup_id(id):
    for p in products:
        if product["id"] == int(id):
           price_usd = '${0:.2f}'.format(product["price"])
           print(" + " + product["name"] + " (" + price_usd + ")")

def lookup_price(id):
    for product in products:
        if product["id"] == int(id):
            return product["price"]

def lookup_product_by_id(product_id):
    matching_products = [product for product in products if product["id"] == product_id]
    return matching_products[0]

print ("-------------------------")
print("VIVA GROCERY")
print("-------------------------")
print("Web: www.vivagrocery.com")
print("Phone: 718-123-4567")
print("Checkout Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%m:%S"))
print("-------------------------")
print("Shopping Cart Items:")

for id in product_ids:
    product = lookup_product_by_id(id)
    running_total += lookup_price(id)
    price_usd = ' (${0:.2f})'.format(product["price"])
    print(" + " + product["name"] + price_usd)

print("-------------------------")
print("Subtotal:", '${0:.2f}'.format(running_total))
tax = running_total * 0.08875
print("Plus NYC Sales Tax (8.875%):", '${0:.2f}'.format(tax))
total = running_total + tax
print("Total:", '${0:.2f}'.format(total))

print("-------------------------")
print("Thank you for stopping with us. Please come back again!")
