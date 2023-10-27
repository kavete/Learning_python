products = ["Phones", "Laptops", "Televisions"]

print(products[0])

print(products[-1])

# for product in products:
#     print(product)

products.append("Cameras")
products.insert(0, "Desktops"), 

print(products)

products.sort(reverse=True)

print(products)

products.remove("Televisions")

print(products)

products.pop(0)

print(products)
