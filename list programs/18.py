#Create a shopping cart using a list.
#Perform: 
#Add item 
#Remove item 
#Search item 
#Display cart 
#Count total items

cart = []

cart.append("Apple")
cart.append("Milk")
cart.append("Bread")
print(cart)
cart.remove("Milk")
print("Updated Cart: ", cart)
search = "Apple"
if search in cart:
    print(f"{search} is in the cart.")
else:
    print(f"{search} is not in the cart.")

print("Cart contents:", cart)
print("Total items:", len(cart))