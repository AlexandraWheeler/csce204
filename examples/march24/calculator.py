def getPrice():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid price")

def getQuantity():
    while True:
        try:
            quantity = int(input("Enter quanitity: "))
            return quantity
        except ValueError:
            print("Invalid quanitity, Enter a whole number.")

price = getPrice()
quantity = getQuantity()

# Calculator
total = price * quantity
print(f"You total is {total}.")
        