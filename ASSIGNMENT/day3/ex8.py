quantity = int(input("Enter quantity: "))
price = quantity * 5

if quantity > 50:
    price = price - (price * 0.15)
elif quantity > 30:
    price = price - (price * 0.10)

print("Total Price =", price)