# ecommerce/main.py
from products import catalog, inventory
from customers import profile
from orders import cart, checkout
from payments import credit_card

print(catalog.get_products())
print(inventory.check_stock())
print(profile.get_customer())
print(cart.add_to_cart("Laptop"))
print(checkout.process_order())
print(credit_card.pay_cc(1000))